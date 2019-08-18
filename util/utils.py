from views.HeroTank import HeroTank
from views.GrassWall import GrassWall
from views.WaterWall import WaterWall
from views.BrickWall import BrickWall
from views.SteelWall import SteelWall
from views.EnemyTank import EnemyTank
from util.local import *
from views.Fortress import *

def parseMap(path, window, views):
    # 解析地图
    file = open(path, encoding='utf-8')
    # 全部读取
    lines = file.readlines()
    # 遍历每一行
    for row in range(0, len(lines)):
        line = lines[row]
        # 获取每一行字符
        for col in range(0, len(line)):
            str = line[col]
            if str == '主':
                # 创建我方坦克
                views.append(HeroTank(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window,direction=Direction.UP))
            elif str == '堡':
                views.append(Fortress(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str == '草':
                views.append(GrassWall(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str == '水':
                views.append(WaterWall(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str == '铁':
                views.append(SteelWall(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str=='砖':
                views.append(BrickWall(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))
            elif str=='敌':
                views.append(EnemyTank(x=col * BLOCK_SIZE, y=row * BLOCK_SIZE, window=window))

    # 列表排序(坦克放到前面)
    views.sort(key=lambda view:view.comKey)