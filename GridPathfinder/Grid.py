import pygame as py
import random
import Path


class State:
    OPEN = 0
    WALL = 1
    START = 2
    STOP = 3
    PATH = 4
    SEARCHED = 5
    

class Colors:
    State_Colors = {State.OPEN:(255,255,255), 
                    State.WALL:(100,100,100),
                    State.START:(0,255,0),
                    State.STOP:(0,0,255),
                    State.PATH:(255,0,0),
                    State.SEARCHED:(0,255,255)}
    
    def Get_StateColor(state):
        if state in Colors.State_Colors.keys():
            return Colors.State_Colors[state]


class Cell(Path.Node):
    def __init__(self):
        super().__init__()
        self.State = State.OPEN
        
    def Swap_Wall(self):
        if self.State == State.OPEN:
            self.State = State.WALL
        elif self.State == State.WALL:
            self.State = State.OPEN
    
    
class Grid:
    def __init__(self, Screen:py.display, Dimension:int):
        self.Screen = Screen
        self.Dimension = Dimension
        self.Cells = []
        self.solution = None
        self.Line_Weight = 1
        self.Cell_size = int(Screen.get_width() / Dimension) - self.Line_Weight
        self.Start = None
        self.Stop = None
        self._build_Grid()
        
    def _build_Grid(self):
        for ii in range(0, self.Dimension):
            new_row = []
            for jj in range(0, self.Dimension):
                c = Cell()
                new_row.append(c)
            self.Cells.append(new_row)
        self.Set_Start(self.Cells[0][0])
        self.Set_Stop(self.Cells[self.Dimension-1][self.Dimension-1])
                
    
    # Returns the cell based on location in the 2D List
    def Get_Cell_byPosition(self, location):
        if location[0] < 0 or location[1] < 0:
            return None
        if location[0] >= self.Dimension or location[1] >= self.Dimension:
            return None
        return self.Cells[location[0]][location[1]]
    
    # Returns the Cell based on location on screen
    def Get_Cell_byScreenLocation(self, location):
        x = location[0] // (self.Cell_size + self.Line_Weight)
        y = location[1] // (self.Cell_size + self.Line_Weight)
        return self.Cells[x][y]
    
    def Set_Start(self, cell):
        if self.Start != None:
            self.Start.State = State.OPEN
        self.Start = cell
        self.Start.State = State.START
    
    def Get_Start(self):
        return self.Start
    
    def Set_Stop(self, cell):
        if self.Stop != None:
            self.Stop.State = State.OPEN
        self.Stop = cell
        self.Stop.State = State.STOP
    
    def Get_Stop(self):
        return self.Stop

    def set_solution(self, solution: [], checked_nodes: [] = None):
        self.solution = solution

        if checked_nodes is not None:
            for node in checked_nodes:
                node.State = State.SEARCHED

        for node in solution:
            node.State = State.PATH

    def Draw(self):
        for ii in range(0, self.Dimension):
            for jj in range(0, self.Dimension):
                py.draw.rect(self.Screen, 
                             Colors.Get_StateColor(self.Cells[jj][ii].State), 
                             py.Rect(jj*(self.Cell_size + self.Line_Weight),
                                     ii*(self.Cell_size + self.Line_Weight),
                                     self.Cell_size,self.Cell_size))
        
        
    def Clear_Solution(self):
        self.solution = None
        for ii in range(0, self.Dimension):
            for jj in range(0, self.Dimension):
                if self.Cells[ii][jj].State != State.WALL:
                    self.Cells[ii][jj].State = State.OPEN
                    self.Cells[ii][jj].distance = 999
                    self.Cells[ii][jj].previous = None
                    self.Cells[ii][jj].Connected_Nodes.clear()
        self.Get_Start().State = State.START
        self.Get_Stop().State = State.STOP
        
        
        
        
        
        
        
        
        
        