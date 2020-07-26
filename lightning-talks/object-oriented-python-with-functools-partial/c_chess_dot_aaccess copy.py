from functools import partial
from types import SimpleNamespace

RANKS = [1, 2, 3, 4, 5, 6, 7, 8]
FILES = "abcdefgh"


def Piece(type, color):
    info = {
        "type": type,
        "color": color
    }
    return info


Pawn = partial(Piece, type="pawn")
Rook = partial(Piece, type="rook")
Knight = partial(Piece, type="knight")
Bishop = partial(Piece, type="bishop")
Queen = partial(Piece, type="queen")
King = partial(Piece, type="king")


# .keywords["type"] will get type


def _set_up_board():
    board = {}
    for file in FILES:
        for rank in RANKS:
            board[(file, rank)] = None

    board[("a", 1)] = Rook(color="white")
    board[("b", 1)] = Knight(color="white")
    board[("c", 1)] = Bishop(color="white")
    board[("d", 1)] = Queen(color="white")
    board[("e", 1)] = King(color="white")
    board[("f", 1)] = Bishop(color="white")
    board[("g", 1)] = Knight(color="white")
    board[("h", 1)] = Rook(color="white")

    for file in FILES:
        board[(file, 2)] = Pawn(color="white")

    board[("a", 8)] = Rook(color="black")
    board[("b", 8)] = Knight(color="black")
    board[("c", 8)] = Bishop(color="black")
    board[("d", 8)] = Queen(color="black")
    board[("e", 8)] = King(color="black")
    board[("f", 8)] = Bishop(color="black")
    board[("g", 8)] = Knight(color="black")
    board[("h", 8)] = Rook(color="black")

    for file in FILES:
        board[(file, 7)] = Pawn(color="black")

    return board


board = _set_up_board()

piece_lookup = {
    ("rook", "black"): "♜",
    ("knight", "black"): "♞",
    ("bishop", "black"): "♝",
    ("queen", "black"): "♛",
    ("king", "black"): "♚",
    ("pawn", "black"): "♟",
    ("rook", "white"): "♖",
    ("knight", "white"): "♘",
    ("bishop", "white"): "♗",
    ("queen", "white"): "♕",
    ("king", "white"): "♔",
    ("pawn", "white"): "♙",
}


def draw_board(board):
    output = ""
    for rank in reversed(RANKS):
        for file in FILES:
            piece = board[(file, rank)]
            if piece:
                piece_char = piece_lookup[(piece.type, piece.color)]
            else:
                piece_char = " "
            output += piece_char + " "
        output += "\n"
    print(output)
    return
