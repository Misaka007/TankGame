"""
敌方坦克
"""
from base.View import *
from util.local import *

from base.AutoMoveAble import *
from base.MoveAble import *
from base.BlockAble import *
from random import *
from base.AutoFire import *
from views.Bullet import *
from base.SufferAble import *
from base.DestroyAble import *
import random
import time
from views.Blast import *
class EnemyTank(View, AutoMoveAble, MoveAble,AutoFire,BlockAble,SufferAble,DestroyAble):
    def __init__(self, **kwargs):
        super(EnemyTank, self).__init__(**kwargs, img='./img/p2tankD.gif')
        # 修改比较键
        self.comKey = 1
        # 所有的图片
        self.images = [
            pygame.image.load('./img/p2tankL.gif'),
            pygame.image.load('./img/p2tankR.gif'),
            pygame.image.load('./img/p2tankU.gif'),
            pygame.image.load('./img/p2tankD.gif')
        ]
        # 方向
        self.direction = Direction.DOWN
        # 移动速度
        self.speed = 0.2
        # 默认没有碰撞
        self.collision = False
        # 基准时间
        self.startTime = time.time()
        # 发射子弹的时间间隔
        self.limitTime = 1
        # 坦克血量
        self.blood = random.randint(3,7)
        self.image1 = pygame.image.load('./img/enemymissile.gif')
        #阵营属性
        self.camp = "Enemycamp"
    def randomDirection(self,direction):
        """
        随机获取方向
        :param direction:当前的碰撞方向,生成的方向需要不同于这个方向
        :return:
        """
        # 生成随机数0-3
        index = randint(0,3)
        newDirection = direction
        if index==0:
            newDirection = Direction.LEFT
        elif index==1:
            newDirection = Direction.RIGHT
        elif index==2:
            newDirection = Direction.UP
        elif index==3:
            newDirection = Direction.DOWN

        # 判断随机生成的方向是否和碰撞方向一致
        if newDirection==direction:
            # 如果一致,重新生成
            return self.randomDirection(direction)
        else:
            # 如果不一致,可以返回
            return newDirection

    def autoMove(self):
        # 判断是否发生碰撞
        if self.collision:
            self.collision = False
            # 随机换一个方向
            self.direction = self.randomDirection(self.direction)
            return
        # 没有碰撞可以移动
        if self.direction == Direction.UP:
            self.y -= self.speed
        elif self.direction == Direction.DOWN:
            self.y += self.speed
        elif self.direction == Direction.LEFT:
            self.x -= self.speed
        elif self.direction == Direction.RIGHT:
            self.x += self.speed

    def notifyCollision(self):
        # 发生碰撞
        self.collision = True

    def display(self):
        # 修改图片
        self.image = self.images[self.direction.value]
        # 显示
        self.window.blit(self.image,(self.x,self.y))



    def autoFire(self):
        # 10 12
        """控制发射频率 1秒钟一次"""
        # 当前时间
        curTime = time.time()
        # 时间差
        offsetTime = curTime-self.startTime
        if offsetTime>self.limitTime:
            # 修改基准时间
            self.startTime = curTime
            # 阵营（cmap）:敌方（Enemycamp）
            return Bullet(camp="Enemycamp",tank_x=self.x, tank_y=self.y, tank_width=self.width, tank_height=self.height, window=self.window,
                          direction=self.direction)

    def notifySuffer(self,attackAble):
        # 判断是否是友军
        # if not isinstance(attackAble.owner,EnemyTank):
        self.blood -= 1

    def needDestroy(self):
        return self.blood<=0

        # 爆炸效果
    def showDestroy(self):
            # center_x = bx + bw / 2
            # center_y = by + bh / 2
            return Blast(center_x=self.x + self.width / 2, center_y=self.y + self.height / 2, window=self.window)