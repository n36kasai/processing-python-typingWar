import Charactor
import Typing

bgImage = None
friendImage = None
friendCastleImage = None

testChar01 = None
testChar02 = None
testChar03 = None
typingMng = None

def setup():
    size(1366, 768)
    
    fontList= PFont.list()
    printArray(fontList)
    
    global bgImage, friendCastleImage
    global testChar01, testChar02, testChar03
    global typingMng

    bgImage = loadImage("typingWar_background.png")

    friendCastleImage = loadImage("typingWar_friendCastle.png")

    testChar01 = Charactor.CharatorFriend(1366-64-100, 768-160, 2, "aquorsChika")
    testChar02 = Charactor.CharatorFriend(1366-64-200, 768-160, 1, "aquorsMari")
    testChar03 = Charactor.CharatorFriend(1366-64-300, 768-160, 2, "aquorsChika")
    typingMng = Typing.TypingManager()
    
def keyPressed():
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
