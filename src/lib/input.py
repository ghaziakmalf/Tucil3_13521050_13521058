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

    print("")
    while True:
        try:
            # Input number of nodes
            num_nodes = input(WHITE + "Enter the number of nodes (>=3): " + RESET)

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

                    # Check if node name already exist, raise error
                    if node_name in nodes:
                        print(LIGHT_RED + "\nNode name already exist! Please re-enter." + RESET)
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
                raise ValueError("Input is not in range!")
            
            # Check if start and stop node is the same, raise error
            if (start == stop):
                raise ValueError("Start and stop node must be different!")
            
            # If pass all the checks, break the loop
            else:
                break

        # For print error message
        except ValueError as e:
            print(LIGHT_RED + "\n" + str(e) + " Please re-enter." + RESET)
            continue

    return nodes[start], nodes[stop]


def inputMap(gmapsClient):
    """
    For handling input map
    Input: gmapsClient (googlemaps.Client)
    Output: locations_name (array of string), matrix (matrix of integer), coordinates (array of string)
    """

    print("")
    while True:
        try:
            # Input number of location
            num_locations = input(WHITE + "Enter the number of locations (>=3): " + RESET)

            # Check if input is empty, raise error
            if (num_locations == ""):
                raise ValueError("Input has not been filled!")
            
            # Check if input is integer, raise error
            try:
                num_locations = int(num_locations)
            except ValueError:
                raise ValueError("Input is not an integer!")

            # Check if number of location is less than 3, raise error
            if num_locations < 3:
                raise ValueError("Number of locations must be >=3!")
            
            print(LIGHT_GREEN + "\nInput a place, landmark, or address name. Recommended to put specific address or full name.")
            print("Example: Institut Teknologi Bandung, Gedung Sate, Jl.Cisitu" + RESET)

            # Array for storing location name, address, id, and coordinates
            locations_name = []
            locations_id = []
            address = []
            coordinates = []

            for i in range(num_locations):
                print("")
                while True:
                    # Input location name
                    location_name = input(f"{WHITE}Enter the name of location {i + 1}: {RESET}")
                    location = gmapsClient.geocode(address = location_name)

                    # Check if location is not found, raise error
                    if (not location):
                        print(LIGHT_RED + "\nLocation Not Found! Please re-enter." + RESET)
                        continue

                    # Check if input is empty, raise error
                    if (location_name == ""):
                        print(LIGHT_RED + "\nInput has not been filled! Please re-enter." + RESET)
                        continue

                    # Check if location name already exist, raise error
                    if location_name in locations_name:
                        print(LIGHT_RED + "\nLocation name already exist! Please re-enter." + RESET)
                        continue

                    # If pass all the checks, break the loop
                    break

                # Print location address
                print(LIGHT_GREEN + "\nObtained Location Address: " + RESET)
                print(WHITE + location[0]["formatted_address"] + RESET)

                # Insert location name, address, coordinates, and id to array
                address.append(location[0]["formatted_address"])
                coordinates.append(str(location[0]["geometry"]["location"]["lat"]) + "," +str(location[0]["geometry"]["location"]["lng"]))
                locations_name.append(location_name)
                locations_id.append(location[0]['place_id'])
            
            # If reach this point, break the loop
            break

        except ValueError as e:
            print(LIGHT_RED + "\n" + str(e) + " Please re-enter." + RESET)
            continue

    while (True):
        print("")
        while (True):
            try:
                # Input number of edge
                num_edge = input(WHITE + "Enter the number of edges: " + RESET)
            
                # Check if input is empty, raise error
                if (num_edge == ""):
                    raise ValueError("Input has not been filled!")
                
                # Check if input is integer, raise error
                try:
                    num_edge = int(num_edge)
                except ValueError:
                    raise ValueError("Input is not an integer!")
                
                # Check if number of edge is less than 1, raise error
                if num_edge < 1:
                    raise ValueError("Number of edges must be >=1!")
                
                # Check if number of edge is more than n(n-1)/2, raise error
                if (num_edge > (num_locations * (num_locations-1)/2)):
                    raise ValueError("Number of edges must be <= n(n-1)/2!")
                
                # If pass all the checks, break the loop
                break
                
            # For print error message
            except ValueError as e:
                print(LIGHT_RED + "\n" + str(e) + " Please re-enter." + RESET)
                continue

        # Print all location
        print(WHITE + "\nList of Locations" + RESET)
        for i in range(num_locations):
            print(f"{LIGHT_RED}{i+1}. {WHITE}{locations_name[i]} ({address[i]}) {RESET}")

        # Matrix for storing distance between locations
        matrix = [[0 for i in range (num_locations)] for j in range (num_locations)]

        for i in range(num_edge):
            while (True):
                try:
                    # Read location a and location b that wanted to be connected, and check if input is already filled
                    try:
                        location_a, location_b = input(WHITE + "Enter two locations to connect (e.g. 1 2): " + RESET).split()
                    except ValueError:
                        raise ValueError("Input has not been filled! Please re-enter.")
                    
                    # Check if input is integer, raise error
                    try:
                        location_a = int(location_a) - 1
                        location_b = int(location_b) - 1
                    except ValueError:
                        raise ValueError("Input is not an integer! Please re-enter.")
                    
                    # Check if input is in range, raise error
                    if (location_a < 0 or location_a >= len(locations_name) or location_b < 0 or location_b >= len(locations_name)):
                        raise ValueError("Input is not in range! Please re-enter.")
                    
                    # Check if input is already connected, raise error
                    if (matrix[location_a][location_b] != 0):
                        raise ValueError("Locations is already connected! Please re-enter.")
                    
                    # Check if location_a and location_b is the same, raise error
                    if (location_a == location_b):
                        raise ValueError("Locations is the same! Please re-enter.")
                    
                    # If pass all the checks, break the loop
                    break

                # For print error message
                except ValueError as e:
                    print(LIGHT_RED + "\n" + str(e) + RESET)
                    continue
            
            # Get distance between location_a and location_b
            distance = gmapsClient.directions(coordinates[location_a],coordinates[location_b])[0]['legs'][0]['distance']['value']

            # Insert distance to matrix
            matrix[location_a][location_b] = distance
            matrix[location_b][location_a] = distance
        
        break
    
    return locations_name, matrix, coordinates