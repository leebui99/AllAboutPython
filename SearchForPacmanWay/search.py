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
from StdSuites.QuickDraw_Graphics_Suite import graphic_group


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import game

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

def graphSearch(problem, dataStructure):
    
    startState = problem.getStartState()
    print "Start:", startState
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    dS = dataStructure #calling data structure from util.py
    visitedState = set([startState])
    startNode = (startState, [])
    dS.push(startNode)
      
    while True:
        if dS.isEmpty():
            return[]
            
        state, gamePath = dS.pop()
        #print "state", state
        #print "path", gamePath
        
        successors = problem.getSuccessors(state)
        
        for successor in successors:
            listPath = list(gamePath)
            #print "listPath: ", listPath
           
            if successor[0] not in visitedState:
                visitedState.add(successor[0])
                action(problem, listPath, successor[1])
                dS.push((successor[0],listPath))   
        
        if problem.isGoalState(state):
            print "Final path to reach the goal: ", gamePath
            return gamePath
           
    return []

def action(problem, path, move):
    
    direction = game.Directions()
    north = direction.NORTH
    south = direction.SOUTH
    east = direction.EAST
    west = direction.WEST
    
    if move == 'North':
        path.append(north)
    elif move == 'South':
        path.append(south)
    elif move == 'East':
        path.append(east)
    elif move == 'West':
        path.append(west)
    
    return path


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
    "*** YOUR CODE HERE ***"  
    return graphSearch(problem, util.Stack())

    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return graphSearch(problem, util.Queue())

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    startState = problem.getStartState()
    print "Start:", startState
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    dS = util.PriorityQueue()
    dS.push((startState,[],0), 0)
    visitedState = set([startState])
    
    while True:
        
        if dS.isEmpty():
            return[]
        
        state, path, cost = dS.pop()
        
        if problem.isGoalState(state):
            return path
        
        successors = problem.getSuccessors(state)
        
        for successor in successors:
            totalCost = cost + successor[2]
            gamePath = list(path)
            if successor[0] not in visitedState:
                visitedState.add(successor[0])
                action(problem, gamePath, successor[1])
                dS.push((successor[0], gamePath, totalCost), totalCost)        
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    print "Start:", startState
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    dS = util.PriorityQueue()
    dS.push((startState,[]),0)
    visitedState = set([startState])
    
    if problem.isGoalState(startState):
        return []
    
    while True:
        if dS.isEmpty():
            return[]
        
        state, path = dS.pop()
      
        if problem.isGoalState(state):
            return path
        
        successors = problem.getSuccessors(state)
        
        for succ in successors:
            
            gamePath = list(path)
            
            if not succ[0] in visitedState:
                visitedState.add(succ[0])
                action(problem, gamePath, succ[1])
                dS.push((succ[0],gamePath), problem.getCostOfActions(gamePath) + heuristic(succ[0],problem))        
    return []  
    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
