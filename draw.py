KEY_W = 55
KEY_H = 45
KEY_RX = 6
KEY_RY = 6
INNER_PAD_W = 2
INNER_PAD_H = 2
OUTER_PAD_W = KEY_W / 2
OUTER_PAD_H = KEY_H / 2
LINE_SPACING = 18

STYLE = """
    svg {
        font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
        font-size: 14px;
        font-kerning: normal;
        text-rendering: optimizeLegibility;
        fill: #24292e;
    }

    rect {
        fill: #f6f8fa;
    }

    .green {
        fill: #fdd;
    }

    .green {
        fill: #dfd;
    }

    .purple {
        fill: #ddf;
    }

    .yellow {
        fill: #ffd;
    }

    .blue {
        fill: #dff;
    }

    .pink {
        fill: #fdf;
    }

    .grey {
        fill: #ddd;
    }

    .red {
        fill: #fdd;
    }

    .none {
        fill: #fff;
        fill-opacity: 0.0;
    }
"""

def green(key):
    return {"key": key, "class": "green"}

def purple(key):
    return {"key": key, "class": "purple"}

def yellow(key):
    return {"key": key, "class": "yellow"}

def blue(key):
    return {"key": key, "class": "blue"}

def pink(key):
    return {"key": key, "class": "pink"}

def grey(key):
    return {"key": key, "class": "grey"}

def red(key):
    return {"key": key, "class": "red"}

def none(): # no text, transparent key
    return {"key": "", "class": "none"}

KEYMAP = [
    {   # base layer
        "left": [
            ["j", "w", "h", "p", "b"],
            ["c", "s", "n", "t", "g"],
            ["\" '", "f", "l", "d", "v"],
        ],
        "right": [
            ["? /", "m", "u", "a", "# @"],
            ["! -", "r", "e", "o", "i"],
            ["~ `", "k", "; ,", ": .", "y"],
        ],
        "thumbs": {"left": ["nav", "_ space"], "right": ["shift", "num"],},
    },
    {   # nav layer
        "left": [
            ["esc", "back", "fwd", "swap win", "screen shot"],
            ["ctrl", "alt", "shift", "cmd", "search"],
            ["undo", "cut", "copy", "paste", "lock"],
        ],
        "right": [
            ["page up", "shift tab", "up", "tab", ""],
            ["page down", "left", "down", "right", ""],
            ["swap lang", "home", "enter", "end", ""],
        ],
        "thumbs": {"left": [red("nav"), ""], "right": ["del bspc", "num"],},
    },
    {    # num layer
        "left": [
            ["", "7", "8", "9", ""],
            ["", "4", "5", "6", ""],
            ["", "1", "2", "3", ""],
        ],
        "right": [
            ["", "", "", "", ""],
            ["", "cmd", "shift", "alt", "ctrl"],
            ["", "", "", "", ""],
        ],
        "thumbs": {"left": ["nav", "º 0"], "right": ["", red("num")],},
    },
    {   # sym layer
        "left": [
            ["%", "^", "$", "£ €", ""],
            ["/", "*", "-", "+", "\\"],
            ["|", "&amp;", "!", "=", ""],
        ],
        "right": [ # magnet shortcuts (window management)
            ["", "left 2/3rd", "left half", "right half", "right 2/3rd"],
            ["", "cmd", "shift", "alt", "ctrl"],
            ["", "left 3rd", "middle 3rd", "right 3rd", "full screen"],
        ],
        "thumbs": {"left": [red("nav"), ""], "right": ["", red("num")],},
    },
    {   # combos, outer horizontal
        "left": [ # &#60; is <
            [green("esc"), green("esc"), blue("{"), blue("{"), ""],
            [purple("&#60;"), purple("&#60;"), pink("("), pink("("), ""],
            [yellow(""), yellow(""), grey("["), grey("["), ""],
        ],
        "right": [ # &#62; is >
            ["", blue("}"), blue("}"), green(""), green("")],
            ["", pink(")"), pink(")"), purple("&#62;"), purple("&#62;")],
            ["", grey("]"), grey("]"), yellow(""), yellow("")],
        ],
        "thumbs": {"left": ["", ""],"right": ["", ""],},
    },
    {   # combos, inner horizontal
        "left": [
            ["", green("Q"), green("Q"), blue("vol up"), blue("vol up")],
            ["", purple("X"), purple("X"), pink("vol down"), pink("vol down")],
            ["", yellow("Z"), yellow("Z"), grey("mute"), grey("mute")],
        ],
        "right": [
            [blue("next"), blue("next"), green("Æ"), green("Æ"), ""],
            [pink("play"), pink("play"), purple("Å"), purple("Å"), ""],
            [grey("prev"), grey("prev"), yellow("Ø"), yellow("Ø"), ""],
        ],
        "thumbs": {"left": ["", ""],"right": ["", ""],},
    },
    { # cross hand combos for bluetooth stuff on ZMK
        "left": [
            ["", pink("reset"), pink("reset"), pink("reset"), blue("boot load")],
            ["", green("bt 0"), green("bt 0"), green("bt 0"), purple("bt 1")],
            ["", yellow("bt clear"), yellow("bt clear"), yellow("bt clear"), grey("out tggl")],
        ],
        "right": [
            [pink("reset"), blue("boot load"), blue("boot load"), blue("boot load"), ""],
            [green("bt 0"), purple("bt 1"), purple("bt 1"), purple("bt 1"), ""],
            [yellow("bt clear"), grey("out tggl"), grey("out tggl"), grey("out tggl"), ""],
        ],
        "thumbs": {"left": ["", ""],"right": ["", ""],},
    },
]

KEYSPACE_W = KEY_W + 2 * INNER_PAD_W
KEYSPACE_H = KEY_H + 2 * INNER_PAD_H
HAND_W = 5 * KEYSPACE_W
HAND_H = 4 * KEYSPACE_H
LAYER_W = 2 * HAND_W + OUTER_PAD_W
LAYER_H = HAND_H
BOARD_W = LAYER_W + 2 * OUTER_PAD_W
BOARD_H = len(KEYMAP) * LAYER_H + (len(KEYMAP) + 1) * OUTER_PAD_H


def print_key(x, y, key):
    key_class = ""
    if type(key) is dict:
        key_class = key["class"]
        key = key["key"]
    print(
        f'<rect rx="{KEY_RX}" ry="{KEY_RY}" x="{x + INNER_PAD_W}" y="{y + INNER_PAD_H}" width="{KEY_W}" height="{KEY_H}" class="{key_class}" />'
    )
    words = key.split()
    y += (KEYSPACE_H - (len(words) - 1) * LINE_SPACING) / 2
    for word in key.split():
        print(
            f'<text text-anchor="middle" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{y}">{word}</text>'
        )
        y += LINE_SPACING


def print_row(x, y, row):
    for key in row:
        print_key(x, y, key)
        x += KEYSPACE_W


def print_block(x, y, block):
    for row in block:
        print_row(x, y, row)
        y += KEYSPACE_H


def print_layer(x, y, layer):
    print_block(x, y, layer["left"])
    print_block(
        x + HAND_W + OUTER_PAD_W, y, layer["right"],
    )
    print_row(
        x + 3 * KEYSPACE_W, y + 3 * KEYSPACE_H, layer["thumbs"]["left"],
    )
    print_row(
        x + HAND_W + OUTER_PAD_W, y + 3 * KEYSPACE_H, layer["thumbs"]["right"],
    )


def print_board(x, y, keymap):
    x += OUTER_PAD_W
    for layer in keymap:
        y += OUTER_PAD_H
        print_layer(x, y, layer)
        y += LAYER_H


print(
    f'<svg width="{BOARD_W}" height="{BOARD_H}" viewBox="0 0 {BOARD_W} {BOARD_H}" xmlns="http://www.w3.org/2000/svg">'
)
print(f"<style>{STYLE}</style>")
print_board(0, 0, KEYMAP)
print("</svg>")
