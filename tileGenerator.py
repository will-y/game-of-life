import pygame as pg
import math
import sys

class TileGenerator():
    def __init__(self, screen, screenSizeX, screenSizeY):
        self.tileSize = 50
        self.tileNumX = int(screenSizeX / self.tileSize)
        self.tileNumY = int(screenSizeY / self.tileSize)
        self.screen = screen
        self.tileArray = []

    def drawTiles(self, array):
        for i in range(self.tileNumX):
            for j in range(self.tileNumY):
                if(array[i][j]):
                    self.turnTileAlive((i, j))
                else:
                    self.turnTileDead((i, j))
        self.tileArray = array

    def turnTileAlive(self, pos):
            pg.draw.rect(self.screen, pg.Color('green'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize))
            pg.draw.rect(self.screen, pg.Color('white'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize), 1)
    
    def turnTileDead(self, pos):
            pg.draw.rect(self.screen, pg.Color('black'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize))
            pg.draw.rect(self.screen, pg.Color('white'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize), 1)

    def handleClick(self, click):
        pos = self.turnToTileCoords(click[1])
        if(click[0] and not click[1] == (-1, -1)):
            self.turnTileAlive(pos)
            self.tileArray[pos[0]][pos[1]] = True
        elif(not click[1] == (-1, -1)):
            self.turnTileDead(pos)
            self.tileArray[pos[0]][pos[1]] = False

    def turnToTileCoords(self, point):
        return int(point[0] / self.tileSize), int(point[1] / self.tileSize)

    def getTileArray(self):
        return self.tileArray

    def initTileArray(self):
        for i in range(self.tileNumX):
            rowArray = []
            for j in range(self.tileNumY):
                rowArray.append(False)
            self.tileArray.append(rowArray)

