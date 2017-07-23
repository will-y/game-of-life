import sys

class Step():
    def __init__(self):
        pass

    def step(self, tileInstance):
        self.tileInstance = tileInstance
        self.tilesX = len(self.tileInstance.tileArray)
        self.tilesY = len(self.tileInstance.tileArray[0])
        self.createNewArray()
        for i in range(self.tilesX):
            for j in range(self.tilesY):
                borders = self.checkBorders((i, j))
                if(self.tileInstance.tileArray[i][j]):
                    if(borders < 2):
                        self.newArray[i][j] = False
                    elif(borders > 3):
                        self.newArray[i][j] = False
                    else:
                        self.newArray[i][j] = True
                else:
                    if(borders == 3):
                        self.newArray[i][j] = True
                    else:
                        self.newArray[i][j] = False

        self.tileInstance.drawTiles(self.newArray)


    def checkBorders(self, pos):
        borderCount = 0
        
        if(self.checkExists((pos[0] + 1, pos[1]))):
            if(self.tileInstance.tileArray[pos[0] + 1][pos[1]]):
                borderCount += 1

        if(self.checkExists((pos[0] - 1, pos[1]))):
            if(self.tileInstance.tileArray[pos[0] - 1][pos[1]]):
                borderCount += 1

        if(self.checkExists((pos[0], pos[1] + 1))):
            if(self.tileInstance.tileArray[pos[0]][pos[1] + 1]):
                borderCount += 1

        if(self.checkExists((pos[0], pos[1] - 1))):
            if(self.tileInstance.tileArray[pos[0]][pos[1] - 1]):
                borderCount += 1

        if(self.checkExists((pos[0] + 1, pos[1] + 1))):
            if(self.tileInstance.tileArray[pos[0] + 1][pos[1] + 1]):
                borderCount += 1

        if(self.checkExists((pos[0] - 1, pos[1] - 1))):
            if(self.tileInstance.tileArray[pos[0] - 1][pos[1] - 1]):
                borderCount += 1

        if(self.checkExists((pos[0] + 1, pos[1] - 1))):
            if(self.tileInstance.tileArray[pos[0] + 1][pos[1] - 1]):
                borderCount += 1

        if(self.checkExists((pos[0] - 1, pos[1] + 1))):
            if(self.tileInstance.tileArray[pos[0] - 1][pos[1] + 1]):
                borderCount += 1
        
        return borderCount


    def checkExists(self, pos):
        if(pos[0] >= self.tilesX or pos[1] >= self.tilesY or pos[0] < 0 or pos[1] < 0):
            return False
        else:
            return True

    def createNewArray(self):
        self.newArray = []
        for i in range(self.tilesX):
            rowArray = []
            for j in range(self.tilesY):
                rowArray.append(False)
            self.newArray.append(rowArray)
