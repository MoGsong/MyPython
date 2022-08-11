import pygame
import sys
pygame.init()  #初始化
size = width, height = 600, 400  # 窗口大小
screen = pygame.display.set_mode(size)
pygame.display.set_caption('game')  # 程序名
bg = (50, 150, 155)    # 背景颜色 r g  b   白色（255, 255, 255）
# 背景图片
# bg = pygame.image.load('hzz.jpg')
# bgposition = bg.get_rect()
# 加载图片
img = pygame.image.load('z.jpg')
position = img.get_rect()   # 图片大小
speed = [1, 0]
while True:
    # 鼠标监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed = [2, 0]
            if event.key == pygame.K_LEFT:
                speed = [-2, 0]
            if event.key == pygame.K_UP:
                speed = [0, -2]
            if event.key == pygame.K_DOWN:
                speed = [0, 2]
        if event.type == pygame.KEYUP:
            speed = [0, 0]
    screen.fill(bg)   # 填充背景
    # screen.blit(bg, bgposition)
    position = position.move(speed)  # 图片移动
    screen.blit(img, position)
    pygame.display.flip()  # 触发
    pygame.time.Clock().tick(60)  # 控制移动速度


