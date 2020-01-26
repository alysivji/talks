# Knight's Tour Problem

## Background

**Graphs** (Networks) are a useful data structure that can be used to model complex relational problems

**Nodes** (vertices) - things we are intersted in

**Edges** (links between nodes) - model the relationships between the things we are interested in

---

## Problem

The Knight's Tour is a sequence of moves that a knight can make on a chessboard to visit every square only once.

Animation from [Wikipedia](https://en.wikipedia.org/wiki/Knight%27s_tour):

<img src="images/knights_tour_from_wikipedia.gif" />

---

## Things We Know

* Chess boards are 8x8
* Knights move in L shape:
  * 2 squares sideways, 1 up/down
  * 2 squares up/down + 1 sideways
* More moves in center of board vs sides
  * Have function to ensure move we make is legal

---

## Thinking in Graphs

* Use integer [0 to 63] to represent each square instead of rank & file
  * Represent 2D structure as 1D structure
    * Create function to convert
* Each square on the board can be represented as node
* Moves the knight makes between squares can be represented as edges
    * Each edge represents move from A to B (i.e. Directed Graph)

---

## Solution in Python

> *Python ~= Pseudocode*

Check out [solutions.py](solution.py)

---

## Aside: Depth First Search (DFS)

* Builds search tree by exploring one branch of tree as deeply as possible
* [Wikpedia Article: Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)