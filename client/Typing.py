# -*- coding: utf-8 -*-

import processing.sound.*

class TypingManager:

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
        # self.soundEffect.stop()
        # self.soundEffect.play()
    
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
