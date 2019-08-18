"""
草
"""
from base.BlockAble import *
from base.View import *


class WaterWall(View,BlockAble):
    def __init__(self,**kwargs):
        super(WaterWall, self).__init__(**kwargs,img='./img/water.gif')
