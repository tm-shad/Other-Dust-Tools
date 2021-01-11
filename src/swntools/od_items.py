from swntools.itemroller import Item, Plunder, Table, TableCall, log

tables = dict()


def RollPlunder(id):

    # T0 Tables: Energy Weapon
    name = "Energy Weapon"
    log.info(f"Creating {name} Table").push().add()
    tables[name] = Table(
        name,
        [
            (4, Item("Laser Pistol")),
            (3, Item("Laser Rifle")),
            (2, Item("Thermal Pistol")),
            (2, Item("Plasma Projector")),
            (2, Item("Shear Rifle")),
            (1, Item("Neutron Blaster")),
        ],
    )
    log.pop()

    # T0 Tables: Armor
    name = "Armor"
    log.info(f"Creating {name} Table").push().add()
    tables[name] = Table(
        name,
        [
            (2, Item("Nothing")),
            (2, Item("Shield")),
            (1, Item("Hide Armor")),
            (2, Item("Hide Armor/Shield")),
            (1, Item("Old Terran Clothing")),
            (1, Item("Old Terran Clothing/Shield")),
            (1, Item("Scrap Mail")),
            (2, Item("Scrap Mail/Shield")),
            (2, Item("Harmony Armor")),
            (1, Item("Harmony Armor/Shield")),
            (1, Item("Terran Explorer Suit")),
            (1, Item("Scrap Plate")),
            (1, Item("Scrap Plate/Shield")),
            (3, Item("Insurgent Combat Shell")),
            (2, Item("Powered Armor")),
            (2, Item("Executive Protection Field")),
            (1, Item("Storm Plate")),
        ],
    )
    log.pop()

    # T0 Tables: Weapon
    name = "Weapon"
    log.info(f"Creating {name} Table").push().add()
    tables[name] = Table(
        name,
        [
            (1, Item("Knife")),
            (1, Item("Club")),
            (2, Item("Spear")),
            (1, Item("Sword")),
            (1, Item("Axe")),
            (1, Item("Breachloading Rifle")),
            (1, Item("Spear")),
            (1, Item("Sword")),
            (2, Item("Revolver")),
            (1, Item("Semi-Auto Pistol")),
            (1, Item("Semi-Auto Rifle")),
            (1, Item("Shotgun")),
            (1, Item("Monoblade")),
            (1, Item("Submachine Gun")),
            (1, Item("Combat Rifle")),
            (1, Item("Monoblade")),
            (1, Item("Combat Rifle")),
            (1, Item("Combat Shotgun")),
            (1, Item("Huge Monoblade")),
            (1, Item("Combat Rifle")),
            (2, Item("Mag Pistol")),
            (2, Item("Mag Rifle")),
        ],
    )
    log.pop()

    log.pop()
    # T1 Tables: Rare Items
    name = "Rare Items"
    log.info(f"Creating {name} Table").push().add()
    tables[name] = Table(
        name,
        [
            (3, Item("+2 Blueprint, TL3")),
            (3, Item("+2 Blueprint, TL4")),
            (3, Item("+2 Blueprint, TL5")),
            (6, Item("+3 Blueprint, TL1d4+1")),
            (2, Item("+4 Blueprint, TL4")),
            (2, Item("+4 Blueprint, TL5")),
            (3, Item("Broadcast Power Mod")),
            (1, Item("Generator, Nanofusion")),
            (6, Item("Power Cell, B+")),
            (16, Item("TL4 Spare Part", "1d20")),
            (20, Item("TL5 Spare Part", "1d6")),
            (5, Item("Toolkit, TL5")),
            (1, Item("Rage stim", "1d10")),
            (2, Item("Purge stim", "1d10")),
            (3, Item("Microfac")),
            (1, Item("Portable Expert System")),
            (1, Item("Invasive Crosslink")),
            (2, Item("Neural Patterning Web")),
            (3, Item("Bot Override Tag")),
            (6, TableCall(tables["Weapon"], roll="1d10+16")),
            (6, TableCall(tables["Energy Weapon"], roll="1d6+8")),
            (5, TableCall(tables["Armor"], roll="1d8+18")),
        ],
        default_dice="1d100",
    )
    log.pop()

    # T1 Tables: Uncommon Items
    name = "Uncommon Items"
    log.info(f"Creating {name} Table").push().add()
    tables[name] = Table(
        name,
        [
            (5, Item("+1 Blueprint, TL 1d3+1")),
            (3, Item("Binocular, TL4")),
            (5, Item("Backpack, TL4")),
            (3, Item("Bedroll, TL4")),
            (3, Item("Compad")),
            (5, Item("Dataslab")),
            (2, Item("Geiger Counter")),
            (2, Item("Generator, Solar")),
            (8, Item("Stim", "2d4")),
            (2, Item("Link, Prosthetic")),
            (5, Item("Medkit")),
            (5, Item("Metatool")),
            (2, Item("Navcomp")),
            (5, Item("Power Cell, A+")),
            (5, Item("Power Cell, B")),
            (4, Item("Ration, Old Terran", "1d6")),
            (2, Item("Rope, 20m, TL4")),
            (2, Item("Solar Cell")),
            (5, Item("TL3 Spare Part", "1d6")),
            (5, Item("TL4 Spare Part", "1d6")),
            (2, Item("Tent, TL4")),
            (3, Item("Toolkit, TL3")),
            (4, Item("Toolkit, TL4")),
            (1, Item("Toxin Detector")),
            (1, Item("Vacc Suit, Pretech")),
            (3, TableCall(tables["Weapon"], roll="1d10+10")),
            (5, TableCall(tables["Energy Weapon"], roll="1d8")),
            (3, TableCall(tables["Rare Items"])),
        ],
        default_dice="1d100",
    )
    log.pop()

    # T1 Tables: Common Items
    name = "Common Items"
    log.info(f"Creating {name} Table").push().add()
    tables[name] = Table(
        name,
        [
            (5, Item("round of Ammunition", "20")),
            (5, Item("Backpack, TL1")),
            (5, Item("Bedroll, TL1")),
            (3, Item("Binocular, TL2")),
            (3, Item("Bonding Tape")),
            (2, Item("Climbing Kit")),
            (3, Item("Compass, Magnetic")),
            (5, Item("Crowbar")),
            (2, Item("Firebox")),
            (2, Item("Firestarter, TL1")),
            (4, Item("Grenade", "1d4")),
            (5, Item("Glowbug")),
            (3, Item("Lantern")),
            (3, Item("Oil Flask", "1d4")),
            (5, Item("Power Cell, Type A")),
            (3, Item("Ration, Dirty", "1d4")),
            (4, Item("Ration, Normal", "1d4")),
            (3, Item("Rope, 20m, TL1")),
            (5, Item("TL1 or 2 Spare Part", "1d6")),
            (5, Item("Stim", "1d6")),
            (2, Item("Tent, TL1")),
            (3, Item("Toolkit, TL1")),
            (4, Item("Toolkit, TL2")),
            (2, Item("Water Filter")),
            (2, Item("Thermal Flare")),
            (2, Item("Utility Tarp")),
            (5, TableCall(tables["Weapon"], roll="1d10+2")),
            (5, TableCall(tables["Uncommon Items"])),
        ],
        default_dice="1d100",
    )
    log.pop()

    # T2 Table: Random Loot
    name = "Random Loot"
    log.info(f"Creating {name} Table").push().add()
    tables[name] = Table(
        name,
        [
            (5, Item("Nothing")),
            (9, TableCall(tables["Common Items"])),
            (5, TableCall(tables["Common Items"], num_rolls=2)),
            (7, TableCall(tables["Uncommon Items"])),
            (3, TableCall(tables["Uncommon Items"], num_rolls=2)),
            (5, TableCall(tables["Rare Items"])),
            (1, TableCall(tables["Rare Items"], num_rolls=2)),
        ],
        default_dice="1d20",
    )
    log.pop()

    # # print the contents of all tables to DEBUG
    # for k, i in tables.items():
    #     log.debug(k + ":").push().add()
    #     i.print_table()
    #     log.pop()

    log.info("Creating Plunder Table").push().add()
    plunder = Plunder(
        [
            (
                "P1",
                "Impoverished Rabble",
                [
                    TableCall(tables["Weapon"], roll="1d6"),
                    TableCall(tables["Armor"], roll="1d6"),
                    Item("Ration, Normal", count="1", chance=0.5),
                    TableCall(tables["Random Loot"], chance=0.5),
                ],
            ),
            (
                "P2",
                "Raider/Tribal Warrior",
                [
                    TableCall(tables["Weapon"], roll="1d6+4"),
                    TableCall(tables["Armor"], roll="1d6+4"),
                    Item("Ration, Normal", count="1"),
                    TableCall(tables["Random Loot"], roll="1d20+3", chance=0.25),
                ],
            ),
            (
                "P3",
                "Elite Warrior",
                [
                    TableCall(tables["Weapon"], roll="1d6+6"),
                    TableCall(tables["Armor"], roll="1d6+6"),
                    Item("Ration, Normal", count="1d4"),
                    TableCall(tables["Random Loot"], roll="1d20+5", chance=0.5),
                ],
            ),
            (
                "P4",
                "Tribal Chieftain",
                [
                    TableCall(tables["Weapon"], roll="1d6+10"),
                    TableCall(tables["Armor"], roll="1d8+8"),
                    TableCall(tables["Random Loot"], roll="1d20+10"),
                ],
            ),
            (
                "P5",
                "TL3 Warrior/Raider",
                [
                    TableCall(tables["Weapon"], roll="1d6+12"),
                    TableCall(tables["Armor"], roll="1d6+1"),
                    TableCall(tables["Random Loot"], roll="1d20+5", chance=0.5),
                ],
            ),
            (
                "P6",
                "TL4 Common Citizen",
                [
                    Item("Laser Pistol"),
                    Item("Old Terran Clothing"),
                    TableCall(tables["Random Loot"], roll="1d20+5", chance=0.5),
                ],
            ),
            (
                "P7",
                "TL4 Gunman",
                [
                    TableCall(tables["Weapon"], roll="1d6+20"),
                    TableCall(tables["Armor"], roll="1d4+18"),
                    TableCall(tables["Random Loot"], roll="1d20+10", chance=0.5),
                ],
            ),
            (
                "P8",
                "TL4 Beamgunner",
                [
                    TableCall(tables["Energy Weapon"], roll="1d4+2"),
                    TableCall(tables["Armor"], roll="1d4+18"),
                    TableCall(tables["Random Loot"], roll="1d20+12", chance=0.5),
                ],
            ),
            (
                "P9",
                "TL4 Elite Soldier",
                [
                    TableCall(tables["Energy Weapon"], roll="1d6+6"),
                    TableCall(tables["Armor"], roll="1d6+18"),
                    TableCall(tables["Random Loot"], roll="1d20+12", chance=0.5),
                ],
            ),
            (
                "P10",
                "TL4 Champion",
                [
                    TableCall(tables["Energy Weapon"], roll="1d4+10"),
                    TableCall(tables["Armor"], roll="1d6+20"),
                    TableCall(tables["Random Loot"], roll="1d20+20"),
                ],
            ),
            (
                "G1",
                "Animal Nest",
                [
                    TableCall(tables["Weapon"], roll="1d10", chance=0.5),
                    TableCall(tables["Armor"], roll="1d10", chance=0.5),
                    TableCall(tables["Random Loot"], chance=0.5),
                ],
            ),
            (
                "G2",
                "Armory, Mandate",
                [
                    TableCall(tables["Energy Weapon"], num_rolls="1d6", roll="1d10+4"),
                    Item("Harmony Armor", count="1d6"),
                    TableCall(tables["Armor"], roll="1d8+18", chance=0.5),
                    Item("TL4 Spare Part", count="1d6"),
                    Item("TL5 Spare Part", count="1d6", chance=0.5),
                    Item("Power Cell, Type A", count="2d6"),
                ],
            ),
            (
                "G3",
                "Armory, Raider",
                [
                    TableCall(tables["Weapon"], num_rolls="1d6", roll="1d10+2"),
                    TableCall(tables["Weapon"], roll="1d6+9", chance=0.5),
                    TableCall(tables["Armor"], num_rolls="1d6", roll="1d10+3"),
                    Item("TL2 Spare Part", count="1d6"),
                    Item("Round of ammo", count="1d4*20"),
                ],
            ),
            (
                "G4",
                "Armory, Rebel",
                [
                    TableCall(tables["Weapon"], num_rolls="1d6", roll="1d10+10"),
                    TableCall(tables["Energy Weapon"], num_rolls="1d4", roll="1d8", chance=0.5),
                    Item("Insurgent Combat Shell", count="1d6"),
                    Item("TL3 Spare Part", count="1d6"),
                    Item("Round of ammo", count="1d6*20"),
                ],
            ),
            (
                "G5",
                "Camp, Small Raider",
                [
                    TableCall(tables["Weapon"], num_rolls="1d3", roll="1d10+2"),
                    TableCall(tables["Random Loot"], num_rolls="1d4", roll="1d20+3"),
                    TableCall(tables["Random Loot"], roll="1d20+10"),
                    Item("Round of ammo", count="20", chance=0.5),
                    Item("Power Cell, Type A", count="1d4", chance=0.5),
                ],
            ),
            (
                "G6",
                "Camp, Small Tribal",
                [
                    TableCall(tables["Weapon"], num_rolls="1d3", roll="1d10"),
                    TableCall(tables["Random Loot"], num_rolls="1d4", roll="1d20+3"),
                    TableCall(tables["Random Loot"], roll="1d20+5"),
                    Item("Round of ammo", count="20", chance=0.25),
                    Item("Power Cell, Type A", count="1d4", chance=0.25),
                ],
            ),
            (
                "G7",
                "Enclave Plunder, TL1",
                [
                    TableCall(tables["Weapon"], num_rolls="2d6", roll="1d10"),
                    TableCall(tables["Armor"], num_rolls="2d6", roll="1d8+2"),
                    TableCall(tables["Random Loot"], num_rolls="2d6"),
                    TableCall(tables["Random Loot"], num_rolls="1d6", roll="1d20+5"),
                    Item("Round of ammo", count="1d4*20"),
                    Item("Power Cell, Type A", count="1d4"),
                    TableCall(tables["Rare Items"], chance=0.1),
                    Item("Ration, Normal", count="1d10*10"),
                ],
            ),
            (
                "G8",
                "Enclave Plunder, TL2",
                [
                    TableCall(tables["Weapon"], num_rolls="2d6", roll="1d6+8"),
                    TableCall(tables["Armor"], num_rolls="2d6", roll="1d10+4"),
                    TableCall(tables["Random Loot"], num_rolls="3d6"),
                    TableCall(tables["Random Loot"], num_rolls="1d6", roll="1d20+10"),
                    Item("Round of ammo", count="3d6*20"),
                    Item("Power Cell, Type A", count="2d6"),
                    TableCall(tables["Rare Items"], chance=0.25),
                    Item("Ration, Normal", count="1d20*10"),
                ],
            ),
            (
                "G9",
                "Enclave Plunder, TL3",
                [
                    TableCall(tables["Weapon"], num_rolls="2d6", roll="1d6+8"),
                    TableCall(tables["Armor"], num_rolls="2d6", roll="1d10+4"),
                    TableCall(tables["Random Loot"], num_rolls="3d6"),
                    TableCall(tables["Random Loot"], num_rolls="1d6", roll="1d20+10"),
                    Item("Round of ammo", count="3d6*20"),
                    Item("Power Cell, Type A", count="2d6"),
                    TableCall(tables["Rare Items"], chance=0.25),
                    Item("Ration, Normal", count="1d10*20"),
                ],
            ),
            (
                "G10",
                "Enclave Plunder, TL4",
                [
                    TableCall(tables["Weapon"], num_rolls="2d6", roll="1d6+14"),
                    TableCall(tables["Armor"], num_rolls="2d6", roll="1d10+10"),
                    TableCall(tables["Random Loot"], num_rolls="3d6", roll="1d20+5"),
                    TableCall(tables["Random Loot"], num_rolls="1d6", roll="1d20+15"),
                    Item("Round of ammo", count="3d6*20"),
                    Item("Power Cell, Type A", count="2d6*5"),
                    TableCall(tables["Rare Items"], num_rolls="1d4"),
                    Item("Ration, Normal", count="2d20*20"),
                ],
            ),
            (
                "G11",
                "Medical Cache, Major",
                [
                    Item("Stim", count="1d10+10"),
                    Item("Medkit", count="1d4"),
                ],
            ),
            (
                "G12",
                "Medical Cache, Minor",
                [
                    Item("Stim", count="1d6"),
                    Item("Medkit", chance=0.5),
                ],
            ),
            (
                "G13",
                "Ruin, Large Structure",
                [
                    TableCall(tables["Random Loot"], num_rolls="5d6"),
                    TableCall(tables["Random Loot"], num_rolls="1d10", roll="1d20+10"),
                    TableCall(tables["Rare Items"], num_rolls="1d4-1"),
                    Item("TL4 Spare Part", count="2d6"),
                ],
            ),
            (
                "G14",
                "Ruin, Single Building",
                [
                    TableCall(tables["Random Loot"], num_rolls="3d6"),
                    TableCall(tables["Random Loot"], num_rolls="1d4", roll="1d20+10"),
                    TableCall(tables["Random Loot"], roll="1d20+20", chance=0.2),
                    Item("TL4 Spare Part", count="1d6"),
                ],
            ),
            (
                "G15",
                "Survival Cache, Enclave",
                [
                    Item("Ration, Old Terran", count="1d10"),
                    TableCall(tables["Random Loot"], num_rolls="1d6"),
                    Item("Round of ammo", count="1d4*20", chance=0.5),
                    Item("Power Cell, Type A", count="1d6", chance=0.5),
                ],
            ),
            (
                "G16",
                "Survival Cache, Ancient",
                [
                    Item("Ration, Old Terran", count="3d8"),
                    TableCall(tables["Uncommon Items"], num_rolls="1d6"),
                    Item("Power Cell, Type A", count="1d6+4"),
                ],
            ),
            (
                "G17",
                "Tech Cache, Major",
                [
                    Item("Spare Part of each TL from 3 to 5", count="1d10+10"),
                    TableCall(tables["Uncommon Items"], num_rolls="1d6"),
                    Item("Metatool", chance=0.5),
                    TableCall(tables["Rare Items"], chance=0.5),
                ],
            ),
            (
                "G18",
                "Tech Cache, Minor",
                [
                    Item("Spare Part of TL 1d4+1", count="1d10+10"),
                    TableCall(tables["Random Loot"], roll="1d20+10", chance=0.5),
                ],
            ),
            (
                "G19",
                "Trader Caravan",
                [
                    TableCall(tables["Weapon"], num_rolls="1d4", roll="1d6+9"),
                    TableCall(tables["Armor"], num_rolls="1d4", roll="1d10+4"),
                    Item("Round of ammo", count="1d6*20"),
                    Item("Power Cell, Type A", count="1d4"),
                    TableCall(tables["Random Loot"], num_rolls="2", roll="1d20+10", chance=0.5),
                    TableCall(tables["Rare Items"], chance=0.25),
                ],
            ),
            (
                "G20",
                "Workshop, Old Terran",
                [
                    Item("Toolkit, TL4", chance=0.75),
                    Item("Toolkit, TL5", chance=0.25),
                    Item("TL4 Spare Part", count="1d10+15"),
                    Item("TL5 Spare Part", count="1d8"),
                    TableCall(tables["Random Loot"], num_rolls="2", roll="1d20+15"),  # TODO: Note as broken
                ],
            ),
            (
                "G21",
                "Workshop, Scrounger",
                [
                    Item("Toolkit, TL2"),
                    Item("Toolkit, TL3", chance=0.75),
                    Item("Toolkit, TL4", chance=0.25),
                    Item("TL2 Spare Part", count="1d10+15"),
                    Item("TL3 Spare Part", count="1d10+5"),
                    Item("TL4 Spare Part", count="1d6"),
                    TableCall(tables["Random Loot"], num_rolls="2"),  # TODO: Note as broken
                ],
            ),
            (
                "TEST",
                "TEST PLUNDER",
                [
                    Item("Toolkit, TL 1d4"),
                ],
            ),
        ]
    )
    log.pop()

    return plunder.resolve(id)
