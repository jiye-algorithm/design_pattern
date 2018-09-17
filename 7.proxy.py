'''
代理人代理幕后好对象交互，但是实际动作的发出者是幕后。
'''
import abc


class GiveGift:
    '''
    抽象接口
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, sg):
        """init"""
        pass

    @abc.abstractmethod
    def give_dolls(self):
        """give dolls"""
        pass

    @abc.abstractmethod
    def give_flowers(self):
        """give flowers"""
        pass


class SchoolGirl:
    def __init__(self, n):
        self.name = n
        pass
    pass


class Pursuit(GiveGift):
    '''
    幕后
    '''
    def __init__(self, sg):
        GiveGift.__init__(self, sg)
        self.school_girl = sg
        pass

    def give_dolls(self):
        print("give " + self.school_girl.name + " dolls")
        pass

    def give_flowers(self):
        print("give " + self.school_girl.name + " flowers")
        pass


class Proxy(GiveGift):
    '''
    代理
    '''
    def __init__(self, sg):
        GiveGift.__init__(self, sg)
        self.pursuit = Pursuit(sg)

    def give_dolls(self):
        self.pursuit.give_dolls()

    def give_flowers(self):
        self.pursuit.give_flowers()
        pass
    pass


if __name__ == "__main__":
    # 对象
    school_girl = SchoolGirl("Alice")
    # 代理人，
    proxy = Proxy(school_girl)
    proxy.give_flowers()
    proxy.give_dolls()
