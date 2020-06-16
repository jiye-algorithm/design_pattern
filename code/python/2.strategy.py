'''
策略模式
用策略封装一个一个的算法，利用继承和多态的思路，统一接口
'''

import abc


class CashSuper:
    # Python本身不提供抽象类和接口机制，要想实现抽象类，可以借助abc模块。ABC是Abstract Base Class的缩写。
    __metaclass__ = abc.ABCMeta

    # 子类必须实现
    @abc.abstractmethod
    def accept_cash(self, c):
        """caculate cash"""
        pass

# 正常要价
class CashNormal(CashSuper):
    def accept_cash(self, c):
        return c

# 打折
class CashRebate(CashSuper):
    def __init__(self, r):
        self.rebate = r
        pass

    def accept_cash(self, c):
        return c * self.rebate

    pass

# 满减
class CashReturn(CashSuper):
    def __init__(self, c, r):
        self.condition = c
        self.money = r
        pass

    def accept_cash(self, c):
        return c - int(c / self.condition) * self.money

    pass

# 利用工厂封装上下文信息
class CashContext:
    def __init__(self, t, s):
        self.cash = None
        if t == "normal":
            self.cash = CashNormal()
        elif t == "rebate":
            self.cash = CashRebate(float(s))
        elif t == "return":
            args = s.split(' ')
            self.cash = CashReturn(float(args[0]), float(args[1]))
            pass
        pass

    def get_result(self, c):
        return self.cash.accept_cash(c)

    pass


if __name__ == "__main__":
    cash_context = CashContext("normal", "")
    print(cash_context.get_result(1000))

    cash_context = CashContext("rebate", "0.8")
    print(cash_context.get_result(1000))

    cash_context = CashContext("return", "300 100")
    print(cash_context.get_result(1000))

    pass

