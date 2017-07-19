import pygame as pg
import sys

class StartScreen():
    def __init__(self):
        self.width = 750
        self.height = 750

        self.startScreen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Game of Life")
        self.background = pg.Surface(self.startScreen.get_size())
        self.background = self.background.convert()
        self.startScreen.fill(pg.Color('white'))
        self.clock = pg.time.Clock()

        self.titleX = 100
        self.subX = 125
        self.subSubX = 150

        self.titleFont = pg.font.SysFont("monospace", 30)
        self.subFont = pg.font.SysFont("monospace", 15)
        self.gameOfLifeRulesTitle = self.titleFont.render("Rules of Conway's Game of Life", 1, pg.Color('black'))
        self.gameOfLifeRules1 = self.subFont.render("1. Any live (green) cell with fewer than two live neighbours dies,", 1, pg.Color('black'))
        self.gameOfLifeRules1_2 = self.subFont.render("as if caused by underpopulation.", 1, pg.Color('black'))
        self.gameOfLifeRules2 = self.subFont.render("2. Any live (green) cell with two or three live neighbours lives on", 1, pg.Color('black'))
        self.gameOfLifeRules2_2 = self.subFont.render("to the next generation.", 1, pg.Color('black'))
        self.gameOfLifeRules3 = self.subFont.render("3. Any live (green) cell with more than three live neighbours dies,", 1, pg.Color('black'))
        self.gameOfLifeRules3_2 = self.subFont.render("as if by overpopulation.", 1, pg.Color('black'))
        self.gameOfLifeRules4 = self.subFont.render("4. Any dead (black) cell with exactly three live neighbours becomes", 1, pg.Color('black'))
        self.gameOfLifeRules4_2 = self.subFont.render("a live cell, as if by reproduction.", 1, pg.Color('black'))

    def launchScreen(self):
        inScreen = True
        self.drawWords()

        while(inScreen):
            self.clock.tick(60)

            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    inScreen = False

            pg.display.update()

    def drawWords(self):
        self.startScreen.blit(self.gameOfLifeRulesTitle, (100, 50))
        self.startScreen.blit(self.gameOfLifeRules1, (self.subX, 85))
        self.startScreen.blit(self.gameOfLifeRules1_2, (self.subSubX, 105))
        self.startScreen.blit(self.gameOfLifeRules2, (self.subX, 125))
        self.startScreen.blit(self.gameOfLifeRules2_2, (self.subSubX, 145))
        self.startScreen.blit(self.gameOfLifeRules3, (self.subX, 165))
        self.startScreen.blit(self.gameOfLifeRules3_2, (self.subSubX, 185))
        self.startScreen.blit(self.gameOfLifeRules4, (self.subX, 205))
        self.startScreen.blit(self.gameOfLifeRules4_2, (self.subSubX, 225))