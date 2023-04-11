from heapq import heappush, heappop

def heuristic(nodes, matrix, current, goal):
    """
    Manhattan distance heuristic
    Input: nodes (array of string), matrix (2D array of integer), current (string), goal (string)
    Output: h (dictionary)
    """

    # Initialize the heuristic dictionary with initial values as infinity for all nodes
    h = {node: float('inf') for node in nodes}

    # Set the heuristic value for the current node to 0
    h[current] = 0

    # Get the index of the goal node
    goal_idx = nodes.index(goal)

    # Get the coordinates of the goal node
    goal_x, goal_y = goal_idx // 3, goal_idx % 3

    # Loop through all the nodes
    for node in nodes:

        # Get the index and coordinates of the current node
        node_idx = nodes.index(node)
        node_x, node_y = node_idx // 3, node_idx % 3

        # Calculate the Manhattan distance from current node to goal node
        h[node] = abs(node_x - goal_x) + abs(node_y - goal_y)

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

                    # Update the heuristic value for the next iteration
                    if nodes[i] not in h or new_f < h[nodes[i]]:
                        h[nodes[i]] = new_f

                    # Append the new node to queue
                    heappush(queue, (new_f, new_cost, nodes[i], path + [nodes[i]]))

    # Calculate total cost
    totalCost = 0
    for i in range(len(path) - 1):
        totalCost += matrix[nodes.index(path[i])][nodes.index(path[i + 1])]

    return path, totalCost, nCalc