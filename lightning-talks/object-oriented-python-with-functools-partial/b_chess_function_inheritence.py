from functools import partial


def Piece(type, color):
    _data = {
        "type": type,
        "color": color
    }
    return _data

Queen = partial(Piece, type="queen")

# .keywords["type"] will get type
>>> piece = Queen(color="black")
>>> piece["type"]
>>> piece["color"]
>>> piece
