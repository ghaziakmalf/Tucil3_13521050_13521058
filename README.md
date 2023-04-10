# Finding the Closest Path between Two Nodes with _UCS (Uniform Cost Search)_ and _A* (A-star)_ Algorithm

## Table of Contents
- [Finding the Closest Path between Two Nodes with _UCS (Uniform Cost Search)_ and _A\* (A-star)_ Algorithm](#finding-the-closest-path-between-two-nodes-with-ucs-uniform-cost-search-and-a-a-star-algorithm)
  - [Table of Contents](#table-of-contents)
  - [Program Description](#program-description)
  - [Algorithm](#algorithm)
    - [UCS (Uniform Cost Search)](#ucs-uniform-cost-search)
    - [A\* (A-star)](#a-a-star)
  - [Requirements](#requirements)
  - [Libraries](#libraries)
  - [Program Structure](#program-structure)
  - [How To Run](#how-to-run)
  - [Author](#author)

## Program Description
In this project, the authors were tasked to develop a program to find the closest path between two nodes. Each node is connected by a line that has weight. The weight of the line is the distance between the two points. This weight is represented by adjacency matrix. The program will look for the shortest path from the starting point to the destination point using the UCS and A* algorithms. The program will display the path found and its weight. The program will also display the total cost, number of calculations, execution time, and system platform to find the path.

## Algorithm
This project uses 2 algorithms, [UCS (Uniform Cost Search)](https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/) and [A* (A-star)](https://www.geeksforgeeks.org/a-search-algorithm/). UCS (Uniform Cost Search) and A* (A-star) are both algorithms used in computer science and artificial intelligence to search for paths in graphs or trees.

### UCS (Uniform Cost Search)
UCS is a graph search algorithm that finds the shortest path from a starting node to a goal node by considering the cost of each path. It explores the graph by expanding the node with the lowest cumulative cost (i.e., the path with the smallest total cost) at each step. It maintains a priority queue (often implemented using a heap data structure) to keep track of the nodes to be expanded, with the node with the lowest cost being expanded first. UCS continues to expand nodes and update the costs until the goal node is reached or all reachable nodes have been explored.

### A* (A-star)
A* is a heuristic search algorithm that is an extension of UCS. Like UCS, it uses a priority queue to explore nodes, but it also incorporates an additional heuristic function that estimates the cost from the current node to the goal node. A* combines the cost of the path from the start node to the current node (g-cost) with the estimated cost from the current node to the goal node (h-cost) to determine the priority of nodes in the priority queue. A* selects the node with the lowest f-cost (g-cost + h-cost) for expansion. This heuristic function helps A* to efficiently explore the most promising paths towards the goal node, making it more informed and often faster than UCS in finding the shortest path.

In summary, UCS is a graph search algorithm that finds the shortest path based on the cumulative cost of the path, while A* is an extension of UCS that uses a heuristic function to estimate the cost to the goal node, making it more efficient in finding the shortest path in many cases.

## Requirements
- Python (tested version 3.11.0)
- Install all libraries used below

## Libraries
- os
- heapq
- platform
- matplotlib
- networkx
- time

## Program Structure
```
.
├── doc/
│   ├── Tucil3_K2_13521050_13521058.pdf
│   └── Tucil3-Stima-2023.pdf
├── src/
│   ├── Javascript/
│   └── Python/
│       ├── lib/
│       │   ├── astar.py
│       │   ├── colors.py
│       │   ├── command.py
│       │   ├── input.py
│       │   ├── output.py
│       │   ├── splash.py
│       │   └── ucs.py
|       └── main.py
├── test/
│   ├── testInput/
│   ├── testOutput/
│   └── graph.txt
├── .gitignore
├── README.md
├── RunnerPy.bat
└── RunnerPython.bat
```

## How To Run
To run the program in the terminal _root directory_, run the command __RunnerPy.bat__ or __RunnerPython.bat__ (on windows). The runner used depends on the latest version of python on the PC (you can check using 'py --version' and 'python --version'), because on some PCs there is a difference between using py and python.
```
./RunnerPy.bat

or

./RunnerPython.bat

or

double click the runner you want to use
```
The program can also be run by directly compiling _main.py_ with the following command.
```
py src/Python/main.py

or

python src/Python/main.py
```
However, it is better to run the program using _Runner_ because it will automatically delete __pycache__ when exiting the program.

## Author
- 13521050 - Naufal Syifa Firdaus
- 13521058 - Ghazi Akmal Fauzan