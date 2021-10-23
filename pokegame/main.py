import pygame
import random
import button
import pictureevent

# 颜色
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (138, 43, 226)
orange = (255, 153, 18)
titlecolor = (170, 47, 138)
# 界面的宽和高
win_width = 800
win_height = 700
# 卡牌的宽和高
poker_w = 105
poker_h = 150
poker_size = (poker_w, poker_h)
# 部分间距长度
t = 5
lx = 50
ly = 47
pygame.init()
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('猪尾巴')
# 设置背景颜色
window.fill((255, 255, 255))
# 刷新显示页面
# pygame.display.flip()     - 第一次刷新
pygame.display.flip()
# 字体
font = pygame.font.Font('pictures and font/STKAITI.TTF', 30)
text1 = font.render('卡组', True, red, yellow)
text2 = font.render('放置区', True, red, yellow)
text3 = font.render('player1', True, red)
text4 = font.render('player2', True, red)
text5 = font.render('*', True, red)
text6 = font.render('*', True, black)
text7 = font.render('ROUND PLAYER1', True, blue, purple)
text8 = font.render('ROUND PLAYER2', True, blue, purple)
font2 = pygame.font.Font('pictures and font/千图小兔体.ttf', 150)
gametitle = font2.render('猪尾巴', True, titlecolor)
# 导入图片
back = pygame.image.load('pictures and font/pokerback.jpg')
back1 = pygame.image.load('pictures and font/pokerback1.png')
back2 = pygame.image.load('pictures and font/pokerback2.png')
back3 = pygame.image.load('pictures and font/pokerback3.png')
back4 = pygame.image.load('pictures and font/pokerback4.png')
heitao = pygame.image.load('pictures and font/黑桃.png')
hongtao = pygame.image.load('pictures and font/红桃.png')
meihua = pygame.image.load('pictures and font/梅花.png')
fangkua = pygame.image.load('pictures and font/方块.png')
background1 = pygame.image.load('pictures and font/背景图.png')
background2 = pygame.image.load('pictures and font/background.jpg')
heit1 = pygame.image.load('pictures and font/heitao1.jpg')
heit2 = pygame.image.load('pictures and font/heitao2.jpg')
heit3 = pygame.image.load('pictures and font/heitao3.jpg')
heit4 = pygame.image.load('pictures and font/heitao4.jpg')
heit5 = pygame.image.load('pictures and font/heitao5.jpg')
heit6 = pygame.image.load('pictures and font/heitao6.jpg')
heit7 = pygame.image.load('pictures and font/heitao7.jpg')
heit8 = pygame.image.load('pictures and font/heitao8.jpg')
heit9 = pygame.image.load('pictures and font/heitao9.jpg')
heit10 = pygame.image.load('pictures and font/heitao10.jpg')
heit11 = pygame.image.load('pictures and font/heitao11.jpg')
heit12 = pygame.image.load('pictures and font/heitao12.jpg')
heit13 = pygame.image.load('pictures and font/heitao13.jpg')
hongt1 = pygame.image.load('pictures and font/hongtao1.jpg')
hongt2 = pygame.image.load('pictures and font/hongtao2.jpg')
hongt3 = pygame.image.load('pictures and font/hongtao3.jpg')
hongt4 = pygame.image.load('pictures and font/hongtao4.jpg')
hongt5 = pygame.image.load('pictures and font/hongtao5.jpg')
hongt6 = pygame.image.load('pictures and font/hongtao6.jpg')
hongt7 = pygame.image.load('pictures and font/hongtao7.jpg')
hongt8 = pygame.image.load('pictures and font/hongtao8.jpg')
hongt9 = pygame.image.load('pictures and font/hongtao9.jpg')
hongt10 = pygame.image.load('pictures and font/hongtao10.jpg')
hongt11 = pygame.image.load('pictures and font/hongtao11.jpg')
hongt12 = pygame.image.load('pictures and font/hongtao12.jpg')
hongt13 = pygame.image.load('pictures and font/hongtao13.jpg')
mh1 = pygame.image.load('pictures and font/meihua1.jpg')
mh2 = pygame.image.load('pictures and font/meihua2.jpg')
mh3 = pygame.image.load('pictures and font/meihua3.jpg')
mh4 = pygame.image.load('pictures and font/meihua4.jpg')
mh5 = pygame.image.load('pictures and font/meihua5.jpg')
mh6 = pygame.image.load('pictures and font/meihua6.jpg')
mh7 = pygame.image.load('pictures and font/meihua7.jpg')
mh8 = pygame.image.load('pictures and font/meihua8.jpg')
mh9 = pygame.image.load('pictures and font/meihua9.jpg')
mh10 = pygame.image.load('pictures and font/meihua10.jpg')
mh11 = pygame.image.load('pictures and font/meihua11.jpg')
mh12 = pygame.image.load('pictures and font/meihua12.jpg')
mh13 = pygame.image.load('pictures and font/meihua13.jpg')
fk1 = pygame.image.load('pictures and font/fangkuai1.jpg')
fk2 = pygame.image.load('pictures and font/fangkuai2.jpg')
fk3 = pygame.image.load('pictures and font/fangkuai3.jpg')
fk4 = pygame.image.load('pictures and font/fangkuai4.jpg')
fk5 = pygame.image.load('pictures and font/fangkuai5.jpg')
fk6 = pygame.image.load('pictures and font/fangkuai6.jpg')
fk7 = pygame.image.load('pictures and font/fangkuai7.jpg')
fk8 = pygame.image.load('pictures and font/fangkuai8.jpg')
fk9 = pygame.image.load('pictures and font/fangkuai9.jpg')
fk10 = pygame.image.load('pictures and font/fangkuai10.jpg')
fk11 = pygame.image.load('pictures and font/fangkuai11.jpg')
fk12 = pygame.image.load('pictures and font/fangkuai12.jpg')
fk13 = pygame.image.load('pictures and font/fangkuai13.jpg')
picture_list = [heit1, heit2, heit3, heit4, heit5, heit6, heit7, heit8, heit9, heit10, heit11, heit12, heit13, hongt1,
                hongt2, hongt3, hongt4, hongt5, hongt6, hongt7, hongt8, hongt9, hongt10, hongt11, hongt12, hongt13, mh1,
                mh2, mh3, mh4, mh5, mh6, mh7, mh8, mh9, mh10, mh11, mh12, mh13, fk1, fk2, fk3, fk4, fk5, fk6, fk7, fk8,
                fk9, fk10, fk11, fk12, fk13]
# 生成一个13张的牌组
poker_num = [i for i in range(1, 14)]
# print(poker_num)

# 生成花色列表
poker_color = ['黑桃', '红桃', '梅花', '方块']

# 生成牌组
poker = [[color, num] for num in poker_num for color in poker_color]
# print(poker)
# print(len(poker))
# 打乱牌组
random.shuffle(poker)
placed_poker = []  # 放置区的牌库
player1_poker1 = []  # 玩家1的黑桃牌
player1_poker2 = []  # 玩家1的红桃牌
player1_poker3 = []  # 玩家1的梅花牌
player1_poker4 = []  # 玩家1的方块牌
player2_poker1 = []  # 玩家2的黑桃牌
player2_poker2 = []  # 玩家2的红桃牌
player2_poker3 = []  # 玩家2的梅花牌
player2_poker4 = []  # 玩家2的方块牌
text = font.render('num:', True, black)

l1 = 13
len1 = str(l1)
kazu_n1 = font.render(len1, True, black)
kazu_n2 = font.render(len1, True, red)
kazu_n3 = font.render(len1, True, black)
kazu_n4 = font.render(len1, True, red)

l2 = len(placed_poker)
len2 = str(l2)
placed_poker_num = font.render(len2, True, black)

l11 = len(player1_poker1)
len11 = str(l11)
l12 = len(player1_poker2)
len12 = str(l12)
l13 = len(player1_poker3)
len13 = str(l13)
l14 = len(player1_poker4)
len14 = str(l14)
p1_n1 = font.render(len11, True, black)
p1_n2 = font.render(len12, True, red)
p1_n3 = font.render(len13, True, black)
p1_n4 = font.render(len14, True, red)

l21 = len(player2_poker1)
len21 = str(l21)
l22 = len(player2_poker2)
len22 = str(l22)
l23 = len(player2_poker3)
len23 = str(l23)
l24 = len(player2_poker4)
len24 = str(l24)
p2_n1 = font.render(len21, True, black)
p2_n2 = font.render(len22, True, red)
p2_n3 = font.render(len23, True, black)
p2_n4 = font.render(len24, True, red)
print(poker)
# 双人对战的按钮
window.blit(background1, (0, 0))
window.blit(gametitle, (win_width / 2 - 225, 0.15 * win_height))
d_button = button.Button('双人对战', (win_width / 2 - 100, win_height / 2 - 25), (160, 50), titlecolor, blue)
d_button.draw(window)
pygame.display.update()
# 判断游戏是否开始的布尔值
is_begin = False


# 游戏循环


def poker_nn(poke):
    huase, shuzi = poke
    if huase == '黑桃':
        a = 1
    elif huase == '红桃':
        a = 2
    elif huase == '梅花':
        a = 3
    else:
        a = 4
    b = (a - 1) * 13 + shuzi - 1
    return b


lk1 = 13
lk2 = 13
lk3 = 13
lk4 = 13
lenk1 = str(lk1)
lenk2 = str(lk2)
lenk3 = str(lk3)
lenk4 = str(lk4)
kazudown = False
is_movplaced = False
movplaced_speed = 1
is_null = True
is_player1 = True
y1_speed1 = -1
y2_speed1 = -1
y3_speed1 = -1
y4_speed1 = -1
y1_speed2 = 1
y2_speed2 = 1
y3_speed2 = 1
y4_speed2 = 1
move_list = []
while True:
    # 事件检测
    for event in pygame.event.get():
        # 玩家1摸牌
        if is_movplaced and is_player1 is True:
            cur_poker = poker.pop()
            placed_poker.append(cur_poker)
            a, b = cur_poker[0], cur_poker[1]
            p = poker_nn(cur_poker)
            l2 = len(placed_poker)
            len2 = str(l2)
            if a == '黑桃':
                lk1 -= 1
                lenk1 = str(lk1)
            elif a == '红桃':
                lk2 -= 1
                lenk2 = str(lk2)
            elif a == '梅花':
                lk3 -= 1
                lenk3 = str(lk3)
            elif a == '方块':
                lk4 -= 1
                lenk4 = str(lk4)
            placed_poker_num = font.render(len2, True, black)
            kazu_n1 = font.render(lenk1, True, black)
            kazu_n2 = font.render(lenk2, True, red)
            kazu_n3 = font.render(lenk3, True, black)
            kazu_n4 = font.render(lenk4, True, red)
            # 放置区中没有牌的时候, 将摸到的牌移动到放置区
            if is_null is True:
                # 摸牌放到放置区
                while movplaced_speed <= win_width / 2:
                    window.blit(begin_screen, (0, 0))
                    movplaced_speed += 0.8
                    window.blit(picture_list[p], (kazu_x + movplaced_speed, kazu_y))
                    window.blit(placed_poker_num,
                                (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                    window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                    window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                    window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                    window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                    l11 = len(player1_poker1)
                    len11 = str(l11)
                    l12 = len(player1_poker2)
                    len12 = str(l12)
                    l13 = len(player1_poker3)
                    len13 = str(l13)
                    l14 = len(player1_poker4)
                    len14 = str(l14)
                    l21 = len(player2_poker1)
                    len21 = str(l21)
                    l22 = len(player2_poker2)
                    len22 = str(l22)
                    l23 = len(player2_poker3)
                    len23 = str(l23)
                    l24 = len(player2_poker4)
                    len24 = str(l24)
                    p1_n1 = font.render(len11, True, black)
                    p1_n2 = font.render(len12, True, red)
                    p1_n3 = font.render(len13, True, black)
                    p1_n4 = font.render(len14, True, red)
                    p2_n1 = font.render(len21, True, black)
                    p2_n2 = font.render(len22, True, red)
                    p2_n3 = font.render(len23, True, black)
                    p2_n4 = font.render(len24, True, red)
                    window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                    window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                    window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                    window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                    window.blit(p2_n1, (win_width - lx - t * 7 - poker_w * 4 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n2, (win_width - lx - t * 5 - poker_w * 3 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n3, (win_width - lx - t * 3 - poker_w * 2 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n4, (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                    pygame.display.update()
                is_null = False
            # 放置区有牌时， 将摸到的牌移动到放置区并进行花色比较
            else:
                # 当花色一样时
                if int(p / 13) == int(t_p2 / 13):
                    for i in range(l2):
                        pii = placed_poker.pop()
                        n1 = poker_nn(pii)
                        move_list.append(pii)
                        if 0 <= n1 <= 12:
                            player1_poker1.append(pii)
                        elif 13 <= n1 <= 25:
                            player1_poker2.append(pii)
                        elif 26 <= n1 <= 38:
                            player1_poker3.append(pii)
                        elif 39 <= n1 <= 51:
                            player1_poker4.append(pii)
                    l2 = 0
                    is_null = True
                # 从卡组摸牌移动到放置区
                while movplaced_speed <= win_width / 2:
                    window.blit(begin_screen, (0, 0))
                    window.blit(temp_p, (kazu_x + win_width / 2, kazu_y))
                    movplaced_speed += 1
                    window.blit(picture_list[p], (kazu_x + movplaced_speed, kazu_y))
                    window.blit(placed_poker_num,
                                (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                    window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                    window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                    window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                    window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                    l11 = len(player1_poker1)
                    len11 = str(l11)
                    l12 = len(player1_poker2)
                    len12 = str(l12)
                    l13 = len(player1_poker3)
                    len13 = str(l13)
                    l14 = len(player1_poker4)
                    len14 = str(l14)
                    l21 = len(player2_poker1)
                    len21 = str(l21)
                    l22 = len(player2_poker2)
                    len22 = str(l22)
                    l23 = len(player2_poker3)
                    len23 = str(l23)
                    l24 = len(player2_poker4)
                    len24 = str(l24)
                    l2 = len(placed_poker)
                    len2 = str(l2)
                    placed_poker_num = font.render(len2, True, black)
                    p1_n1 = font.render(len11, True, black)
                    p1_n2 = font.render(len12, True, red)
                    p1_n3 = font.render(len13, True, black)
                    p1_n4 = font.render(len14, True, red)
                    p2_n1 = font.render(len21, True, black)
                    p2_n2 = font.render(len22, True, red)
                    p2_n3 = font.render(len23, True, black)
                    p2_n4 = font.render(len24, True, red)
                    window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                    window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                    window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                    window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                    window.blit(p2_n1, (win_width - lx - t * 7 - poker_w * 4 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n2, (win_width - lx - t * 5 - poker_w * 3 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n3, (win_width - lx - t * 3 - poker_w * 2 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n4, (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                    pygame.display.update()
                # 将放置区的牌归玩家一所有
                for movepoke in move_list:
                    n1 = poker_nn(movepoke)
                    if 0 <= n1 <= 12:
                        while y1_speed1 >= p1_y1 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x + k11 * y1_speed1, place_y + y1_speed1))
                            y1_speed1 -= 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y1_speed1 = -1
                    elif 13 <= n1 <= 25:
                        while y2_speed1 >= p1_y2 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x + k12 * y2_speed1, place_y + y2_speed1))
                            y2_speed1 -= 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y2_speed1 = -1
                    elif 26 <= n1 <= 38:
                        while y3_speed1 >= p1_y3 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x + k13 * y3_speed1, place_y + y3_speed1))
                            y3_speed1 -= 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y3_speed1 = -1
                    elif 39 <= n1 <= 51:
                        while y4_speed1 >= p1_y4 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x + k14 * y4_speed1, place_y + y4_speed1))
                            y4_speed1 -= 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y4_speed1 = -1
                move_list = []
            t_p1 = p
            temp_p = picture_list[p]
            movplaced_speed = 1
            window.blit(text8, (win_width / 2 - x / 2, win_height / 2 - y))
            pygame.display.update()
            print(p)
            is_player1 = False
            is_movplaced = False
        # 玩家2摸牌
        if is_movplaced and is_player1 is not True:
            cur_poker = poker.pop()
            placed_poker.append(cur_poker)
            a, b = cur_poker[0], cur_poker[1]
            p = poker_nn(cur_poker)
            l2 = len(placed_poker)
            len2 = str(l2)
            if a == '黑桃':
                lk1 -= 1
                lenk1 = str(lk1)
            elif a == '红桃':
                lk2 -= 1
                lenk2 = str(lk2)
            elif a == '梅花':
                lk3 -= 1
                lenk3 = str(lk3)
            elif a == '方块':
                lk4 -= 1
                lenk4 = str(lk4)
            placed_poker_num = font.render(len2, True, black)
            kazu_n1 = font.render(lenk1, True, black)
            kazu_n2 = font.render(lenk2, True, red)
            kazu_n3 = font.render(lenk3, True, black)
            kazu_n4 = font.render(lenk4, True, red)
            # 放置区中没有牌的时候
            if is_null is True:
                # 将牌摸到放置区
                while movplaced_speed <= win_width / 2:
                    window.blit(begin_screen, (0, 0))
                    movplaced_speed += 0.8
                    window.blit(picture_list[p], (kazu_x + movplaced_speed, kazu_y))
                    window.blit(placed_poker_num,
                                (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                    window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                    window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                    window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                    window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                    l11 = len(player1_poker1)
                    len11 = str(l11)
                    l12 = len(player1_poker2)
                    len12 = str(l12)
                    l13 = len(player1_poker3)
                    len13 = str(l13)
                    l14 = len(player1_poker4)
                    len14 = str(l14)
                    l21 = len(player2_poker1)
                    len21 = str(l21)
                    l22 = len(player2_poker2)
                    len22 = str(l22)
                    l23 = len(player2_poker3)
                    len23 = str(l23)
                    l24 = len(player2_poker4)
                    len24 = str(l24)
                    p1_n1 = font.render(len11, True, black)
                    p1_n2 = font.render(len12, True, red)
                    p1_n3 = font.render(len13, True, black)
                    p1_n4 = font.render(len14, True, red)
                    p2_n1 = font.render(len21, True, black)
                    p2_n2 = font.render(len22, True, red)
                    p2_n3 = font.render(len23, True, black)
                    p2_n4 = font.render(len24, True, red)
                    window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                    window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                    window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                    window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                    window.blit(p2_n1, (win_width - lx - t * 7 - poker_w * 4 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n2, (win_width - lx - t * 5 - poker_w * 3 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n3, (win_width - lx - t * 3 - poker_w * 2 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n4, (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                    pygame.display.update()
                is_null = False

            # 放置区有牌
            else:
                # 当花色一样时
                if int(p / 13) == int(t_p1 / 13):
                    print('=========')
                    for i in range(l2):
                        pii = placed_poker.pop()
                        n1 = poker_nn(pii)
                        move_list.append(pii)
                        if 0 <= n1 <= 12:
                            player2_poker1.append(pii)
                        elif 13 <= n1 <= 25:
                            player2_poker2.append(pii)
                        elif 26 <= n1 <= 38:
                            player2_poker3.append(pii)
                        elif 39 <= n1 <= 51:
                            player2_poker4.append(pii)
                    l2 = 0
                    is_null = True
                # 从卡组摸牌到放置区
                while movplaced_speed <= win_width / 2:
                    window.blit(begin_screen, (0, 0))
                    window.blit(temp_p, (kazu_x + win_width / 2, kazu_y))
                    movplaced_speed += 1
                    window.blit(picture_list[p], (kazu_x + movplaced_speed, kazu_y))
                    window.blit(placed_poker_num,
                                (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                    window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                    window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                    window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                    window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                    l11 = len(player1_poker1)
                    len11 = str(l11)
                    l12 = len(player1_poker2)
                    len12 = str(l12)
                    l13 = len(player1_poker3)
                    len13 = str(l13)
                    l14 = len(player1_poker4)
                    len14 = str(l14)
                    l21 = len(player2_poker1)
                    len21 = str(l21)
                    l22 = len(player2_poker2)
                    len22 = str(l22)
                    l23 = len(player2_poker3)
                    len23 = str(l23)
                    l24 = len(player2_poker4)
                    len24 = str(l24)
                    l2 = len(placed_poker)
                    len2 = str(l2)
                    placed_poker_num = font.render(len2, True, black)
                    p1_n1 = font.render(len11, True, black)
                    p1_n2 = font.render(len12, True, red)
                    p1_n3 = font.render(len13, True, black)
                    p1_n4 = font.render(len14, True, red)
                    p2_n1 = font.render(len21, True, black)
                    p2_n2 = font.render(len22, True, red)
                    p2_n3 = font.render(len23, True, black)
                    p2_n4 = font.render(len24, True, red)
                    window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                    window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                    window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                    window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                    window.blit(p2_n1, (win_width - lx - t * 7 - poker_w * 4 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n2, (win_width - lx - t * 5 - poker_w * 3 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n3, (win_width - lx - t * 3 - poker_w * 2 + 80, win_height - 9 * t - poker_h - 15))
                    window.blit(p2_n4, (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                    pygame.display.update()
                    is_player1 = True
                # 玩家2摸到的牌与放置区牌堆顶的牌花色一样，将获得所要牌
                for movepoke in move_list:
                    n1 = poker_nn(movepoke)
                    if 0 <= n1 <= 12:
                        while y4_speed2 <= p2_y4 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x - k24 * y4_speed2, place_y + y4_speed2))
                            y4_speed2 += 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y4_speed2 = 1
                    elif 13 <= n1 <= 25:
                        while y3_speed2 <= p2_y3 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x + k23 * y3_speed2, place_y + y3_speed2))
                            y3_speed2 += 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y3_speed2 = +1
                    elif 26 <= n1 <= 38:
                        while y2_speed2 <= p2_y2 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x + k22 * y2_speed2, place_y + y2_speed2))
                            y2_speed2 += 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y2_speed2 = 1
                    elif 39 <= n1 <= 51:
                        while y1_speed2 <= p2_y1 - place_y:
                            window.blit(begin_screen, (0, 0))
                            window.blit(picture_list[n1], (place_x + k21 * y1_speed2, place_y + y1_speed2))
                            y1_speed2 += 1
                            window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                            window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                            window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                            window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                            window.blit(placed_poker_num,
                                        (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                            window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                            window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                            window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                            window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                            window.blit(p2_n1,
                                        (win_width - lx - t * 7 - poker_w * 4 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n2,
                                        (win_width - lx - t * 5 - poker_w * 3 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n3,
                                        (win_width - lx - t * 3 - poker_w * 2 + 80,
                                         win_height - 9 * t - poker_h - 15))
                            window.blit(p2_n4,
                                        (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                            pygame.display.update()
                        y1_speed2 = 1
                move_list = []
            t_p2 = p
            temp_p = picture_list[p]
            movplaced_speed = 1
            window.blit(text7, (win_width / 2 - x / 2, win_height / 2 - y))
            pygame.display.update()
            print(p)
            is_movplaced = False
            is_player1 = True
        # 检测鼠标点击事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            l0 = len(poker)
            if is_begin is not True:
                d_button.is_down(event.pos, window)
            elif kazu.move_placed_isdown(event.pos, l0):
                kazudown = True
        # 检测鼠标弹起事件
        if event.type == pygame.MOUSEBUTTONUP:
            # 点击双人对战按钮后切换到游戏界面并开始
            if is_begin is not True and d_button.is_up(event.pos, window):
                is_begin = True
                window.blit(background2, (0, 0))
                pygame.display.update()
                # 生成卡组图像
                window.blit(back, (win_width / 4 - poker_w / 2, win_height / 2 - poker_h * 0.7))
                w1, h1 = text1.get_size()
                window.blit(text1, (win_width / 4 - w1 / 2, win_height / 2 + poker_h * 0.3 + t + 5))
                kazu_x, kazu_y = (win_width / 4 - poker_w / 2, win_height / 2 - poker_h * 0.7)
                window.blit(heitao, (30, win_height / 2 - poker_h * 0.7 + 10))
                window.blit(text6, (30 + 40, win_height / 2 - poker_h * 0.7 + 10))
                window.blit(hongtao, (30, win_height / 2 - poker_h * 0.7 + 50))
                window.blit(text5, (30 + 40, win_height / 2 - poker_h * 0.7 + 50))
                window.blit(meihua, (30, win_height / 2 - poker_h * 0.7 + 90))
                window.blit(text6, (30 + 40, win_height / 2 - poker_h * 0.7 + 90))
                window.blit(fangkua, (30, win_height / 2 - poker_h * 0.7 + 130))
                window.blit(text5, (30 + 40, win_height / 2 - poker_h * 0.7 + 130))
                pygame.display.update()
                kazu = pictureevent.picture((win_width / 4 - poker_w / 2, win_height / 2 - poker_h * 0.7), poker_size)
                # 生成放置区图像
                pygame.draw.rect(window, blue,
                                 (win_width * 0.75 - poker_w / 2, win_height / 2 - poker_h * 0.7, poker_w, poker_h))
                w2, h2 = text2.get_size()
                place_x, place_y = (win_width * 0.75 - poker_w / 2, win_height / 2 - poker_h * 0.7)
                window.blit(text2, (win_width * 0.75 - w2 / 2, win_height / 2 + poker_h * 0.3 + t + 5))
                window.blit(text, (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.7 + 10))
                pygame.display.update()
                # 生成男孩
                boy = pygame.image.load('pictures and font/boy.png')
                pw1, ph1 = boy.get_size()
                window.blit(boy, (lx, win_height - ly - ph1))
                w3, h3 = text4.get_size()
                window.blit(text4, (lx + pw1 / 2 - w3 / 2, win_height - ly + 5))
                pygame.display.update()
                # 生成女孩
                girl = pygame.image.load('pictures and font/girl.png')
                pw2, ph2 = girl.get_size()
                window.blit(girl, (win_width - lx - pw2, ly))
                w4, h4 = text3.get_size()
                window.blit(text3, (win_width - lx - pw2 / 2 - w4 / 2, 5))
                pygame.display.update()
                # 玩家1的手牌区
                window.blit(back1, (lx + t, 3 * t))
                p1_x1, p1_y1 = (lx + t, 3 * t)
                window.blit(back2, (lx + 3 * t + poker_w, 3 * t))
                p1_x2, p1_y2 = (lx + 3 * t + poker_w, 3 * t)
                window.blit(back3, (lx + 5 * t + poker_w * 2, 3 * t))
                p1_x3, p1_y3 = (lx + 5 * t + poker_w * 2, 3 * t)
                window.blit(back4, (lx + 7 * t + poker_w * 3, 3 * t))
                p1_x4, p1_y4 = (lx + 7 * t + poker_w * 3, 3 * t)
                window.blit(heitao, (lx + t + 30, 4 * t + poker_h + 5))
                window.blit(text6, (lx + t + 60, 4 * t + poker_h))
                window.blit(hongtao, (lx + 3 * t + poker_w + 30, 4 * t + poker_h + 5))
                window.blit(text5, (lx + 3 * t + poker_w + 60, 4 * t + poker_h))
                window.blit(meihua, (lx + 5 * t + poker_w * 2 + 30, 4 * t + poker_h + 5))
                window.blit(text6, (lx + 5 * t + poker_w * 2 + 60, 4 * t + poker_h))
                window.blit(fangkua, (lx + 7 * t + poker_w * 3 + 30, 4 * t + poker_h + 5))
                window.blit(text5, (lx + 7 * t + poker_w * 3 + 60, 4 * t + poker_h))
                # 玩家2的手牌区
                window.blit(back1, (win_width - lx - t - 1 * poker_w, win_height - 3 * t - poker_h))
                p2_x1, p2_y1 = (win_width - lx - t - 1 * poker_w, win_height - 3 * t - poker_h)
                window.blit(back2, (win_width - lx - 3 * t - 2 * poker_w, win_height - 3 * t - poker_h))
                p2_x2, p2_y2 = (win_width - lx - 3 * t - 2 * poker_w, win_height - 3 * t - poker_h)
                window.blit(back3, (win_width - lx - 5 * t - 3 * poker_w, win_height - 3 * t - poker_h))
                p2_x3, p2_y3 = (win_width - lx - 5 * t - 3 * poker_w, win_height - 3 * t - poker_h)
                window.blit(back4, (win_width - lx - 7 * t - 4 * poker_w, win_height - 3 * t - poker_h))
                p2_x4, p2_y4 = (win_width - lx - 7 * t - 4 * poker_w, win_height - 3 * t - poker_h)
                window.blit(heitao, (win_width - lx - t * 7 - poker_w * 4 + 30, win_height - 9 * t - poker_h - 5))
                window.blit(text6, (win_width - lx - t * 7 - poker_w * 4 + 60, win_height - 9 * t - poker_h - 15))
                window.blit(hongtao, (win_width - lx - t * 5 - poker_w * 3 + 30, win_height - 9 * t - poker_h - 5))
                window.blit(text5, (win_width - lx - t * 5 - poker_w * 3 + 60, win_height - 9 * t - poker_h - 15))
                window.blit(meihua, (win_width - lx - t * 3 - poker_w * 2 + 30, win_height - 9 * t - poker_h - 5))
                window.blit(text6, (win_width - lx - t * 3 - poker_w * 2 + 60, win_height - 9 * t - poker_h - 15))
                window.blit(fangkua, (win_width - lx - t - poker_w + 30, win_height - 9 * t - poker_h - 5))
                window.blit(text5, (win_width - lx - t - poker_w + 60, win_height - 9 * t - poker_h - 15))
                pygame.display.update()
                pygame.image.save(window, 'screen.png')
                begin_screen = pygame.image.load('screen.png')
                window.blit(kazu_n1, (30 + 70, win_height / 2 - poker_h * 0.7 + 5))
                window.blit(kazu_n2, (30 + 70, win_height / 2 - poker_h * 0.7 + 45))
                window.blit(kazu_n3, (30 + 70, win_height / 2 - poker_h * 0.7 + 85))
                window.blit(kazu_n4, (30 + 70, win_height / 2 - poker_h * 0.7 + 125))
                window.blit(placed_poker_num, (win_width * 0.75 + poker_w / 2 + t + 10, win_height / 2 - poker_h * 0.3))
                window.blit(p1_n1, (lx + t + 80, 4 * t + poker_h))
                window.blit(p1_n2, (lx + 3 * t + poker_w + 80, 4 * t + poker_h))
                window.blit(p1_n3, (lx + 5 * t + poker_w * 2 + 80, 4 * t + poker_h))
                window.blit(p1_n4, (lx + 7 * t + poker_w * 3 + 80, 4 * t + poker_h))
                window.blit(p2_n1, (win_width - lx - t * 7 - poker_w * 4 + 80, win_height - 9 * t - poker_h - 15))
                window.blit(p2_n2, (win_width - lx - t * 5 - poker_w * 3 + 80, win_height - 9 * t - poker_h - 15))
                window.blit(p2_n3, (win_width - lx - t * 3 - poker_w * 2 + 80, win_height - 9 * t - poker_h - 15))
                window.blit(p2_n4, (win_width - lx - t - poker_w + 80, win_height - 9 * t - poker_h - 15))
                x, y = text7.get_size()
                window.blit(text7, (win_width / 2 - x / 2, win_height / 2 - y))
                pygame.display.update()
                k11 = (place_x - p1_x1) / (place_y - p1_y1)
                k12 = (place_x - p1_x2) / (place_y - p1_y2)
                k13 = (place_x - p1_x3) / (place_y - p1_y1)
                k14 = (place_x - p1_x4) / (place_y - p1_y1)
                k21 = (place_x - p2_x1) / (place_y - p2_y1)
                k22 = (place_x - p2_x2) / (place_y - p2_y2)
                k23 = (place_x - p2_x3) / (place_y - p2_y3)
                k24 = (p2_x4 - place_x) / (place_y - p2_y4)
            # 游戏已开始
            if is_begin is True and kazudown is True:
                if kazu.move_placed_isup(event.pos, l0):
                    is_movplaced = True
                    kazudown = False
        # 检测点击打叉这个事件
        if event.type == pygame.QUIT:
            exit()
