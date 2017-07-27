import pygame as pg
import sys

class Draw():
    def __init__(self, screen, screenX, screenY, sideBarWidth):
        self.screen = screen
        self.screenX = screenX
        self.screenY = screenY
        self.sideBarWidth = sideBarWidth
        self.toolBarWidth = int(self.sideBarWidth * 2 / 3)
        self.toolBarHeight = self.toolBarWidth / 5
        self.toolBarX = self.screenX + (sideBarWidth / 6)

        

    def draw_toolbar(self, y):
        self.toolBarY = y
        pg.draw.rect(self.screen, pg.Color('purple'), (self.toolBarX, y, self.toolBarWidth, self.toolBarHeight))

    def draw_textbox(self, y):
        pg.draw.rect(self.screen, pg.Color('black'), (self.toolBarX, y, 30, 20), 3)

    def draw_changeSizeButton(self, y):
        pass