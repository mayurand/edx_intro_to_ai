'''
Created on Feb 8, 2017

@author: Mayur Andulkar
gameState.py is used to define the game state as input in the driver.py
'''

import math
import copy


class Directions:
    UP = 'U'
    DOWN = 'D'
    RIGHT = 'R'
    LEFT = 'L'
    
    
class Actions:
    """
    A collection of static methods for manipulating move actions.
    """
    # Directions
    _directions = {Directions.UP: (-1, 0),
                   Directions.DOWN: (1, 0),
                   Directions.RIGHT:  (0, 1),
                   Directions.LEFT:  (0, -1)}

    # Directions
    _directionsBack = {'U': 'Up',
                   'D': 'Down',
                   'R': 'Right',
                   'L': 'Left'}
    
    _directionsAsList = _directions.items()
    
    
    _directPrecedence = {Directions.UP:4, 
                         Directions.DOWN:3, 
                         Directions.RIGHT:2, 
                         Directions.LEFT:1}

    def reverseDirection(action):
        if action == Directions.UP:
            return Directions.DOWN
        if action == Directions.DOWN:
            return Directions.UP
        if action == Directions.RIGHT:
            return Directions.LEFT
        if action == Directions.LEFT:
            return Directions.RIGHT
        
    reverseDirection = staticmethod(reverseDirection)

    def getPossibleActions(blankPos,gridSize):
        possible = []
        x_int, y_int = blankPos


        for dir_, vec in Actions._directionsAsList:
            dx, dy = vec
            next_y = y_int + dy
            next_x = x_int + dx

            if 0<=next_y<gridSize and 0<=next_x<gridSize:
                # possible.append(Actions.reverseDirection(dir_))
                # possible.append(([next_x,next_y],Actions.reverseDirection(dir_)))
                possible.append(([next_x,next_y],dir_))
        
        
        # Sort the successors in the precedence of Up, Down, Left, Right actions
        possible = sorted(possible, key=lambda x: Actions._directPrecedence[x[1]], reverse=True)
                
        return possible

    getPossibleActions = staticmethod(getPossibleActions)

    

class GameState(Actions):
    """
     The game state defines the full game state here where the state is defined
    by the positions of the tiles. Each tile
    """
    
    def __init__(self,prevState=None):
        """
        Generates a new state by copying information from its predecessor.
        """
        
        if prevState != None: # Copy previous state
            self.tilePositions = prevState.getTilePositions()
            self.blankPos = prevState.getBlankPos()
            self.gridSize = prevState.getGridSize()
    
        else: # No previous state. Do initializeGame after this
            self.tilePositions = []
            self.blankPos = [0][0]
            self.gridSize = 0

    def getBlankPos(self):
        return self.blankPos
    
    
    def getGridSize(self):
        return self.gridSize
    
    def getTilePositions(self):
        return self.tilePositions
    
        # for pos,direct_ in Actions.getPossibleActions(self.getBlankPos(),self.getGridSize()):
            #------------------------ print self.getTilePositions()[pos],direct_
    
    def initializeGame(self,initialGameState = [0,1,2,3,4,5,6,7,8]):
        self.gridSize = int(math.sqrt(len(initialGameState)))
        count = 0
        self.tilePositions = [[0 for _ in range(self.gridSize)] for _ in range(self.gridSize)] 
        
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.tilePositions[i][j]=initialGameState[count]
                if initialGameState[count]==0:
                    self.blankPos=[i,j]
                count += 1



    def generateSuccessor(self, pos=None, action=None):
        """
        Generates a new configuration reached by translating the current
        configuration by the action (UP,DOWN,LEFT,RIGHT).  This is a low-level call and does
        not attempt to respect the legality of the movement.
        Actions are movement vectors.
        """

        # Copy the existing state into a new one and
        # change the corresponding tiles according to the action
        newState = copy.deepcopy(GameState(self))

        # The current blank square is occupied by a new number
        new_pos=newState.getBlankPos()
        newState.getTilePositions()[new_pos[0]][new_pos[1]]=newState.getTilePositions()[pos[0]][pos[1]]

        # The new number position is now vacant
        newState.getTilePositions()[pos[0]][pos[1]] = 0
        newState.blankPos = [pos[0],pos[1]]

        return newState
    