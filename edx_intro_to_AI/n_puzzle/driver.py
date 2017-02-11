'''
Created on Feb 8, 2017

@author: Mayur Andulkar

driver.py takes the input game state for nxn game puzzle.

The input is given as:

python driver.py bfs 3,1,2,0,4,5,6,7,8

    where bfs/dfs/ast/ida are the search algorithms to be used 
    and
    3,1,2,0,4,5,6,7,8 is the state of the game with 0 as null or blank tile 
'''

import sys
import re
import math
from gameState import GameState
from search import SearchAgent
from search import SearchProblem
# from search import SearchAgent

def printPuzzle(currentState):
    for i in range(currentState.getGridSize()):
        row_ = '|'
        for j in range(currentState.getGridSize()):
            row_ = row_ +' ' + str(currentState.getTilePositions()[i][j])+' |'
        print row_
    print " "
    
def runGame(searchAlgo, initialGameState):
    
    # Create a current state object and initialize it for given input
    currentState = GameState()
    currentState.initializeGame(initialGameState)
    printPuzzle(currentState) # To view whats going on

    # Send the initial state to the SearchAgent along with searchType
    searchType = SearchAgent(searchAlgo)
    searchType.registerInitialState(currentState)
    searchType.generateOutFile()
    # print 'Actions to be executed:', searchType.getActions()

    
def readCommand(argv):
    """
    Processes the command used to run game from the command line.
    """
    import argparse
    parser = argparse.ArgumentParser()
    
    """
    USAGE:      python driver.py <search> <initial game state>
    EXAMPLES:   (1) python driver.py bfs 4,1,2,3,0,5,6,7,8
    """
    parser.add_argument("searchAlgo", type=str, help="the search algorithm")
    parser.add_argument("gameState", type=str, \
                        help="the game state to be input as n*n or n^2 random numbers: 0,1,2,3,4,5,6,7,8")
    args = parser.parse_args(argv)
    args.gameState = map(int,re.findall('\d+', args.gameState))

    gridSize = math.sqrt(len(args.gameState))
    if gridSize.is_integer():
        print 'The grid is '+ str(int(gridSize))+' X '+str(int(gridSize))
        print ""
        return args
    else:
        raise Exception, 'Please enter a valid grid'
        sys.exit()
    

if __name__ == '__main__':
    """
    The main function called when pacman.py is run
    from the command line:
 
    > python driver.py
 
    See the usage string for more details.
 
    > python driver.py --help
    """
    args = readCommand( sys.argv[1:] ) # Get game components based on input

    runGame(args.searchAlgo, args.gameState)

    pass
