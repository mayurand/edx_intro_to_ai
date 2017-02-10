"""
Created on Feb 8, 2017

@author: Mayur Andulkar

The search Agents are implemented here.

The state of the game is taken and solved for action sequence 
being visited as UDLR or Up, Down,Left,Right
"""

import time
from gameState import Actions
import searchAlgorithms




class SearchAgent():
    """
    This very general search agent finds a path using a supplied search
    algorithm for a supplied search problem, then returns actions to follow that
    path.
    """

    def __init__(self, fn='dfs', heuristic='nullHeuristic'): 
        
        func = getattr(searchAlgorithms, fn)
        if 'heuristic' not in func.func_code.co_varnames:
            print('Search Algorithm being used:' + fn)
            self.searchFunction = func
        
        else:
            if heuristic in dir(searchAlgorithms):
                heur = getattr(searchAlgorithms, heuristic)
            else:
                raise AttributeError, heuristic + ' is not a function in searchAgents.py or search.py.'
            print('[SearchAgent] using function %s and heuristic %s' % (fn, heuristic))
            # Note: this bit of Python trickery combines the search algorithm and the heuristic
            self.searchFunction = lambda x: func(x, heuristic=heur)

    def registerInitialState(self, state):
        """
        state: a GameState object (driver.py)
        """
        if self.searchFunction == None: raise Exception, "No search function provided for SearchAgent"
        starttime = time.time()
        problem = SearchProblem(state) # Makes a new search problem
        self.actions  = self.searchFunction(problem) # Find a path
        totalCost = problem.getCostOfActions(self.actions)
        print('Path found with total cost of %d in %.1f seconds' % (totalCost, time.time() - starttime))
        if '_expanded' in dir(problem): print('Search nodes expanded: %d' % problem._expanded)

    def getActions(self):
        """
        Returns all actions else None
        """
        return self.actions

class SearchProblem(Actions):
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.

    The state space consists of (x,y) positions in a pacman game.

    Note: this search problem is fully specified; you should NOT change it.
    """
    def __init__(self, gameState, cost= 1, start=None, warn=True, visualize=True):
        """
        Stores the start and goal.

        gameState: A GameState object (pacman.py)
        costFn: In this case 1
        goal: A position in the gameState
        """
        self.startState = gameState
        self.cost = cost
        self._expanded = 0


    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        current = 0
        for row in range(state.getGridSize()):
            for col in range(state.getGridSize()):
                if current != state.getTilePositions()[row][col]:
                    return False
                current += 1
        return True

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """
        successors = []
        
        
        for position, direct_ in state.getPossibleActions(state.getBlankPos(),state.getGridSize()):
            nextState = state.generateSuccessor(position,direct_)
            cost = self.cost
            successors.append((nextState, direct_, cost))

        self._expanded =+1
        
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions. If those actions
        include an illegal move, return 999999.
        """
        if actions == None: return 999999
        cost = 0
        for action in actions:
            cost += 1
        return cost