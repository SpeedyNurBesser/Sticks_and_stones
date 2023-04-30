
wood_types = ["cherry", "acacia", "jungle", "birch", "oak", "dark_oak", "spruce", "mangrove"]
nether_wood_types = ["warped", "crimson"]

input_item_types = [
    {
        "item": "stairs",
        "output": "3"
    },
    {
        "item": "slab",
        "output": "1"
    },
    {
        "item": "fence",
        "output": "3"
    },
    {
        "item": "fence_gate",
        "output": "8"
    },
    {
        "item": "door",
        "output": "4"
    },
    {
        "item": "trapdoor",
        "output": "6"
    },
    {
        "item": "pressure_plate",
        "output": "4"
    },
    {
        "item": "button",
        "output": "2"
    },
    {
        "item": "sign",
        "output": "4"
    },
    {
        "item": "planks",
        "output": "2"
    },
    {
        "item": "log",
        "output": "8"
    },
    {
        "item": "stripped_log",
        "output": "8"
    },
    {
        "item": "wood",
        "output": "8"
    },
    {
        "item": "stripped_wood",
        "output": "8"
    }
]
nether_input_item_types = [
    {
        "item": "stairs",
        "output": "3"
    },
    {
        "item": "slab",
        "output": "1"
    },
    {
        "item": "fence",
        "output": "3"
    },
    {
        "item": "fence_gate",
        "output": "8"
    },
    {
        "item": "door",
        "output": "4"
    },
    {
        "item": "trapdoor",
        "output": "6"
    },
    {
        "item": "pressure_plate",
        "output": "4"
    },
    {
        "item": "button",
        "output": "2"
    },
    {
        "item": "sign",
        "output": "4"
    },
    {
        "item": "planks",
        "output": "2"
    },
    {
        "item": "stem",
        "output": "8"
    },
    {
        "item": "stripped_stem",
        "output": "8"
    },
    {
        "item": "hyphae",
        "output": "8"
    },
    {
        "item": "stripped_hyphae",
        "output": "8"
    }
]
bamboo_input_item_types = [
    {
        "item": "block",
        "output": "4"
    },
    {
        "item": "stripped_block",
        "output": "4"
    },
    {
        "item": "planks",
        "output": "2"
    },
    {
        "item": "mosaic",
        "output": "2"
    },
    {
        "item": "stairs",
        "output": "3"
    },
    {
        "item": "mosaic_stairs",
        "output": "3"
    },
    {
        "item": "slab",
        "output": "1"
    },
    {
        "item": "mosaic_slab",
        "output": "1"
    },
    {
        "item": "fence",
        "output": "3"
    },
    {
        "item": "fence_gate",
        "output": "8"
    },
    {
        "item": "trapdoor",
        "output": "6"
    },
    {
        "item": "door",
        "output": "4"
    },
    {
        "item": "pressure_plate",
        "output": "4"
    },
    {
        "item": "button",
        "output": "2"
    },
    {
        "item": "sign",
        "output": "4"
    }
]

for x in wood_types:
    for i in input_item_types:
        f = open(x + "_" + i["item"] + ".json", "w")
        f.write('{"type": "minecraft:stonecutting","ingredient": {"item": "minecraft:'+ x + "_" + i["item"] +'"},"result": "minecraft:stick","count":' + i["output"] + '}')

for x in nether_wood_types:
    for i in nether_input_item_types:
        f = open(x + "_" + i["item"] + ".json", "w")
        f.write('{"type": "minecraft:stonecutting","ingredient": {"item": "minecraft:'+ x + "_" + i["item"] +'"},"result": "minecraft:stick","count":' + i["output"] + '}')

for i in bamboo_input_item_types:
    f = open("bamboo_" + i["item"] + ".json", "w")
    f.write('{"type": "minecraft:stonecutting","ingredient": {"item": "minecraft:' + "bamboo" + "_" + i[
        "item"] + '"},"result": "minecraft:stick","count":' + i["output"] + '}')