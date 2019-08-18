"""
具有攻击能力的控件父类(攻击力)
"""
class AttackAble:
    def hasCollision(self, sufferAble):
        """
        检测和阻挡控件的碰撞
        :param sufferAble: 具备受伤害能力的控件
        :return:
        """
        pass

    def notifyAttack(self):
        """
        通知攻击到了受伤害的控件
        :return:
        """
        pass