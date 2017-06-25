# -*- coding: utf-8 -*-

'''Solution to Knight's Tour Problem

Created for Chicago Tech Interviews meetup

Author: Aly Sivji
Date: June 25, 2017
'''

from collections import namedtuple

import networkx as nx
import matplotlib.pyplot as plt
import math

BOARDSIZE = 8
Square = namedtuple('Square', ['row', 'col'])


def rankfile_to_nodeid(row, col, boardsize=BOARDSIZE):
    return row * BOARDSIZE + col


def nodeid_to_rankfile(nodeid, boardsize=BOARDSIZE):
    row = math.floor(nodeid / boardsize)
    col = nodeid % boardsize

    assert row * BOARDSIZE + col == nodeid
    return Square(row, col)


def is_legal_pos(row, col, boardsize=BOARDSIZE):
    if 0 <= row < boardsize:
        if 0 <= col < boardsize:
            return True

    return False


def possible_moves(row, col, boardsize=BOARDSIZE):
    knight_moves = [(1, 2), (-1, 2), (1, -2), (-1, -2),
                    (2, 1), (-2, 1), (2, -1), (-2, -1)]

    moves = []
    for move in knight_moves:
        new_row = row + move[0]
        new_col = col + move[1]

        if is_legal_pos(new_row, new_col):
            moves.append(Square(new_row, new_col))

    return moves


# formulate problem
if __name__ == '__main__':
    # initialize list of node
    G = nx.DiGraph()
    G.add_nodes_from(range(BOARDSIZE**2))

    # build up graph of possible moves
    for row in range(BOARDSIZE):
        for col in range(BOARDSIZE):
            current_node = rankfile_to_nodeid(row, col)

            for move in possible_moves(row, col):
                possible_node = rankfile_to_nodeid(move.row, move.col)
                G.add_edge(current_node, possible_node)

    print(f'Number of nodes: {len(G)}')
    print(f'Number of edges: {len(G.edges())}')

    # use network x's Depth First Search to find solution
    solution = list(nx.dfs_edges(G))

    print(f'Number of nodes in solution: {len(solution)}')
    print(solution)
    # convert back to 2d representation
    print([(nodeid_to_rankfile(curr_square), nodeid_to_rankfile(next_square)) for curr_square, next_square in solution])
