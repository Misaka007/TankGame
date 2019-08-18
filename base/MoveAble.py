"""
具备运动能力的控件
"""
from util.local import *
import pygame

class MoveAble:
    def hasCollision(self, blockAble):
        """
        检测和阻挡控件的碰撞
        :param blockAble: 具备阻挡能力的控件
        :return:
        """
        # 记录当前的x和y
        x = self.x
        y = self.y
        # 预判下一步轨迹
        if self.direction == Direction.UP:
            y -= self.speed
        elif self.direction == Direction.DOWN:
            y += self.speed
        elif self.direction == Direction.LEFT:
            x -= self.speed
        elif self.direction == Direction.RIGHT:
            x += self.speed

        # 坦克矩形(下一步的轨迹)
        tankRect = pygame.Rect(x, y, self.width, self.height)
        # 砖墙矩形
        blockRect = pygame.Rect(blockAble.x, blockAble.y, blockAble.width, blockAble.height)
        # 边界碰撞结果
        return (tankRect.colliderect(blockRect)) or (
                x < 0 or y < 0 or y > WINDOW_HEIGHT - self.height or x > WINDOW_WIDTH - self.width)

    def notifyCollision(self):
        """
        通知发生了碰撞
        :return:
        """
        pass