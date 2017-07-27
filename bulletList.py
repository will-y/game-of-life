import pygame as pg
import sys

class BulletList():
    def __init__(self, screen, pos, numOptions, title, optionNames):
        self.screen = screen
        self.x = pos[0]
        self.y = pos[1]
        self.optionX = self.x + 30
        self.optionPadding = 50
        self.numOptions = numOptions
        self.titleText = title
        self.optionNames = optionNames
        self.optionSelected = 0
        self.optionArray = []

        self.initOptionArray()

        self.titleFont = pg.font.SysFont("monospace", 30)
        self.optionFont = pg.font.SysFont("monospace", 20)
        self.title = self.titleFont.render(self.titleText, 1, pg.Color('black'))

    def drawList(self):
        print("Drawing List")
        sys.stdout.flush()
        self.screen.blit(self.title, (self.x, self.y))

        for i in range(self.numOptions - 1):
            text = self.optionFont.render(self.optionNames[i], 1, pg.Color('black'))
            self.screen.blit(text, (self.optionX, self.y + self.optionPadding * (i + 1)))

    def updateChoice(self, click):
        pass

    def getChoice(self):
        return self.optionSelected

    def initOptionArray(self):
        for i in range(self.numOptions - 1):
            self.optionArray.append(0)
        self.optionArray[0] = 1