from heapq import heappush, heappop

def heuristic(nodes, matrix, start, stop):
    """
    Heuristic function
    Input: nodes (array of string), matrix (2D array of integer), start (string), stop (string)
    Output: h (array of integer)
    """
    h = {}  # Using a dictionary for faster lookups
    for node in nodes:
        h[node] = matrix[nodes.index(start)][nodes.index(node)] + matrix[nodes.index(node)][nodes.index(stop)]
    return h


def astar(nodes, matrix, start, stop):
    """
    A* algorithm
    Input: nodes (array of string), matrix (2D array of integer), start (string), stop (string)
    Output: path (array of string), totalCost (integer), nCalc (integer)
    """

    # Initialize variables
    path = []
    visited = set()
    queue = []
    cost = 0
    h = heuristic(nodes, matrix, start, stop)
    heappush(queue, (cost + h[start], cost, start, [start]))
    nCalc = 0

    # Loop until queue is empty
    while queue:

        # Increment nCalc
        nCalc += 1

        # Pop the node with the lowest f value
        f, cost, current, path = heappop(queue)

        # If current node is the goal, break the loop
        if current == stop:
            break

        # If current node is not visited, add it to visited
        if current not in visited:
            visited.add(current)

            # Loop through all the nodes
            for i in range(len(nodes)):

                # If there is a connection between current node and the other node
                if matrix[nodes.index(current)][i] != 0:

                    # Calculate the new g value
                    new_cost = cost + matrix[nodes.index(current)][i]

                    # Calculate the new f value using the heuristic
                    new_f = new_cost + h[nodes[i]]

                    # Append the new node to queue
                    heappush(queue, (new_f, new_cost, nodes[i], path + [nodes[i]]))

    # Calculate total cost
    totalCost = 0
    for i in range(len(path) - 1):
        totalCost += matrix[nodes.index(path[i])][nodes.index(path[i + 1])]

    return path, totalCost, nCalc