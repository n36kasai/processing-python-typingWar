add_library("sound")

bgImage = None
friendImage = None
friendCastleImage = None

testChar01 = None
testChar02 = None
testChar03 = None
typingMng = None

soundMusic = None


def setup():
    size(1366, 768)
    
    fontList= PFont.list()
    printArray(fontList)
    
    global bgImage, friendCastleImage
    global testChar01, testChar02, testChar03
    global typingMng
    global soundMusic

    bgImage = loadImage("typingWar_background.png")
    friendCastleImage = loadImage("typingWar_friendCastle.png")

    testChar01 = CharatorFriend(1366-64-100, 768-160, 2, "aquorsChika")
    testChar02 = CharatorFriend(1366-64-200, 768-160, 1, "aquorsMari")
    testChar03 = CharatorFriend(1366-64-300, 768-160, 2, "aquorsChika")
    typingMng = TypingManager()
    
    soundMusic = SoundFile(this, "Battle-forHonor_SNES.mp3")
    soundMusic.amp(0.2)
    soundMusic.loop()


def keyPressed():
    global typingMng
    typingMng.keyPressed()
    
    
def draw():
    background(0)
    
    
    image(bgImage, 0, 0)
    image(friendCastleImage, 1366-80, 768-256+32)

    testChar01.display()
    testChar02.display()
    testChar03.display()
    typingMng.display()
    
    square(200, 200, 80)
    
class TypingManager(object):

    def __init__(self):
        # self.font = loadFont("YuKyo-Medium-48.vlw")
        self.font = createFont("UDDigiKyokashoNK-R", 48)
        self.input = ""
        self.soundEffect = SoundFile(this, "key04.mp3")
        self.soundEffect.amp(1)

        self.textReader = createReader("mondai.txt")
        linetext = self.textReader.readLine()
        pieces = split(linetext, ",");
        println(pieces[0])
    


    def keyPressed(self):
        self.soundEffect.stop()
        self.soundEffect.play()
    
        if key == ENTER:
            self.input = "EnTeR"
        elif "a" <= key <= "z" or "A" <= key <= "Z" or key == " ":
            self.input = self.input + key
        
    def display(self):
        textFont(self.font)
        text(self.input, 100, 100)
        text(key, 100, 160)
        textFont(self.font, 48)
        text(u"山田！！！！山田やまだ", 100, 200)
        
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
        
