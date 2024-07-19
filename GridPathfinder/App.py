import pygame as py
import Grid
import Path

# Constants
SCREENWIDTH = 500
SCREENHEIGHT = 500
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
FRAMERATE = 30
SCREENCOLOR = (0, 0, 0)


# Initialize game variables
clock = py.time.Clock()
screen = py.display.set_mode(SCREENSIZE)

# Set up game
isRunning = False

Map = Grid.Grid(Screen = screen, Dimension = 10)


def OnMouseClick():
    global Map
    mouse_loc = py.mouse.get_pos()
    Map.Clear_Solution()
    cell = Map.Get_Cell_byScreenLocation(mouse_loc)
    cell.Swap_Wall()
    

def OnKeyPress(key):
    global Map
    if key == py.K_SPACE:
        Map.Clear_Solution()
        Dijkstra = Path.Dijkstra(Map)
        Dijkstra.Solve()
        print("Done")
    
py.init()

# Main Game Loop
app_running = True
while app_running:
    #Handle Events
    for event in py.event.get():
        if event.type == py.QUIT:
            app_running = False
        if event.type == py.MOUSEBUTTONUP:
            if not isRunning:
                OnMouseClick()
        if event.type == py.KEYDOWN:
            OnKeyPress(event.key)

    #Draw
    screen.fill(SCREENCOLOR)
    Map.Draw()
   
    py.display.flip()
    #Update
   
    clock.tick(FRAMERATE)

py.quit()