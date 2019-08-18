"""
View是可以显示的控件
是所有控件的父类
"""
import pygame
class View:
    def __init__(self,**kwargs):
        """
        传任何类型
        :param kwargs:
        """
        self.camp = "NeutralCamp"
        # 默认比较键
        self.comKey = 2
        # 坐标
        self.x = kwargs['x']
        self.y = kwargs['y']
        # 图片Surface
        self.image = pygame.image.load(kwargs['img'])
        # window
        self.window = kwargs['window']
        # 宽度和高度
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.blood = 0
    def display(self):
        self.window.blit(self.image,(self.x,self.y))

