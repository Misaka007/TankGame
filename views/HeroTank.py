"""
我方坦克
"""
from base.MoveAble import *
from views.Bullet import *
from base.BlockAble import *
from base.SufferAble import *
from base.DestroyAble import *
from views.Blast import *
class HeroTank(View, MoveAble,BlockAble,SufferAble,DestroyAble):
    def __init__(self, **kwargs):
        # 坦克移动速度
        self.speed = 0.5
        # 获取坦克方向
        self.direction = kwargs['direction']
        # 保存所有方向的图片Sufface
        self.images = [
            pygame.image.load('./img/p1tankL.gif'),
            pygame.image.load('./img/p1tankR.gif'),
            pygame.image.load('./img/p1tankU.gif'),
            pygame.image.load('./img/p1tankD.gif')
        ]
        super(HeroTank, self).__init__(**kwargs, img='./img/p1tankL.gif')
        # 修改比较键
        self.comKey = 1
        # 获取坦克需要显示的图片
        self.image = self.images[self.direction.value]
        # 是否碰撞属性
        self.collision = False
        # 我方坦克血量
        self.blood = 10
        # 阵营属性
        self.camp="Ourcamp"
        for ele in range(1,self.blood):
            self.window.blit(self.image,(self.x+ele*16,self.y))

    def display(self):
        # 修改显示的图片
        self.image = self.images[self.direction.value]
        # 父类的display
        super(HeroTank, self).display()

    def move(self, direction):
        """
        移动坦克,修改坦克坐标
        :param direction:Direction枚举类型
        :return:
        """
        # 如果移动的方向和原来的方向不一致,需要先换方向
        if self.direction != direction:
            # 改变方向
            self.direction = direction
            return

        # 判断有没有发生碰撞,如果发生碰撞,就return
        if self.collision:
            self.collision = False
            return
        # 移动
        if direction == Direction.UP:
            self.y -= self.speed
        elif direction == Direction.DOWN:
            self.y += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.RIGHT:
            self.x += self.speed

    def notifyCollision(self):
        """
        通知发生了碰撞,坦克停下来
        :return:
        """
        self.collision = True

    def fire(self):
        """
        发射子弹(创建子弹对象 添加到views,显示到界面上)
        :return:
        """
        # 坦克的x和y   宽度和高度  子弹的宽度和高度
        #阵营（cmap）:我方（Ourcamp）
        return Bullet(camp="Ourcamp",tank_x=self.x, tank_y=self.y, tank_width=self.width, tank_height=self.height, window=self.window,
                      direction=self.direction)
    #受攻击通知
    def notifySuffer(self,attackAble):
         self.blood -= 1

    def needDestroy(self):
        return self.blood<=0

    # 爆炸效果
    def showDestroy(self):
        # center_x = bx + bw / 2
        # center_y = by + bh / 2
        return Blast(center_x=self.x+self.width/2,center_y=self.y+self.height/2,window=self.window)