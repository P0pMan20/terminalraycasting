# row, column
#TODO
# triangles
# rotation
# floor + celing
#  larger grid
# find terminal size
# Use more ASCII/ UTF 8 chars for walls
import os
import keyboard
import time

cameraY = 1
cameraX = 1
grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def printGrid():
    os.system("cls")
    grid[cameraY][cameraX] = 2
    for i in grid:
        print(i)
    pass

grid[cameraY][cameraX] = 2


def wait(length):
    time.sleep(length)


def createLine(height):
    line = []
    for i in range(height):
        line.append(["#"])

    return line


def lineCreateRender(height):
    line = []
    for i in range(height):
        line.append(["#"])
    for i in line:
        print(i)
    os.system("cls")
def getDistanceToWall(xpos, ypos): #currently this is a terrible way of doing this
    for i in range(len(grid[ypos])):
        if grid[ypos - i][xpos] == 1:
            return i

def basicLineLengthRender():
    pass

os.system("cls")
for i in grid:
    print(i)
time.sleep(2)
#
while True:
    if keyboard.is_pressed("w"):
        grid[cameraY][cameraX] = 0
        if grid[cameraY - 1][cameraX] != 1:
            cameraY -= 1
        printGrid()
        # print(getDistanceToWall(cameraX,cameraY))
        wait(0.2)
    if keyboard.is_pressed("s"):
        grid[cameraY][cameraX] = 0
        if grid[cameraY + 1][cameraX] != 1:
            cameraY += 1
        printGrid()
        wait(0.2)
    if keyboard.is_pressed("a"):
        grid[cameraY][cameraX] = 0
        if grid[cameraY][cameraX - 1] != 1:
            cameraX -= 1
        printGrid()
        wait(0.2)
    if keyboard.is_pressed("d"):
        grid[cameraY][cameraX] = 0
        if grid[cameraY][cameraX + 1] != 1:
            cameraX += 1
        printGrid()
        wait(0.2)
    # lineCreateRender(getDistanceToWall(cameraX, cameraY))
