"""---------------------- 主程序 ----------------------"""
import pygame
from pygame.locals import *
from util.local import *
import sys


def start():
    # 初始化游戏
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 修改游戏标题和图片
    pygame.display.set_caption("坦克大战")
    # 修改图标
    iconImage = pygame.image.load("./img/camp.gif")
    # 设置图标
    pygame.display.set_icon(iconImage)
    # 死循环控制程序不退出
    while True:
        # 处理事件
        eventList = pygame.event.get()
        for eventEle in eventList:
            if eventEle.type == QUIT:
                # 退出游戏界面
                pygame.quit()
                # 退出程序
                sys.exit()


if __name__ == '__main__':
    start()
