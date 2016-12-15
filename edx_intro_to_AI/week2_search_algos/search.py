# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from astropy.wcs.docstrings import NoSolution


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    ## Initialize frontier using the initial state of problem
    frontier = util.Stack()
    
    ## Any state is given as the state that you are into
    ## by taking some action. The state is defined by postion, action and direction
    frontier.push((problem.getStartState(),[],[]))
    
    while not frontier.isEmpty():

        ## Pop a node from the frontier and add the corresponding action
        ## The node and action_taken are initialized here
        node, action_taken, explored_set = frontier.pop()

        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in explored_set: # This is implementing graph search
                if problem.isGoalState(coord):
                    return action_taken + [direction]
                frontier.push((coord, action_taken + [direction], explored_set + [node] ))
                # print str(action_taken)+ "\n"

    return []
        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    ## Initialize frontier using the initial state of problem
    frontier = util.Queue()
    
    frontier.push((problem.getStartState(),[],[]))
 
    while not frontier.isEmpty():

        ## Pop a node from the frontier and add the corresponding action
        ## The node and action_taken are initialized here
        node, action_taken, explored_set = frontier.pop()
        
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in explored_set: # This is implementing graph search
                if problem.isGoalState(coord):
                    return action_taken + [direction]
                frontier.push((coord, action_taken + [direction], explored_set + [node] ))


    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    
    cost_of_actions = 0

    frontier.push((problem.getStartState(),[],[]),cost_of_actions)
 
    while not frontier.isEmpty():

        ## Pop a node from the frontier and add the corresponding action
        ## The node and action_taken are initialized here
        
        node, action_taken, explored_set = frontier.pop()
        
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in explored_set: # This is implementing graph search
                if problem.isGoalState(coord):
                    print(problem.getCostOfActions(action_taken + [direction]))
                    return action_taken + [direction]
                frontier.push((coord, action_taken + [direction], explored_set + [node]),problem.getCostOfActions(action_taken + [direction]))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
   # return manhattanDistance( xy1, xy2 )
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    
    total_cost = 0

    frontier.push((problem.getStartState(),[],[]),total_cost)
 
    while not frontier.isEmpty():

        ## Pop a node from the frontier and add the corresponding action
        ## The node and action_taken are initialized here
        
        node, action_taken, explored_set = frontier.pop()
        
        for coord, direction, steps in problem.getSuccessors(node):
            if not coord in explored_set: # This is implementing graph search
                if problem.isGoalState(coord):
                    return action_taken + [direction]
                total_cost = heuristic(coord, problem) +\
                 problem.getCostOfActions(action_taken + [direction])
                frontier.push((coord, action_taken + [direction], explored_set + [node]),total_cost)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
