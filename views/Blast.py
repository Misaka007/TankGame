"""
爆炸物
"""
from base.View import *
from base.DestroyAble import *
import pygame


class Blast(View, DestroyAble):
    def __init__(self, **kwargs):
        # 获取中心点的x和y
        center_x = kwargs['center_x']
        center_y = kwargs['center_y']
        # 图片的index
        self.index = 1
        # 图片总数
        self.total = 32
        # 当前图片
        self.image = pygame.image.load('./img/blast_{}.png'.format(self.index))
        # 宽度和高度
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # x和y坐标
        self.x = center_x - self.width / 2
        self.y = center_y - self.height / 2
        # 获取window
        self.window = kwargs['window']

    def display(self):
        # 当前图片
        self.image = pygame.image.load('./img/blast_{}.png'.format(self.index))
        # 显示图片
        super(Blast, self).display()
        # 换图片
        if self.index < self.total:
            self.index += 1

    def needDestroy(self):
        return self.index == 32
