from base.View import *
from util.local import *
"""---------------------- 血量 ----------------------"""
class HP(View):
    def __init__(self,**kwargs,):
        super(HP, self).__init__(**kwargs,img='./img/enemymissile.gif')
        self.blood = kwargs['blood']
    def display(self):
        HpCentre = self.x+BLOCK_SIZE/2 - self.blood*16/2
        for ele in range(0,self.blood):

            self.window.blit(self.image,(HpCentre+ele*16,self.y-18))



