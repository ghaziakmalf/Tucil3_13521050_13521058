from lib.colors import *
from lib.splash import *
from lib.command import *
from lib.input import *
from lib.output import *
from lib.ucs import *
from lib.astar import *

def main():
    # Show splash screen
    splash()

    # Start program
    commandStart()
    process = inputInteger(2)

    # Loop until user exit
    while (process == 1):
        print("")
        commandInputOption()
        option = inputInteger(2)

        # Option 1: File input
        if (option == 1):
            nodes, matrix = inputFile()
            
            # Plot the graph
            plot("", nodes, matrix, [], None)

        # Option 2: Google Maps input
        else:
            print(LIGHT_RED + "\nSorry, this feature is not available yet." + RESET)

        # Get start and stop node
        start, stop = inputStartStop(nodes)

        # Pick algorithm
        print("")
        commandAlgorithm()
        algorithm = inputInteger(3)

        # Run Uniform Cost Search (UCS)
        if (algorithm == 1) or (algorithm == 3):
            # Start timer
            start_time = time.time()

            # Run UCS
            pathUCS, totalCostUCS, nCalcUCS = ucs(nodes, matrix, start, stop)

            # Stop timer
            timeElapsed = time.time() - start_time

            # Print result
            printResult("UNIFORM COST SEARCH", start, stop, nCalcUCS, pathUCS, totalCostUCS, timeElapsed)

            # Plot the graph
            plot("UNIFORM COST SEARCH", nodes, matrix, pathUCS, None)

        # Run A*
        if (algorithm == 2) or (algorithm == 3):
            # Start timer
            start_time = time.time()

            # Run A*
            pathAStar, totalCostAStar, nCalcAStar = astar(nodes, matrix, start, stop)

            # Stop timer
            timeElapsed = time.time() - start_time

            # Print result
            printResult("A*", start, stop, nCalcAStar, pathAStar, totalCostAStar, timeElapsed)

            # Plot the graph
            plot("A*", nodes, matrix, pathAStar, None)
        
        # Save option
        print("")
        commandSave()
        save = inputInteger(2)

        # Save to file
        if (save == 1):
            saveConfig = input(str(WHITE + "\nInput Filename: " + RESET))

            # Save Uniform Cost Search (UCS) result
            if (algorithm == 1) or (algorithm == 3):
                saveResult("UNIFORM COST SEARCH", start, stop, nCalcUCS, pathUCS, totalCostUCS, timeElapsed, nodes, matrix, saveConfig)
            
            # Save A* result
            if (algorithm == 2) or (algorithm == 3):
                saveResult("A*", start, stop, nCalcAStar, pathAStar, totalCostAStar, timeElapsed, nodes, matrix, saveConfig)
            
            # Display message file saved
            print(LIGHT_GREEN + "\nAdditional Information Added into txt File" + RESET)
            print(LIGHT_GREEN + "File saved!" + RESET)

        # Try again option, continue loop if yes
        print(LIGHT_GREEN + "\nDo you want to try again?\n" + RESET)
        commandStart()
        process = inputInteger(2)

    # Outside loop. Exit program
    print(LIGHT_GREEN + "\nThank you for using Shortest Path Solver!\n" + RESET)    

if __name__ == "__main__":
    main()