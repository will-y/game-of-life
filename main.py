import pygame as pg
import sys
import startScreen
import tileGenerator
import stepSystem
import time
import drawButtons
import bulletList

class main():
    def __init__(self):
        self.windowWidth = 1000
        self.windowHeight = 1000
        self.currentClick = (0, 0)

        self.sideBarWidth = 300
        
        self.clock = pg.time.Clock()

        self.stepMode = False

    def run(self):
        pg.init()
        pg.font.init()

        startScreenInstance = startScreen.StartScreen()
        startScreenInstance.launchScreen()
        
        self.screen = pg.display.set_mode((self.windowWidth + self.sideBarWidth, self.windowHeight))
        pg.display.set_caption("Game of Life")
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill(pg.Color('white'))

        tileGeneratorInstance = tileGenerator.TileGenerator(self.screen, self.windowWidth, self.windowHeight)
        tileGeneratorInstance.initTileArray()
        tileGeneratorInstance.drawTiles(tileGeneratorInstance.tileArray)

        print((self.screen, self.windowWidth, self.windowHeight, self.sideBarWidth))
        sys.stdout.flush()

        drawer = drawButtons.Draw(self.screen, self.windowWidth, self.windowHeight, self.sideBarWidth)
        
        drawer.draw_toolbar(200)

        drawer.draw_textbox(100)

        sizeList = bulletList.BulletList(self.screen, (1100, 100), 5, "List", ["Option1", "Option2", "Option3", "Option4", "Option5"])

        sizeList.drawList()
        stepInstance = stepSystem.Step()

        

        while(True):
            self.clock.tick(60)
            key = pg.key.get_pressed()

            if(not self.stepMode):
                click = self.detectClick()
                tileGeneratorInstance.handleClick(click)
                self.currentClick = click[1]
                self.leftClick = click[0]
            else:
                stepInstance.step(tileGeneratorInstance)
                time.sleep(1)

            if key[pg.K_RETURN]:
                self.stepMode = True
                time.sleep(.5)

            events = pg.event.get()
            for event in events:
                if(event.type == pg.QUIT):
                    sys.exit()
            
            pg.display.update()

    def detectClick(self):
        if(pg.mouse.get_pressed()[0]):
            return True, pg.mouse.get_pos()
        elif(pg.mouse.get_pressed()[2]):
            return False, pg.mouse.get_pos()
        else:
            return True, (-1, -1)

def runMain():
    mainClass = main()
    mainClass.run()

runMain()