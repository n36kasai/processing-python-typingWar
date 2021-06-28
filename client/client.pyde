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
    
    # soundMusic = SoundFile(this, "Battle-forHonor_SNES.mp3")
    soundMusic = SoundFile(this, "bgm03.mp3")
    soundMusic.amp(0.3)
    soundMusic.loop()
    soundMusic.jump(4.35)


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
    
class TypingManager():

    def __init__(self):
        self.x = 400
        self.y = 100
        self.fontHeight = 48
        self.font = createFont("UDDigiKyokashoNK-R", self.fontHeight)
        # self.font = createFont("JF-Dot-Ayu-18", self.fontHeight)
        self.mondai = []
        self.yomi = []
        self.romazi = []
        self.mondaiNo = 0
        self.mondaiMax = 0
        self.soundEffect = SoundFile(this, "key04.mp3")
        self.textReader = createReader("mondai.txt")

        self.input = ""
        self.kaitou = ""
        self.kaitouPos = 0
        
        textFont(self.font)
        self.soundEffect.amp(1)

        # 問題ファイルの読み込み
        buf = ""
        record = ""
        while buf <> None:
            buf = self.textReader.readLine()
            if buf <> None:
                record = split(buf, ",");
                self.mondai.append(record[0])
                self.yomi.append(record[1])
                self.romazi.append(record[2])
                self.mondaiMax += 1
                
        # 1問目準備
        self.kaitou = str(self.romazi[self.mondaiNo]) #キャストしないとUnicodeオブジェクトのままで厄介
        

    def keyPressed(self):
        self.soundEffect.stop()
        self.soundEffect.play()
    
        if key == ENTER:
            self.input = "EnTeR"
            self.mondaiNo += 1
            if self.mondaiNo >= self.mondaiMax:
                self.mondaiNo = 0
        else:
            
            # タイピング大戦争形式
            # if key == self.kaitou[0]:
            #     if len(self.kaitou) == 1:
            #         self.mondaiNo += 1
            #         if self.mondaiNo >= self.mondaiMax:
            #             self.mondaiNo = 0
            #         self.kaitou = self.romazi[self.mondaiNo]
            #     else:
            #         self.kaitou = self.kaitou[1:len(self.kaitou)]

            if key == self.kaitou[self.kaitouPos]:
                if self.kaitouPos >= len(self.kaitou) - 1:
                    self.mondaiNo += 1
                    self.kaitouPos = 0
                    if self.mondaiNo >= self.mondaiMax:
                        self.mondaiNo = 0
                    self.kaitou = self.romazi[self.mondaiNo]
                else:                    
                    self.kaitouPos += 1
            
                
        # elif "a" <= key <= "z" or "A" <= key <= "Z" or key == " ":
        #     self.input = self.input + key
        
    def display(self):
        
        # 問題文
        textSize(self.fontHeight)
        fill(255)
        text(self.mondai[self.mondaiNo], self.x, self.y)
        
        # ひらがな
        textSize(self.fontHeight - 30)
        fill(200)
        text(self.yomi[self.mondaiNo], self.x, self.y + 24)
        
        # ローマ字
        textSize(self.fontHeight)
        fill(255)
        text(self.romazi[self.mondaiNo], self.x, self.y + 64)
        
        # 解答欄（タイピング大戦争形式）
        # text(self.kaitou, self.x, self.y + 120)

        text(self.kaitou, self.x, self.y + 120)
        fill(255, 100, 100)
        text(self.kaitou[0:self.kaitouPos], self.x, self.y + 120)
        
        # デバッグ
        fill(255)
        text(key, self.x, self.y + 400)
        
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
        
