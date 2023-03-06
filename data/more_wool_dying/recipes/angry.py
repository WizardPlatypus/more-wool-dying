from sys import argv

# this used to be __template = ..., but didn't work, so now we have a function
def get_template():
    return """{
    "type": "crafting_shaped",
    "pattern": [
        "###",
        "#O#",
        "###"
    ],
    "key": {
        "#": [
            {WOOL}
        ],
        "O": {
            "item": "minecraft:{COLOR}_dye"
        }
    },
    "result": {
        "item": "minecraft:{COLOR}_wool",
        "count": 8
    },
    "group": "more_wool_dying"
}"""

__wool = {
    "brown": '{"item": "minecraft:brown_wool"}',
    "red": '{"item": "minecraft:red_wool"}',
    "orange": '{"item": "minecraft:orange_wool"}',
    "yellow": '{"item": "minecraft:yellow_wool"}',
    "lime": '{"item": "minecraft:lime_wool"}',
    "green": '{"item": "minecraft:green_wool"}',
    "cyan": '{"item": "minecraft:cyan_wool"}',
    "light_blue": '{"item": "minecraft:light_blue_wool"}',
    "blue": '{"item": "minecraft:blue_wool"}',
    "purple": '{"item": "minecraft:purple_wool"}',
    "magenta": '{"item": "minecraft:magenta_wool"}',
    "pink": '{"item": "minecraft:pink_wool"}',
    "white": '{"item": "minecraft:white_wool"}',
    "light_gray": '{"item": "minecraft:light_gray_wool"}',
    "gray": '{"item": "minecraft:gray_wool"}',
    "black": '{"item": "minecraft:black_wool"}',
}

__colors = [
    "brown",
    "red",
    "orange",
    "yellow",
    "lime",
    "green",
    "cyan",
    "light_blue",
    "blue",
    "purple",
    "magenta",
    "pink",
    "white",
    "light_gray",
    "gray",
    "black"
]

def fill_template(color_id):
    _color = __colors[color_id]
    # no reason to redye wool into it's own color, so
    # such recipe should be excluded
    _wool = ""
    sep = ',\n            '
    for other in __colors:
        if other == _color:
            continue
        _wool += __wool[other] + sep
    _wool = _wool[:len(_wool) - len(sep)]

    template = get_template()

    # this does not work, sadge[
    # print(template.format(WOOL=_wool, COLOR=_color))
    # soo gonna do this instead
    template = template.replace("{WOOL}", _wool)
    template = template.replace("{COLOR}", _color)

    return template

def main():
    color_id = (int(argv[1]) % len(__colors)) if len(argv) > 1 else 0
    print(fill_template(color_id))


if __name__ == "__main__":
    main()