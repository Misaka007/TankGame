from base.View import *
from util.local import *
from base.AutoMoveAble import *
from base.DestroyAble import *
from base.AttackAble import *
from base.SufferAble import *
from views.Blast import *
import pygame

class Bullet(View,AutoMoveAble,DestroyAble,AttackAble,SufferAble):
    def __init__(self, **kwargs):
        # 子弹阵营
        self.camp = kwargs['camp']
        # 是否需要销毁
        self.shouldDestroy = False
        # 定义自动移动速度
        self.speed = 1
        # 获取方向属性
        self.direction = kwargs['direction']
        # 获取坦克属性
        tank_x = kwargs['tank_x']
        tank_y = kwargs['tank_y']
        tank_width = kwargs['tank_width']
        tank_height = kwargs['tank_height']
        # window
        self.window = kwargs['window']
        # 子弹图片
        self.image = pygame.image.load('./img/tankmissile.gif')
        # 宽度和高度
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.blood=0
        # x和y
        if self.direction == Direction.UP:
            self.x = tank_x + tank_width / 2 - self.width / 2
            self.y = tank_y - self.height
        elif self.direction == Direction.DOWN:
            self.x = tank_x + tank_width / 2 - self.width / 2
            self.y = tank_y + tank_height
        elif self.direction == Direction.LEFT:
            self.x = tank_x - self.width
            self.y = tank_y + tank_height / 2 - self.height / 2
        elif self.direction == Direction.RIGHT:
            self.x = tank_x + tank_width
            self.y = tank_y + tank_height / 2 - self.height / 2

    def autoMove(self):
        if self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed
        elif self.direction == Direction.LEFT:
            self.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed

    def needDestroy(self):
        # 子弹越界
        return (self.x<0 or self.y<0 or self.x>WINDOW_WIDTH or self.y>WINDOW_HEIGHT) or self.shouldDestroy

    def hasCollision(self, sufferAble):
        # 坦克矩形(下一步的轨迹)
        bulletRect = pygame.Rect(self.x, self.y, self.width, self.height)
        # 砖墙矩形
        sufferRect = pygame.Rect(sufferAble.x, sufferAble.y, sufferAble.width, sufferAble.height)
        # 边界碰撞结果
        return bulletRect.colliderect(sufferRect)

    def notifyAttack(self):
        self.shouldDestroy = True
    # 爆炸
    def showDestroy(self):

        return Blast(center_x=self.x + self.width / 2, center_y=self.y + self.height / 2, window=self.window)