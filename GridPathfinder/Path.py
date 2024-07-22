import Grid
import pygame as py
import time

class Node:
    def __init__(self):
        self.previous = None
        self.distance = 999
        self.Connected_Nodes = []
        self.weight = 1
    
    
class PathFinder:
    def __init__(self, maze):
        self.maze = maze
        self.maze.get_start().distance = 0
        self.unchecked = []
        self.checked = []
        self.solution = []
        self.Preload_Connections()
        self.Preload_Unchecked()
    
    def Find_Connection(self, current, location):
        test_Node = self.maze.Get_Cell_byPosition(location)
        if test_Node:
            if test_Node.State != Grid.State.WALL:
                # START HERE
                current.Connected_Nodes.append(test_Node)
    
    def Preload_Connections(self):
        for ii in range(0, self.maze.Dimension):
            for jj in range(0, self.maze.Dimension):
                current = self.maze.Get_Cell_byPosition((jj, ii))
                if current.State != Grid.State.WALL:
                    self.Find_Connection(current, (jj-1, ii))
                    self.Find_Connection(current, (jj+1, ii))
                    self.Find_Connection(current, (jj, ii-1))
                    self.Find_Connection(current, (jj, ii+1))

    # Initializes all nodes in the maze that are not a wall as being unchecked to pull from
    def Preload_Unchecked(self):
        self.unchecked = [j for i in self.maze.Cells for j in i if j.State != Grid.State.WALL]
        #self.Sort_Unchecked() # Todo: not needed as all weights are 1
        
    def Sort_Unchecked(self):
        self.unchecked.sort(key=lambda x: x.distance, reverse=False)

    
    def Step(self):
        current = self.unchecked[0]
        self.unchecked.remove(current)
        if current.State == Grid.State.STOP:
            self.checked.append(current)
            return True
        for adjacent in current.Connected_Nodes:
            # Lesson: Breadth first vs Dijkstra.
            # -- If a node has been visited, why don't we need to check it
            # -- versus Dijkstra where we would?
            if adjacent.previous is not None:
                continue
            val = current.distance + adjacent.weight
            if val < adjacent.distance:
                adjacent.previous = current
                adjacent.distance = val
        self.checked.append(current)
        self.Sort_Unchecked()
        return False
    
    
    def Solve(self):
        # Complete the solving process
        while not self.Step():
            pass

        # build the solution linked in reverse from the goal node
        current = self.maze.get_stop()
        while current:
            self.solution.append(current)
            current = current.previous
        # the solution is backwards and needs to be reversed
        self.solution.reverse()
        return self.solution, self.checked

            

            
            
    
    
    
    
    
    
    
    
    