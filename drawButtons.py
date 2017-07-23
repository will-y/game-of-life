import pygame as pg
import sys

class Draw():
    def __init__(self, screen, screenX, screenY, sideBarWidth):
        self.screen = screen
        self.screenX = screenX
        self.screenY = screenY
        self.sideBarWidth = sideBarWidth
        self.toolBarWidth = int(self.sideBarWidth * 2 / 3)
        print(self.toolBarWidth)
        sys.stdout.flush()
        self.toolBarHeight = self.toolBarWidth / 5
        self.toolBarX = self.screenX + (sideBarWidth / 6)

    def draw_toolbar(self, y):
        self.toolBarY = y
        pg.draw.rect(self.screen, pg.Color('purple'), (self.toolBarX, y, self.toolBarWidth, self.toolBarHeight))
        print((self.toolBarX, y, self.toolBarWidth, self.toolBarHeight))
        sys.stdout.flush()
