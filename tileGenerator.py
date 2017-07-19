import pygame as pg
import math

class TileGenerator():
    def __init__(self, screen, screenSizeX, screenSizeY):
        self.tileSize = 50
        self.tileNumX = screenSizeX / self.tileSize
        self.tileNumY = screenSizeY / self.tileSize
        self.screen = screen
        self.tileArray = []

    def drawTiles(self):
        for i in range(self.tileNumX):
            rowArray = []
            for j in range(self.tileNumY):
                rowArray.append(False)
                self.turnTileDead((i, j))
            self.tileArray.append(rowArray)
        print(self.tileArray)

    def turnTileAlive(self, pos):
            pg.draw.rect(self.screen, pg.Color('green'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize))
            pg.draw.rect(self.screen, pg.Color('white'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize), 1)
    
    def turnTileDead(self, pos):
            pg.draw.rect(self.screen, pg.Color('black'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize))
            pg.draw.rect(self.screen, pg.Color('white'), (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize), 1)

    def handleClick(self, click):
        if(click[0] and not click[1] == (-1, -1)):
            self.turnTileAlive(self.turnToTileCoords(click[1]))
        elif(not click[1] == (-1, -1)):
            self.turnTileDead(self.turnToTileCoords(click[1]))

    def turnToTileCoords(self, point):
        return math.floor(point[0] / self.tileSize), math.floor(point[1] / self.tileSize)
