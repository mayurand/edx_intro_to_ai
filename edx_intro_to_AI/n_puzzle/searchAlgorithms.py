'''
Created on Feb 10, 2017

@author: Mayur Andulkar
'''

from dataStructures import *
import resource

# from driver import printPuzzle

class outputDetails:
    def __init__(self):
        self.maxFringeSize = 0
        self.path = []
        self.fringeSize = 0
        self.searchDepth = 0
        self.maxSearchDepth = 0
        self.maxRamUsage = 0

def printPuzzle(currentState):
    for i in range(currentState.getGridSize()):
        row_ = '|'
        for j in range(currentState.getGridSize()):
            row_ = row_ +' ' + str(currentState.getTilePositions()[i][j])+' |'
        print row_
    print " "


def generic_search(problem, fringe, add_to_fringe_fn):
    closed = set()
    outputVals = outputDetails()
    start = (problem.getStartState(), 0, [])  # (node, cost, path)
    add_to_fringe_fn(fringe, start, 0)

    while not fringe.isEmpty():
        # print 'Fringe size: ',fringe.length()
        outputVals.maxFringeSize=max(outputVals.maxFringeSize,fringe.length())
        (node, cost, path) = fringe.pop()
        
        if problem.isGoalState(node):
            outputVals.path = path
            outputVals.fringeSize = fringe.length()
            outputVals.searchDepth = len(path)
            return outputVals
        
        
        node_tuple = tuple([tuple(node.getTilePositions()[i]) for i in range(len(node.getTilePositions()))])
        if not node_tuple in closed:
            closed.add(node_tuple)
            ram_usage = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
            outputVals.maxRamUsage = max(outputVals.maxRamUsage,ram_usage)
            # printPuzzle(node)
           
            # raw_input("Press Enter to continue...")

            for child_node, child_action, child_cost in problem.getSuccessors(node):
                
                ## Check if the resulting child node has already been explored else add it to the fringe
                node_tuple = tuple([tuple(child_node.getTilePositions()[i]) for i in range(len(child_node.getTilePositions()))])
                if not node_tuple in closed:
                    new_cost = cost + child_cost
                    new_path = path + [child_action]
                    # Update search depth
                    outputVals.maxSearchDepth=max(outputVals.maxSearchDepth,len(new_path))
                    new_state = (child_node, new_cost, new_path)
                    add_to_fringe_fn(fringe, new_state, new_cost)
                

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
    fringe = Stack()
    def add_to_fringe_fn(fringe, state, cost):
        fringe.push(state)

    return generic_search(problem, fringe, add_to_fringe_fn)



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = Queue()
    def add_to_fringe_fn(fringe, state, cost):
        fringe.push(state)

    return generic_search(problem, fringe, add_to_fringe_fn)



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe = PriorityQueue()
    def add_to_fringe_fn(fringe, state, cost):
        fringe.push(state, cost)

    return generic_search(problem, fringe, add_to_fringe_fn)



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = PriorityQueue()
    def add_to_fringe_fn(fringe, state, cost):
        new_cost = cost + heuristic(state[0], problem)
        fringe.push(state, new_cost)

    return generic_search(problem, fringe, add_to_fringe_fn)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch