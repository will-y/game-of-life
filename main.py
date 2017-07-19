import pygame as pg
import sys
import startScreen

class main():
    def __init__(self):
        self.windowWidth = 750
        self.windowHeight = 750
        self.screen = pg.display.set_mode((self.windowWidth, self.windowHeight))
        pg.display.set_caption("Game of Life")
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        
        self.clock = pg.time.Clock()

    def run(self):
        pg.init()
        pg.font.init()

        startScreenInstance = startScreen.StartScreen(self.windowWidth, self.windowHeight)
        startScreenInstance.launchScreen()

        self.screen.fill(pg.Color('white'))

        while(True):
            self.clock.tick(60)

            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()

            pg.display.update()

def runMain():
    mainClass = main()
    mainClass.run()

runMain()