from itemroller import Table, Item, TableCall, log

tables = dict()

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
        (3, Item("+2 Blueprints, TL3")),
        (3, Item("+2 Blueprints, TL4")),
        (3, Item("+2 Blueprints, TL5")),
        (6, Item("+3 Blueprint, TL1d4+1")),
        (2, Item("+4 Blueprint, TL4")),
        (2, Item("+4 Blueprint, TL5")),
        (3, Item("Broadcast Power Mod")),
        (1, Item("Generator, Nanofusion")),
        (6, Item("Power Cell, B+")),
        (16, Item("TL4 Spare Parts", "1d20")),
        (20, Item("TL5 Spare Parts", "1d6")),
        (5, Item("Toolkit, TL5")),
        (1, Item("Rage stims", "1d10")),
        (2, Item("Purge stims", "1d10")),
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
        (5, Item("+1 Blueprints, TL 1d3+1")),
        (3, Item("Binoculars, TL4")),
        (5, Item("Backpack, TL4")),
        (3, Item("Bedroll, TL4")),
        (3, Item("Compad")),
        (5, Item("Dataslab")),
        (2, Item("Geiger Counter")),
        (2, Item("Generator, Solar")),
        (8, Item("Stims", "2d4")),
        (2, Item("Link, Prosthetic")),
        (5, Item("Medkit")),
        (5, Item("Metatool")),
        (2, Item("Navcomp")),
        (5, Item("Power Cell, A+")),
        (5, Item("Power Cell, B")),
        (4, Item("Rations, Old Terran", "1d6")),
        (2, Item("Rope, 20m, TL4")),
        (2, Item("Solar Cell")),
        (5, Item("TL3 Spare Parts", "1d6")),
        (5, Item("TL4 Spare Parts", "1d6")),
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
        (5, Item("rounds of Ammunition", "20")),
        (5, Item("Backpack, TL1")),
        (5, Item("Bedroll, TL1")),
        (3, Item("Binoculars, TL2")),
        (3, Item("Bonding Tape")),
        (2, Item("Climbing Kit")),
        (3, Item("Compass, Magnetic")),
        (5, Item("Crowbar")),
        (2, Item("Firebox")),
        (2, Item("Firestarter, TL1")),
        (4, Item("Grenades", "1d4")),
        (5, Item("Glowbug")),
        (3, Item("Lantern")),
        (3, Item("Oil Flasks", "1d4")),
        (5, Item("Power Cell, Type A")),
        (3, Item("Rations, Dirty", "1d4")),
        (4, Item("Rations, Normal", "1d4")),
        (3, Item("Rope, 20m, TL1")),
        (5, Item("TL1 or 2 Spare Parts", "1d6")),
        (5, Item("Stims", "1d6")),
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

# print the contents of all tables to DEBUG
for k, i in tables.items():
    log.debug(k + ":").push().add()
    i.print_table()
    log.pop()


print(tables["Common Items"].get(40).resolve())
