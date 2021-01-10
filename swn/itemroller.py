import logging
from python_log_indenter import IndentedLoggerAdapter
import sys
from random import random
from dice import roll
from dice.utilities import verbose_print as dice_print

FORMAT = "%(asctime)s - %(levelname)-8s - %(name)s - %(message)s"
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format=FORMAT)
log = IndentedLoggerAdapter(logging.getLogger(__name__))


class Item:
    def __init__(self, name: str, count: str = "1", chance: float = 1.0):
        self.name = name
        self.count = count
        self.chance = chance

        log.debug(f"New Item: {self}")

    def __str__(self):
        return f"Item[name=`{self.name}`; count={self.count}; chance={self.chance}]"

    def resolve(self):
        log.info(f"Resolving: {self}").push().add()

        curr_count = roll(self.count)
        curr_count.evaluate()

        if random() > self.chance:
            log.info(f"Failed chance to exist ({self.chance*100}%)")
        else:
            log.info(f"Passed chance to exist ({self.chance*100}%)")
            log.debug(f"Rolling Dice: {curr_count}")

            log.info(f"Count = {curr_count}").pop()

            return (curr_count, self.name)


class Table:
    def __init__(self, name: str, entries: list):
        self.name = name
        self.entries = []

        for number, thing in entries:
            self.entries = self.entries + [thing] * number

        log.debug(f"New Table: {self}")

    def __str__(self):
        return f"Table[name=`{self.name}`; size={len(self.entries)}]"

    def get(self, index):
        # clamp it into the range of the list
        index = max(0, min(index, len(self.entries) - 1))

        return self.entries[index]


class TableCall:
    def __init__(self, table: Table, num_rolls: int = 1, roll: str = "3d6", chance: float = 1.0):
        self.table_ref = table
        self.num_rolls = num_rolls
        self.roll = roll
        self.chance = chance

        log.debug(f"New TableCall: {self}")

    def __str__(self):
        return f"TableCall[table=`{self.table_ref.name}`; num_rolls={self.num_rolls}; roll={self.roll}; chance={self.chance}]"

    def resolve(self):
        log.info(f"Resolving: {self}").push().add()

        if random() > self.chance:
            log.info(f"Failed chance to exist ({self.chance*100}%)")
        else:
            log.info(f"Passed chance to exist ({self.chance*100}%)")

            return_list = []
            for i in range(self.num_rolls):
                curr_roll = roll(self.roll)
                curr_roll.evaluate()

                log.debug(f"Roll #{i+1} on {self.table_ref.name}: {curr_roll}")

                # get the entry from the table and resolve it
                log.add()
                return_list.append(self.table_ref.get(curr_roll).resolve())
                log.sub()

            log.pop()
            return return_list
