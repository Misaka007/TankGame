import pygame
from pygame.locals import *
from util.utils import *
from base.BlockAble import *
from base.MoveAble import *
from base.AutoMoveAble import *
from base.DestroyAble import *
from base.AttackAble import *
from base.SufferAble import *
from base.AutoFire import *
from views.Hp import *
import sys

# 保存界面上所有需要显示的控件


def start():

    # 初始化游戏
    pygame.init()
    # 显示窗口
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 修改游戏标题和图片
    pygame.display.set_caption("坦克大战")
    # 修改图标
    iconImage = pygame.image.load('./img/camp.gif')
    # 设置图标
    pygame.display.set_icon(iconImage)
    while True:
        views = []
        # 加载地图
        parseMap('./map/1.map', window, views)

        # 获取坦克
        tank = list(filter(lambda view: isinstance(view, HeroTank), views))[0]

        # 定义结束文字
        font = pygame.font.Font('./font/happy.ttf', 50)

        overFont = font.render("""失败了   按“Y”重新开始""", True, (255, 0, 0))
        # 字体宽度和高度
        fontWidth = overFont.get_width()
        fontHeight = overFont.get_height()

        overFont1 = font.render("""胜利了   按“Y”重新开始""", True, (0, 0, 255))
        # 字体宽度和高度
        fontWidth1 = overFont1.get_width()
        fontHeight1 = overFont1.get_height()

        # 死循环控制程序不退出
        while True:
            # 检测是否游戏停止
            # 敌方坦克列表
            EnemyTankList = list(filter(lambda view: isinstance(view, EnemyTank), views))
            # 我方坦克列表
            HeroTankList = list(filter(lambda view: isinstance(view, HeroTank), views))
            # 我方堡垒列表
            FortresskList = list(filter(lambda view: isinstance(view, Fortress), views))
            if len(EnemyTankList)*len(HeroTankList)*len(FortresskList) == 0:
                # 显示结束文字
                if len(EnemyTankList)==0:
                    window.blit(overFont1, (WINDOW_WIDTH / 2 - fontWidth1 / 2, WINDOW_HEIGHT / 2 - fontHeight1 / 2))
                else:
                    window.blit(overFont, (WINDOW_WIDTH / 2 - fontWidth / 2, WINDOW_HEIGHT / 2 - fontHeight / 2))
                # 刷新
                pygame.display.flip()

                break

            # 检测自动发射的子弹
            autoFireList = list(filter(lambda view: isinstance(view, AutoFire), views))
            for autoFire in autoFireList:
                bullet = autoFire.autoFire()
                # 子弹发射有可能空弹
                if bullet:
                    # 添加到列表中
                    views.append(bullet)

            # 阵营判断
            # 攻与受检测
            # 所有具有攻击能力的控件
            attackList = list(filter(lambda view: isinstance(view, AttackAble), views))
            sufferList = list(filter(lambda view: isinstance(view, SufferAble), views))
            for attack in attackList:
                for suffer in sufferList:
                    # 判断阵营
                    if not attack.camp==suffer.camp:
                         # 检测碰撞
                        collision = attack.hasCollision(suffer)
                        # 如果攻击到了,通知攻击和受攻击的控件
                        if collision:
                            # 通知攻击者
                            attack.notifyAttack()
                            # 通知受伤害者
                            suffer.notifySuffer(attack)
                            break


            # 找到可能被销毁的控件
            destroyList = list(filter(lambda view: isinstance(view, DestroyAble), views))
            # 看每一个有可能被销毁的控件是否现在需要被销毁
            for destroyView in destroyList:
                if destroyView.needDestroy():
                    # 是否需要显示挂掉特效
                    destroyResult = destroyView.showDestroy()
                    if destroyResult:
                        views.append(destroyResult)

                    # 移除列表
                    views.remove(destroyView)
                    # 内存置为不可用
                    del destroyView

            # 处理自动移动
            # 获取所有自动移动的控件
            autoMoveList = list(filter(lambda view: isinstance(view, AutoMoveAble), views))
            for autoMove in autoMoveList:
                autoMove.autoMove()

            # 运动和阻挡碰撞检测
            # 运动的控件
            moveList = list(filter(lambda view: isinstance(view, MoveAble), views))
            # 阻挡的控件
            blockList = list(filter(lambda view: isinstance(view, BlockAble), views))
            # 运动和阻挡碰撞检测
            for move in moveList:
                for block in blockList:
                    # 如果是和自己碰撞,跳过去
                    if move == block:
                        continue
                    # 碰撞检测
                    collison = move.hasCollision(block)
                    if collison:
                        # 发生了碰撞
                        # 通知运动控件发生了碰撞
                        move.notifyCollision()
                        # 通知阻挡控件发生了碰撞
                        block.notifyCollision()
                        break



            # 清除窗口上的画面
            window.fill((0, 0, 0))
            # 显示
            # 显示坦克的血量
            # 敌方坦克列表
            for suffer1 in EnemyTankList + HeroTankList:
                hp=HP(x=suffer1.x,y=suffer1.y,blood=suffer1.blood,window=window)
                hp.display()
            # 显示所有的控件
            for view in views:
                view.display()
            # 显示非坦克的血量
            sufferList1 = list(filter(lambda view: isinstance(view, SufferAble), views))
            for suffer1 in sufferList1 :
                if not (suffer1 in HeroTankList or suffer1 in EnemyTankList):
                    hp=HP(x=suffer1.x,y=suffer1.y,blood=suffer1.blood,window=window)
                    hp.display()
            # 刷新
            pygame.display.flip()

            # 处理事件
            eventList = pygame.event.get()
            # 遍历事件
            for eventEle in eventList:
                if eventEle.type == QUIT:
                    # 退出游戏界面
                    pygame.quit()
                    # 退出程序
                    sys.exit()
                elif eventEle.type == KEYDOWN:
                    if eventEle.key == K_SPACE:
                        # 发生子弹
                        views.append(tank.fire())

            # 获取按压事件
            status = pygame.key.get_pressed()
            # 盘算是否有按键按压
            if 1 in status:
                # 有按键按压
                if status[K_LEFT]:
                    tank.move(Direction.LEFT)
                elif status[K_RIGHT]:
                    tank.move(Direction.RIGHT)
                elif status[K_UP]:
                    tank.move(Direction.UP)
                elif status[K_DOWN]:
                    tank.move(Direction.DOWN)

        status = True
        while status:
            # 处理事件
            eventList = pygame.event.get()
            # 遍历事件
            for eventEle in eventList:
                if eventEle.type == QUIT:
                    # 退出游戏界面
                    pygame.quit()
                    # 退出程序
                    sys.exit()
                elif eventEle.type == KEYDOWN:
                    if eventEle.key == K_y:
                        # 发生子弹
                        status = False


if __name__ == '__main__':
    start()
