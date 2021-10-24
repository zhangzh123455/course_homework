import pygame


class picture:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def picture_isdown(self, pos, num):
        mx, my = pos
        px, py = self.pos
        pw, ph = self.size
        if px <= mx <= px + pw and py <= my <= py + ph and num != 0:
            return True

        return False

    def picture_isup(self, pos, num):
        mx, my = pos
        px, py = self.pos
        pw, ph = self.size
        if px <= mx <= px + pw and py <= my <= py + ph and num != 0:
            return True

        return False
