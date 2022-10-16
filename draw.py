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
            ["q", "w", "f", "p", "b"],
            ["a", "r", "s", "t", "g"],
            ["z", "x", "c", "d", "v"],
        ],
        "right": [
            ["j", "l", "u", "y", "\" '"],
            ["m", "n", "e", "i", "o"],
            ["k", "h", "; ,", ": .", "? /"],
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
            ["", "shift tab", "up", "tab", ""],
            ["", "left", "down", "right", "enter"],
            ["swap lang", "æ", "ø", "å", ""],
        ],
        "thumbs": {"left": [green("nav"), ""], "right": ["del bspc", "num"],},
    },
    {    # num layer
        "left": [
            ["", "7", "8", "9", "vol up"],
            ["", "4", "5", "6", "vol dn"],
            ["", "1", "2", "3", "vol mute"],
        ],
        "right": [ # magnet shortcuts (window management)
            ["next", "left 2/3rd", "left half", "right half", "right 2/3rd"],
            ["play", "cmd", "shift", "alt", "ctrl"],
            ["prev", "left 3rd", "middle 3rd", "right 3rd", "full screen"],
        ],
        "thumbs": {"left": ["nav", "º 0"], "right": ["", green("num")],},
    },
    {   # sym layer
        "left": [
            ["%", "^", "$", "£ €", ""],
            ["/", "*", "-", "+", "\\"],
            ["|", "&amp;", "!", "=", ""],
        ],
        "right": [ # &#60; is < and &#62; is >
            ["", "{", "}", "@", "#"],
            ["", "(", ")", "&#60;", "&#62;"],
            ["``` ```", "[", "]", "~", "`"],
        ],
        "thumbs": {"left": [green("nav"), ""], "right": ["", green("num")],},
    }, 
    { # cross hand combo for reset
        "left": [
            ["", "", "", "", ""],
            ["", red("reset"), red("reset"), red("reset"), ""],
            ["", "", "", "", ""],
        ],
        "right": [
            ["", "", "", "", ""],
            ["", red("reset"), red("reset"), red("reset"), ""],
            ["", "", "", "", ""],
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
