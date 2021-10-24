import pygame


class Button:
    # 初始化
    def __init__(self, title, pos, size, bg_color, text_color=(255, 255, 255), font_size=30):
        self.title = title
        self.pos = pos
        self.size = size
        self.bg_color = bg_color
        self.text_color = text_color
        self.font_size = font_size
        self.old_color = bg_color

    # 画按钮
    def draw(self, window):
        pygame.draw.rect(window, self.bg_color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        font = pygame.font.Font('pictures and font/STKAITI.TTF', self.font_size)
        text = font.render(self.title, True, self.text_color)
        tw, th = text.get_size()
        window.blit(text, (self.pos[0] + self.size[0] / 2 - tw / 2, self.pos[1] + self.size[1] / 2 - th / 2))

    # 按钮是否被点击
    def is_down(self, pos, window):
        mx, my = pos
        btn_x, btn_y = self.pos
        btn_w, btn_h = self.size
        if btn_x <= mx <= btn_x + btn_w and btn_y <= my <= btn_y + btn_h:
            self.bg_color = (200, 200, 200)
            self.draw(window)
            pygame.display.update()
            return True

        return False

    # 按键是否弹起
    def is_up(self, pos, window):
        mx, my = pos
        btn_x, btn_y = self.pos
        btn_w, btn_h = self.size
        if btn_x <= mx <= btn_x + btn_w and btn_y <= my <= btn_y + btn_h:
            self.bg_color = self.old_color
            self.draw(window)
            pygame.display.update()
            return True

        return False
