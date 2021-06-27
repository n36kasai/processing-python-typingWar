# -*- coding: utf-8 -*-

class TypingManager:

    def __init__(self):
        # self.font = loadFont("YuKyo-Medium-48.vlw")
        # self.font = createFont("YuKyo-Bold", 48)
        self.font = createFont("UDDigiKyokashoNK-R", 48)
        self.input = ""

    def keyPressed(self):
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
