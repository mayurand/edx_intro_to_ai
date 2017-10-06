'''
Created on Feb 24, 2017

@author: Mayur Andulkar
'''

import resource
import sys

class outputDetails:
    def __init__(self):
        self.maxFringeSize = 0
        self.path = []
        self.fringeSize = 0
        self.searchDepth = 0
        self.maxSearchDepth = 0
        self.maxRamUsage = 0

def generic_search_modified(problem, fringe, add_to_fringe_fn):
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
            print 'Ram usage: '+str(ram_usage)
            outputVals.maxRamUsage = max(outputVals.maxRamUsage,ram_usage)
            # printPuzzle(node)
            print 'Fringe Size: '+str(sys.getsizeof(fringe))
            print 'closed Size in MB: '+str(int(sys.getsizeof(closed))/10**6)
            
            
            # raw_input("Press Enter to continue...")

            for child_node, child_action, child_cost in problem.getSuccessors(node):
                
                ## Check if the resulting child node has already been explored else add it to the fringe
                node_tuple = tuple([tuple(child_node.getTilePositions()[i]) for i in range(len(child_node.getTilePositions()))])
                if not node_tuple in closed:
                    new_cost = cost + child_cost
                    new_path = child_action
                    # Update search depth
                    outputVals.maxSearchDepth=max(outputVals.maxSearchDepth,len(new_path))
                    
                    new_state = (child_node, new_cost, new_path, node)
                    add_to_fringe_fn(fringe, new_state, new_cost)
