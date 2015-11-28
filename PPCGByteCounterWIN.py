from pymclevel import TAG_Byte, TAG_Short, TAG_Int, TAG_Compound, TAG_List, TAG_String, TAG_Double, TAG_Float
import operator
displayName = "PPCG.SE Minecraft Byte Counter"

t1 = (1, 1, 5)
t2 = (2, 1, 10)
t3 = (0, 0, 3)
t4 = (1, 0, 3)

ids = {
    "RedstoneDust": 55,
    "RepeaterON": 94,
    "RepeaterOFF": 93,
    "ComparatorON": 150,
    "ComparatorOFF": 149,
    "StickyPiston": 29,
    "NormalPiston": 33,
    "ImpulseCommandBlock": 137,
    "RepeatCommandBlock": 210,
    "ChainCommandBlock": 211,
    "AirBlock": 0,
    "BarrierBlock": 166,
    "Lever": 69,
    "NoteBlock": 25,
    "StoneButton": 77,
    "WoodenButton": 143,
    "LampOFF": 123,
    "LampON": 124,
    "TorchOFF": 75,
    "TorchON": 76
}
count = {
    "RedstoneDust": 0,
    "Repeater": 0,
    "StickyPiston": 0,
    "NormalPiston": 0,
    "ImpulseCommandBlock": 0,
    "RepeatCommandBlock": 0,
    "ChainCommandBlock": 0,
    "AirBlock": 0,
    "BarrierBlock": 0,
    "Commands": 0,
    "MiscBlock": 0,
    "Entities": 0,
    "Levers": 0,
    "NoteBlock": 0,
    "Button": 0,
    "Lamp": 0,
    "Torch": 0
}
blockcount = {
    "RedstoneDust": 0,
    "Repeater": 0,
    "StickyPiston": 0,
    "NormalPiston": 0,
    "ImpulseCommandBlock": 0,
    "RepeatCommandBlock": 0,
    "ChainCommandBlock": 0,
    "AirBlock": 0,
    "BarrierBlock": 0,
    "Commands": 0,
    "MiscBlock": 0,
    "Entities": 0,
    "Levers": 0,
    "NoteBlock": 0,
    "Button": 0,
    "Lamp": 0,
    "Torch": 0
}

inputs = [
    (
        ("Redstone", "title"),
        ("Redstone Dust", t1),
        ("Redstone Repeater", t1),
        ("Redstone Comparator", t1),
        ("Piston", t2),
        ("Sticky Piston", t2),
        ("Lever", t1),
        ("Note Block", t1),
        ("Button", t1),
        ("Lamp", t1),
        ("Torch", t1)
    ),
    (
        ("Command Blocks", "title"),
        ("These values are preset for 1.9+", "label"),
        ("Impulse (Normal)", t2),
        ("Chain", t2),
        ("Repeat", t2)
    ),
    (
        ("Misc", "title"),
        ("Air Block", t3),
        ("Barrier Block", t4),
        ("Other Block", t4),
        ("Entity", t4),
        ("Bottom Layer is Floor", False)
    )
]

def perform(level, box, options):
    global inputs
    count = {
        "RedstoneDust": 0,
        "Repeater": 0,
        "StickyPiston": 0,
        "NormalPiston": 0,
        "ImpulseCommandBlock": 0,
        "RepeatCommandBlock": 0,
        "ChainCommandBlock": 0,
        "AirBlock": 0,
        "BarrierBlock": 0,
        "Commands": 0,
        "MiscBlock": 0,
        "Entities": 0,
        "Levers": 0,
        "NoteBlock": 0,
        "Button": 0,
        "Lamp": 0,
        "Torch": 0
    }
    blockcount = {
        "RedstoneDust": 0,
        "Repeater": 0,
        "StickyPiston": 0,
        "NormalPiston": 0,
        "ImpulseCommandBlock": 0,
        "RepeatCommandBlock": 0,
        "ChainCommandBlock": 0,
        "AirBlock": 0,
        "BarrierBlock": 0,
        "MiscBlock": 0,
        "Commands": 0,
        "Entities": 0,
        "Levers": 0,
        "NoteBlock": 0,
        "Button": 0,
        "Lamp": 0,
        "Torch": 0
    }
    bytecount = 0
    print("--------------------------------------------\nPPCG.SE Minecraft Program Size Counter\nby GamrCorps\n--------------------------------------------\n")
    for x in xrange(box.minx, box.maxx):
        for y in xrange(box.miny, box.maxy):
            for z in xrange(box.minz, box.maxz):
                if y == box.miny and options["Bottom Layer is Floor"] == True:
                    continue
                if level.blockAt(x,y,z) == ids["AirBlock"]:
                    bytecount += options["Air Block"]
                    count["AirBlock"] += options["Air Block"]
                    blockcount["AirBlock"] += 1
                elif level.blockAt(x,y,z) == ids["BarrierBlock"]:
                    bytecount += options["Barrier Block"]
                    count["BarrierBlock"] += options["Barrier Block"]
                    blockcount["BarrierBlock"] += 1
                elif level.blockAt(x,y,z) == ids["RedstoneDust"]:
                    bytecount += options["Redstone Dust"]
                    count["RedstoneDust"] += options["Redstone Dust"]
                    blockcount["RedstoneDust"] += 1
                elif level.blockAt(x,y,z) == ids["RepeaterON"]:
                    bytecount += options["Redstone Repeater"]
                    count["Repeater"] += options["Redstone Repeater"]
                    blockcount["Repeater"] += 1
                elif level.blockAt(x,y,z) == ids["RepeaterOFF"]:
                    bytecount += options["Redstone Repeater"]
                    count["Repeater"] += options["Redstone Repeater"]
                    blockcount["Repeater"] += 1
                elif level.blockAt(x,y,z) == ids["ComparatorON"]:
                    bytecount += options["Redstone Comparator"]
                    count["Comparator"] += options["Redstone Comparator"]
                    blockcount["Comparator"] += 1
                elif level.blockAt(x,y,z) == ids["ComparatorOFF"]:
                    bytecount += options["Redstone Comparator"]
                    count["Comparator"] += options["Redstone Comparator"]
                    blockcount["Comparator"] += 1
                elif level.blockAt(x,y,z) == ids["NormalPiston"]:
                    bytecount += options["Piston"]
                    count["NormalPiston"] += options["Piston"]
                    blockcount["NormalPiston"] += 1
                elif level.blockAt(x,y,z) == ids["StickyPiston"]:
                    bytecount += options["Sticky Piston"]
                    count["StickyPiston"] += options["Sticky Piston"]
                    blockcount["StickyPiston"] += 1
                elif level.blockAt(x,y,z) == ids["ImpulseCommandBlock"]:
                    bytecount += options["Impulse (Normal)"]
                    count["ImpulseCommandBlock"] += options["Impulse (Normal)"]
                    blockcount["ImpulseCommandBlock"] += 1
                elif level.blockAt(x,y,z) == ids["ChainCommandBlock"]:
                    bytecount += options["Chain"]
                    count["ChainCommandBlock"] += options["Chain"]
                    blockcount["ChainCommandBlock"] += 1
                elif level.blockAt(x,y,z) == ids["RepeatCommandBlock"]:
                    bytecount += options["Repeat"]
                    count["RepeatCommandBlock"] += options["Repeat"]
                    blockcount["RepeatCommandBlock"] += 1
                elif level.blockAt(x,y,z) == ids["Lever"]:
                    bytecount += options["Levers"]
                    count["Levers"] += options["Levers"]
                    blockcount["Levers"] += 1
                elif level.blockAt(x,y,z) == ids["NoteBlock"]:
                    bytecount += options["Note Block"]
                    count["NoteBlock"] += options["Note Block"]
                    blockcount["NoteBlock"] += 1
                elif level.blockAt(x,y,z) == ids["StoneButton"]:
                    bytecount += options["Button"]
                    count["Button"] += options["Button"]
                    blockcount["Button"] += 1
                elif level.blockAt(x,y,z) == ids["WoodenButton"]:
                    bytecount += options["Button"]
                    count["Button"] += options["Button"]
                    blockcount["Button"] += 1
                elif level.blockAt(x,y,z) == ids["LampON"]:
                    bytecount += options["Lamp"]
                    count["Lamp"] += options["Lamp"]
                    blockcount["Lamp"] += 1
                elif level.blockAt(x,y,z) == ids["LampOFF"]:
                    bytecount += options["Lamp"]
                    count["Lamp"] += options["Lamp"]
                    blockcount["Lamp"] += 1
                elif level.blockAt(x,y,z) == ids["TorchOFF"]:
                    bytecount += options["Torch"]
                    count["Torch"] += options["Torch"]
                    blockcount["Torch"] += 1
                elif level.blockAt(x,y,z) == ids["TorchON"]:
                    bytecount += options["Torch"]
                    count["Torch"] += options["Torch"]
                    blockcount["Torch"] += 1
                else:
                    bytecount += options["Other Block"]
                    count["MiscBlock"] += options["Other Block"]
                    blockcount["MiscBlock"] += 1
    for (chunk, slices, point) in level.getChunkSlices(box):
        for e in chunk.TileEntities:
            x = e["x"].value
            y = e["y"].value
            z = e["z"].value
            if (x, y, z) in box:
                if e["id"].value == "Control":
                    bytecount += len(e["Command"].value)
                    count["Commands"] += len(e["Command"].value)
                    blockcount["Commands"] += 1
        for e in chunk.Entities:
                x = e["Pos"][0].value
                y = e["Pos"][1].value
                z = e["Pos"][2].value
                if (x, y, z) in box:
                    bytecount += options["Entity"]
                    count["Entities"] += options["Entity"]
                    blockcount["Entities"] += 1
    for key, value in sorted(blockcount.items(), key=operator.itemgetter(1), reverse = True):
        print(key + ":\t" + str(value) + " (" + str(count[key]) + ")")
    print("\nTotal:" + str(bytecount) + "\n--------------------------------------------")
