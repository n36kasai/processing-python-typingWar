class CharatorFriend:

    def __init__(self, x, y, fr, fileName):
        self.charImages = list()
        self.posX = x
        self.posY = y
        self.posFrame = 0
        self.maxFrame = fr
        self.nFrame = 0
        
        for i in range(1, self.maxFrame+1):
            na = "aquorsChika0" + str(i) + ".png"
            self.charImages.append(loadImage(na))
        
    def display(self):
        image(self.charImages[self.nFrame], self.posX, self.posY - self.nFrame * 4)

        
            
        if frameCount % 30 == 0:
            self.posX = self.posX - 3
            if self.posX < 0:
                self.posX = width
            if self.nFrame >= self.maxFrame - 1:
                self.nFrame = 0
            else:
                self.nFrame = self.nFrame + 1 
        
