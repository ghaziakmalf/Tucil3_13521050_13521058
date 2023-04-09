from heapq import heappush, heappop

def ucs(nodes, matrix, start, stop):
    """
    Uniform Cost Search algorithm
    Input: nodes (array of string), matrix (2D array of integer), start (string), stop (string)
    Output: path (array of string), totalCost (integer), nCalc (integer)
    """

    # Create a dictionary to store the cost of each node
    costs = {node: float('inf') for node in nodes}
    costs[start] = 0

    # Create a dictionary to store the path to each node
    paths = {node: [] for node in nodes}
    paths[start] = [start]

    # Initialize variables
    queue = []
    heappush(queue, (0, start))
    nCalc = 0

    # Loop until queue is empty
    while queue:

        # Increment nCalc
        nCalc += 1

        # Pop the node with the lowest cost
        cost, current = heappop(queue)

        # If current node is the goal, break the loop
        if current == stop:
            break

        # Skip nodes that have already been visited
        if cost > costs[current]:
            continue

        # Loop through all the nodes
        for i in range(len(nodes)):

            # If there is a connection between current node and the other node
            if matrix[nodes.index(current)][i] != 0:

                # Calculate the cost to the neighbor through the current node
                new_cost = cost + matrix[nodes.index(current)][i]

                # If the new cost is lower than the current cost, update the cost and path
                if new_cost < costs[nodes[i]]:
                    costs[nodes[i]] = new_cost
                    paths[nodes[i]] = paths[current] + [nodes[i]]
                    heappush(queue, (new_cost, nodes[i]))

    # Extract the final path and total cost
    path = paths[stop]
    totalCost = sum(matrix[nodes.index(path[i])][nodes.index(path[i+1])] for i in range(len(path) - 1))

    return path, totalCost, nCalc