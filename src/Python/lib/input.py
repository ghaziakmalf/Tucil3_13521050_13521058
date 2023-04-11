import os

from lib.colors import *

def inputFile():
    """
    Read graph file (txt). Represented as adjacency matrix
    Input: -
    Output: Nodes name (array of string), adjacency matrix (matrix of integer)
    """

    while (True):
        # Read file
        print(LIGHT_GREEN + "\nInput format (example.txt). Put inside 'test' folder." + RESET)
        filename = input(WHITE + "Input Filename: " + RESET)

        try:
            # Check if filename is empty, raise error
            if (filename == ""):
                raise ValueError("Filename has not been filled!")
            
            # Check if file is txt, raise error
            if (filename[-4:] != ".txt"):
                raise ValueError("File must be in .txt format!")
            
            # Check if file exists, raise error
            if (not os.path.isfile("test/" + filename)):
                raise ValueError("File does not exist!")
            
            # Read first line (nodes name)
            file = open("test/" + filename, "r")
            nodesLine = file.readline()
            nodes = []

            # Insert nodes name into array
            for node in nodesLine.strip().split():
                nodes.append(str(node))

            # Check if nodes < 8, raise error
            if (len(nodes) < 8):
                raise ValueError("Number of nodes must be at least 8!")

            # Read the rest of the file (adjacency matrix)
            matrix = []
            for i in range(len(nodes)):
                line = file.readline()
                matrix.append(line.strip().split())

                # Check if matrix is not square (column), raise error
                if (len(matrix[i]) != len(nodes)):
                    raise ValueError("Adjacency matrix must be square!")
                
                # Check if matrix element is valid, raise error
                for j in range(len(nodes)):
                    try:
                        matrix[i][j] = int(matrix[i][j])
                    except ValueError:
                        raise ValueError("Adjacency matrix contains non-valid elements!")

            # Check if matrix is not square (row), raise error
            with open("test/" + filename, "r") as f:
                if (len(f.readlines())-1 != len(nodes)):
                    raise ValueError("Adjacency matrix must be square!")

            # Check if matrix is symmetric, raise error
            for i in range(len(nodes)):
                for j in range(len(nodes)):
                    if (matrix[i][j] != matrix[j][i]):
                        raise ValueError("Adjacency matrix must be symmetric!")

            # If pass all the checks, break the loop
            break

        # For print error message
        except ValueError as e:
            print(LIGHT_RED + "\n" + str(e) + " Please re-enter." + RESET)
            continue

    return nodes, matrix


def inputInteger(min, max):
    """
    For handling input integer. Check if input is integer and in range (from min to max)
    Input: min, max (integer)
    Output: val (integer)
    """

    while (True):
        val = input(WHITE + ">> " + RESET)
        try:
            # Check if input is empty, raise error
            if (val == ""):
                raise ValueError("Input has not been filled!")
            
            # Check if input is integer, raise error
            try:
                val = int(val)
            except ValueError:
                raise ValueError("Input is not an integer!")
            
            # Check if input is in range, break the loop
            if (val >= min and val <= max):
                break
            else:
                print(LIGHT_RED + "\nPlease enter a valid input! (" + str(min) + "-" + str(max) + ")" + RESET)

        # For print error message
        except ValueError as e:
            print(LIGHT_RED + "\n" + str(e) + " Please re-enter." + RESET)

    return val


def inputStartStop(nodes):
    """
    For handling input start and stop node
    Input: nodes (array of string)
    Output: start (string), stop (string)
    """

    # Print list of nodes
    print(WHITE + "\nList of nodes: " + RESET)
    for i in range(len(nodes)):
        print(LIGHT_RED + str(i+1) + ". " + WHITE + nodes[i] + RESET)

    while (True):
        try:
            # Read start and stop node and also check if start and stop node already inputted
            try:
                start, stop = input(WHITE + "Input start and stop nodes (e.g. A B): " + RESET).split()
            except ValueError:
                raise ValueError("Input must be 2 nodes!")
            
            # Check if start and stop node is in nodes array, raise error
            if (start not in nodes and stop not in nodes):
                raise ValueError("Start and stop node is not in the graph! Please re-enter.")
            
            # Check if start node is in nodes array, raise error
            elif (start not in nodes):
                raise ValueError("Start node is not in the graph! Please re-enter.")
            
            # Check if stop node is in nodes array, raise error
            elif (stop not in nodes):
                raise ValueError("Stop node is not in the graph! Please re-enter.")
            
            # If pass all the checks, break the loop
            else:
                break

        # For print error message
        except ValueError as e:
            print(LIGHT_RED + "\n" + str(e) + RESET)
            continue

    return start, stop