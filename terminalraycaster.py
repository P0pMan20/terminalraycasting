# row, column
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
def getDistanceToWall(xpos, ypos):
    for i in range():
        if grid[cameraY + i][cameraX] == 1:
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
# lineCreateRender(6)
