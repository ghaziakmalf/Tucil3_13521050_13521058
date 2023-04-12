import os
import networkx as nx
import matplotlib.pyplot as plt
import platform

from lib.colors import *

def plot (title, nodes, matrix, path, saveConfig):
    """
    Plot graph using networkx
    Input: title, nodes, matrix, path, saveConfig
    Output: Show plot. If saveConfig is not None, save plot
    """

    # Clear plot
    plt.clf()

    # Create weighted graph
    G = nx.Graph()
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if (matrix[i][j] != 0):
                G.add_edge(nodes[i], nodes[j], weight=matrix[i][j])

    # Compute node positions using spring layout algorithm
    pos = nx.spring_layout(G)

    # Draw graph with node positions from spring layout, show labels in bold, set font size for node labels
    nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=7)

    # Get edge labels from 'weight' attribute of graph G
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Draw edge labels on graph G with bold font, set font size for edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold', font_size=7)

    # Compute edge colors based on whether edge is in graph G or not
    edge_colors = ['b' if (path[i], path[i+1]) in nx.edges(G) else 'k' for i in range(len(path)-1)]

    # Draw edges on graph G with specified edge list, color, and width 
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='r', width=4)

    # Draw edges on graph G with edge colors based on edge_colors list
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)

    # Set title, set font size for title
    plt.suptitle(title, fontsize=10)

    # Show or save plot
    if saveConfig is None:
        plt.show()
    else:
        plt.savefig(saveConfig)


def printResult(algorithm, start, stop, nCalc, path, totalCost, time):
    """
    Print result of algorithm
    Input: algorithm, start, stop, nCalc, path, totalCost, time
    Output: Print result
    """

    if (algorithm == "UNIFORM COST SEARCH"):
        print(WHITE + "\n=============== " + LIGHT_RED + "UNIFORM COST SEARCH" + WHITE + " ===============")
    else:
        print(WHITE + "\n======================= " + LIGHT_RED + "A*" + WHITE + " ========================")
    print(WHITE + "Start node: " + YELLOW + str(start))
    print(WHITE + "Stop node: " + YELLOW + str(stop))
    print(WHITE + "Shortest path: " + YELLOW + " -> ".join(str(p) for p in path))
    print(WHITE + "Total cost: " + YELLOW + str(totalCost))
    print(WHITE + "Number of calculations: " + YELLOW + str(nCalc))
    print(WHITE + "Execution time: " + YELLOW + "{:.2f} ms".format(time * 1000))
    print(WHITE + "Processor: " + YELLOW + str(platform.processor()) + RESET)


def saveResult(algorithm, start, stop, nCalc, path, totalCost, time, nodes, matrix, saveConfig, mapImage, option):
    """
    Save result of algorithm
    Input: algorithm, start, stop, nCalc, path, totalCost, time, nodes, matrix, saveConfig
    Output: Save result
    """

    # Create folder if not exist
    if not os.path.exists("test"):
        os.mkdir("test")
    if not os.path.exists("test/" + saveConfig):
        os.mkdir("test/" + saveConfig)

    if algorithm == "A*":
        f = open("test/" + saveConfig + "/" + saveConfig + "AStar.txt", "w")

        # save image
        if(option == 2):
            mapImage.save("test/" + saveConfig + "/" + saveConfig + "MapAStar.png")

        # Save plot
        plot(algorithm, nodes, matrix, path, "test/" + saveConfig + "/" + saveConfig + "AStar.png")
    else:
        f = open("test/" + saveConfig + "/" + saveConfig + "UCS.txt", "w")

        # save image
        if(option == 2):
            mapImage.save("test/" + saveConfig + "/" + saveConfig + "MapUCS.png")

        # Save plot
        plot(algorithm, nodes, matrix, path, "test/" + saveConfig + "/" + saveConfig + "UCS.png")

    # Save nodes
    f.write("Nodes:\n")
    for i in range(len(nodes)):
        f.write(str(nodes[i]) + "\n")
    f.write("\n")

    # Save matrix
    f.write("Matrix:\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            f.write(str(matrix[i][j]) + " ")
        f.write("\n")

    # Save weight for each connected node
    f.write("\nWeight for each node:\n")
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if (matrix[i][j] != 0):
                f.write(str(nodes[i]) + " <-> " + str(nodes[j]) + " = " + str(matrix[i][j]) + "\n")
    
    # Save result
    if (algorithm == "UNIFORM COST SEARCH"):
        f.write("\n=============== " + "UNIFORM COST SEARCH" + " ===============\n")
    else:
        f.write("\n======================= " + "A*" + " ========================\n")
    f.write("Start node: " + str(start) + "\n")
    f.write("Stop node: " + str(stop) + "\n")
    f.write("Shortest path: " + " -> ".join(str(p) for p in path) + "\n")
    f.write("Total cost: " + str(totalCost) + "\n")
    f.write("Number of calculations: " + str(nCalc) + "\n")
    f.write("Execution time: " + "{:.2f} ms".format(time * 1000) + "\n")
    f.write("Processor: " + str(platform.processor()))

def addPathUrl(matrix, coordinates, url, gmapsClient):
    pathurl = url
    
    # find relation
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            if(i != j and i < j and matrix[i][j]):
                enc = gmapsClient.directions(coordinates[i],coordinates[j])[0]["overview_polyline"]["points"]
                pathurl += f"&path=color:blue%7Cenc:{enc}"
                
    return pathurl

def addShortestPathUrl(coordinates, url, gmapsClient, path):
    pathurl = url

    for i in range(len(path)-1):
        enc = gmapsClient.directions(coordinates[path[i]],coordinates[path[i+1]])[0]["overview_polyline"]["points"]
        pathurl += f"&path=color:0xff0000ff%7Cenc:{enc}"
    
    return pathurl

def convertPathToInt(path, nodes):

    intPath = []

    for el in path:
        intPath.append(nodes.index(el))

    return intPath