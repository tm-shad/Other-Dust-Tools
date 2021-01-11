import logging
from random import random

from dice import roll
from dice.elements import Roll
from python_log_indenter import IndentedLoggerAdapter
import inflect
import re
from collections import Counter

from swntools.constants import DICE_REGEX

log = IndentedLoggerAdapter(logging.getLogger(__name__))


def get_roll(*args, **kwargs) -> int:
    i = roll(*args, **kwargs)

    if type(i) == Roll:
        return i[0]
    else:
        return i


def flatten(in_list):
    for el in in_list:
        if isinstance(el, list) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


class Item:
    def __init__(self, name: str, count: str = "1", chance: float = 1.0):
        self.name = name
        self.count = count
        self.chance = chance

        log.debug(f"New Item: {self!r}")

    def __str__(self):
        out = ""
        out += f"{self.count} " if self.count != "1" else ""
        out += f"{self.name}"
        out += f" [{self.chance*100}%]" if self.chance != 1.0 else ""
        return out

    def __repr__(self):
        return f"Item[name=`{self.name}`; count={self.count}; chance={self.chance}]"

    def resolve(self):
        log.info(f"{self}").push().add()

        curr_count = get_roll(self.count)

        if random() > self.chance:
            log.info(f"Failed chance to exist ({self.chance*100}%)")
            log.pop()
            return []
        else:
            if self.chance < 1:
                log.info(f"Passed chance to exist ({self.chance*100}%)")

            if self.count != "1":
                log.info(f"Rolling count: {self.count} -> {curr_count}")

            log.pop()
            return [(self.name, curr_count)]


class Table:
    def __init__(self, name: str, entries: list, default_dice: str = None):
        self.name = name
        self.entries = []
        self.default_dice = default_dice

        for number, thing in entries:
            self.entries = self.entries + [thing] * number

        log.debug(f"New Table: {self}")

    def __str__(self):
        return f"Table[name=`{self.name}`; size={len(self.entries)}]"

    def get(self, index):
        # clamp it into the range of the list
        index = max(0, min(index, len(self.entries) - 1))

        return self.entries[index]

    def print_table(self):
        for i, item in enumerate(self.entries):
            log.debug(f"{i+1:>3} | {item}")


class TableCall:
    def __init__(self, table: Table, num_rolls: str = "1", roll: str = None, chance: float = 1.0):
        self.table_ref = table
        self.num_rolls = str(num_rolls)

        if roll is None:
            if table.default_dice is not None:
                self.roll = table.default_dice
            else:
                raise ValueError(
                    "Missing argument 'roll', must either be passes as an argument or defined in the table's 'default_dice' parameter"
                )
        else:
            self.roll = roll

        self.chance = chance

        log.debug(f"New TableCall: {self!r}")

    def __str__(self):
        out = ""
        out += f"{self.num_rolls} " if self.num_rolls != "1" else ""
        out += f"{self.table_ref.name} ({self.roll})"
        out += f" [{self.chance*100}%]" if self.chance != 1.0 else ""
        return out

    def __repr__(self):
        return f"TableCall[table=`{self.table_ref.name}`; num_rolls={self.num_rolls}; roll={self.roll}; chance={self.chance}]"

    def resolve(self):
        log.info(f"{self}").push().add()

        if random() > self.chance:
            log.info(f"Failed chance to exist ({self.chance*100}%)")
            log.pop()
            return []
        else:
            if self.chance < 1:
                log.info(f"Passed chance to exist ({self.chance*100}%)")

            if type(self.num_rolls) == str:
                num_rolls = get_roll(self.num_rolls)
                if self.num_rolls != "1":
                    log.info(f"Getting the number of rolls: {self.num_rolls} -> {num_rolls}")
            else:
                num_rolls = self.num_rolls

            return_list = []
            for i in range(num_rolls):
                curr_roll = get_roll(self.roll)

                log.info(f"Roll {i+1} of {num_rolls}: {self.roll} -> {curr_roll}")

                # get the entry from the table and resolve it
                log.add()
                return_list.append(self.table_ref.get(curr_roll).resolve())
                log.sub()

            log.pop()
            return return_list


class Plunder:
    def __init__(self, rows: list):
        self.examples = dict()
        self.loot = dict()

        for id, example, loot in rows:
            log.debug(f"Adding Plunder Row: {id} [{example}] with {len(loot)} entries")
            self.examples[id] = example
            self.loot[id] = loot

    def resolve(self, id):
        log.info(f"Rolling for {id} (e.g. {self.examples[id]})").push().add()

        out = []
        for i in self.loot[id]:
            out += i.resolve()

        log.pop()
        return PlunderResult(list(flatten(out)), self.examples[id])


class PlunderResult:
    def __init__(self, res_list, name) -> None:
        self.res_list = res_list
        self.name = name
        self.roll_descriptions()
        self.res_list = Counter(dict(res_list))

    def __str__(self):
        p = inflect.engine()
        retstr = f"Loot from {p.a(self.name)}:\n"
        for i, (desc, count) in enumerate(self.res_list.most_common()):
            desc_split = desc.split(", ", maxsplit=1)
            retstr += f"\t{p.no(desc_split[0], count)}{', '+desc_split[1] if len(desc_split)==2 else ''}\n"

        return retstr

    def __repr__(self):
        pass
        return f"PlunderResult[size {len(self.res_list)}]"

    def roll_descriptions(self):
        log.info("Resolving all description rolls...").push().add()

        for i in range(len(self.res_list)):
            if re.search(DICE_REGEX, self.res_list[i][0]):
                clean_parts = [
                    str(get_roll(part)) if re.fullmatch(DICE_REGEX, part) else part
                    for part in re.split(f"({DICE_REGEX})", self.res_list[i][0])
                ]

                log.info(f"`{self.res_list[i][0]}` -> `{''.join(clean_parts)}`")
                self.res_list[i] = ("".join(clean_parts), self.res_list[i][1])

        log.pop()
