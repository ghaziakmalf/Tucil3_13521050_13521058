import os
import googlemaps

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

            # Insert nodes name into array and check if nodes name is valid
            try:
                for node in nodesLine.strip().split():
                    nodes.append(str(node))
            except ValueError:
                raise ValueError("Nodes name must be alphabet!")

            # Check if nodes < 8, raise error
            if (len(nodes) < 8):
                raise ValueError("Number of nodes must be at least 8!")
            
            # Check duplicate node name, raise error
            if (len(nodes) != len(set(nodes))):
                raise ValueError("Node name must be unique!")

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


def inputManual():
    """
    Input manual from user. Ask for how many nodes (>=3), nodes name, and weight for each nodes
    Input: -
    Output: Nodes name (array of string), adjacency matrix (matrix of integer)
    """
    while True:
        try:
            # Input number of nodes
            num_nodes = input(WHITE + "\nEnter the number of nodes (>=3): " + RESET)

            # Check if input is empty, raise error
            if (num_nodes == ""):
                raise ValueError("Input has not been filled!")
            
            # Check if input is integer, raise error
            try:
                num_nodes = int(num_nodes)
            except ValueError:
                raise ValueError("Input is not an integer!")

            # Check if number of nodes is less than 3, raise error
            if num_nodes < 3:
                raise ValueError("Number of nodes must be >=3!")

            # Input nodes name
            nodes = []
            print("")
            for i in range(num_nodes):
                while True:
                    node_name = input(f"{WHITE}Enter the name of node {i + 1}: {RESET}")

                    # Check if input is empty, raise error
                    if (node_name == ""):
                        print(LIGHT_RED + "\nInput has not been filled! Please re-enter." + RESET)
                        continue

                    # Check if node name is already exist, raise error
                    if node_name in nodes:
                        print(LIGHT_RED + "\nNode name is already exist! Please re-enter." + RESET)
                        continue

                    # If pass all the checks, break the loop
                    break

                nodes.append(node_name)

            # Input upper triangle matrix
            matrix = []
            print("")
            for i in range(num_nodes):
                matrix.append([0] * i)
                for j in range(i, num_nodes):
                    if i == j:
                        matrix[i].append(0)
                    else:
                        while True:
                            weight = input(f"{WHITE}Enter the weight of edge between {nodes[i]} and {nodes[j]}: {RESET}")

                            # Check if input is empty, raise error
                            if (weight == ""):
                                print(LIGHT_RED + "\nInput has not been filled! Please re-enter." + RESET)
                                continue

                            # Check if input is integer, raise error
                            try:
                                weight = int(weight)
                            except ValueError:
                                print(LIGHT_RED + "\nInput is not an integer! Please re-enter." + RESET)
                                continue

                            # Check if weight is less than 0, raise error
                            if weight < 0:
                                print(LIGHT_RED + "\nWeight must be >=0! Please re-enter." + RESET)
                                continue

                            # If pass all the checks, break the loop
                            break
                        
                        matrix[i].append(weight)        

            # Copy the upper triangle to lower triangle to make adjacency matrix
            for i in range(num_nodes):
                for j in range(num_nodes):
                    matrix[j][i] = matrix[i][j]

            # Check if matrix is symmetric, raise error
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if matrix[i][j] != matrix[j][i]:
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
            # Read start and stop node and check if input is already filled
            try:
                start, stop = input(WHITE + "Input start and stop nodes (e.g. 1 2): " + RESET).split()
            except ValueError:
                raise ValueError("Input has not been filled!")
            
            # Check if input is integer, raise error
            try:
                start = int(start) - 1
                stop = int(stop) - 1
            except ValueError:
                raise ValueError("Input is not an integer!")
            
            # Check if input is in range, raise error
            if (start < 0 or start >= len(nodes) or stop < 0 or stop >= len(nodes)):
                raise ValueError("Input is not in range! Please re-enter.")

            # Check if start and stop node is in nodes array, raise error
            if (nodes[start] not in nodes and nodes[stop] not in nodes):
                raise ValueError("Start and stop node is not in the graph! Please re-enter.")
            
            # Check if start node is in nodes array, raise error
            elif (nodes[start] not in nodes):
                raise ValueError("Start node is not in the graph! Please re-enter.")
            
            # Check if stop node is in nodes array, raise error
            elif (nodes[stop] not in nodes):
                raise ValueError("Stop node is not in the graph! Please re-enter.")
            
            # If pass all the checks, break the loop
            else:
                break

        # For print error message
        except ValueError as e:
            print(LIGHT_RED + "\n" + str(e) + RESET)
            continue

    return nodes[start], nodes[stop]


def inputMap(gmapsClient):

    print("Input a place, landmark, or address. Recommended to put spesific address or full name of a landmark")
    print("landmark: Empire State Building, Insitut Teknologi Bandung, or Gedung Sate")
    print("address: Jl.Cisitu, Dago, Coblong, Bandung Kidul (Complete Address)\n")

    n = int(input("How many place (node)? "))

    places_name = []
    address = []
    places_id = []
    coordinates = []
    matrix = [[0 for i in range (n)] for j in range (n)]
    i = 0

    # Input all nodes
    for i in range(n):
        while(True):
            address_input = input("\nInsert location: ")
            location = gmapsClient.geocode(address = address_input)
            if location:
                break
            else:
                print("Location Not Found")

        print("\nObtained Location Address: ")
        print(location[0]["formatted_address"])
        address.append(location[0]["formatted_address"])
        coordinates.append(str(location[0]["geometry"]["location"]["lat"]) + "," +str(location[0]["geometry"]["location"]["lng"]))
        places_name.append(address_input)
        places_id.append(location[0]['place_id'])


    # PRINT ALL NODE
    print("List of Place")
    for i in range(n):
        print(f"{i+1}. {places_name[i]} ({address[i]})")

    # INPUT ROUTE
    n = int(input("How many route (edge)? "))
    for i in range(n):
        while(True):
            a, b = input("Input two place index to connect (e.g. 1 5) ").split()
            a = int(a) 
            b = int(b) 

            if((a > 0 and a <= len(places_id) and b <= len(places_id) and b > 0) and a != b):
                distance = gmapsClient.distance_matrix(f"place_id:{places_id[a-1]}", f"place_id:{places_id[b-1]}")["rows"][0]["elements"][0]['distance']['value']
                matrix[a-1][b-1] = distance
                matrix[b-1][a-1] = distance
                break
            else:
                print("Input tidak dalam range")
    
    return places_name, places_id, matrix, coordinates
