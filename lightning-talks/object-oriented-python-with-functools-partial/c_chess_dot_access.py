from functools import partial
from types import SimpleNamespace

def Piece(type, color):
    _data = {
        "type": type,
        "color": color
    }
    return SimpleNamespace(**_data)


Pawn = partial(Piece, type="pawn")
Rook = partial(Piece, type="rook")
Knight = partial(Piece, type="knight")
Bishop = partial(Piece, type="bishop")
Queen = partial(Piece, type="queen")
King = partial(Piece, type="king")
