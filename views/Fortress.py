"""
砖墙
"""
import pygame
from base.View import *
from base.BlockAble import *
from base.SufferAble import *
from base.DestroyAble import *
from views.Blast import *
# 堡垒
class Fortress(View,BlockAble,SufferAble,DestroyAble):
    def __init__(self,**kwargs):
        super(Fortress, self).__init__(**kwargs,img='./img/camp.gif')
        # 血量值
        self.blood = 3
        # 阵营属性
        self.camp = "Ourcamp"
    def notifySuffer(self,attackAble):
        # 减少血量
        self.blood -= 1

    def needDestroy(self):
        return self.blood<=0

    def showDestroy(self):
        # center_x = bx + bw / 2
        # center_y = by + bh / 2
        return Blast(center_x=self.x+self.width/2,center_y=self.y+self.height/2,window=self.window)
