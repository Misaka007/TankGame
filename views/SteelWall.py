"""
铁墙
"""
from base.BlockAble import *
from base.View import *
from base.SufferAble import *

class SteelWall(View,BlockAble,SufferAble):
    def __init__(self,**kwargs):
        super(SteelWall, self).__init__(**kwargs,img='./img/steels.gif')
