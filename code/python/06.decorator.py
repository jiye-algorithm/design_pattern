'''
装饰模式

装饰模式是利用set_component来对对象进行包装的。这样每个装饰对象的实现就和如何使用这个对象分离开了，
每个装饰对象值关心自己的功能，不需要关心如何被添加到对象链当中。
'''


class Person:
    def show(self):
        print("person")
        pass
    pass

# 用服饰装饰人
class Finery(Person):
    def __init__(self, c):
        # 用服饰装饰的对象
        self.component = c
        pass

    def show(self):
        """finery show"""
        pass
    pass


class Tie(Finery):
    def show(self):
        print("tie ",)
        self.component.show()
        pass
    pass


class Suit(Finery):
    def show(self):
        print( "suit ",)
        self.component.show()
        pass
    pass


class Shoes(Finery):
    def show(self):
        print("shoes ",)
        self.component.show()
        pass
    pass


if __name__ == "__main__":

    # 对象
    person = Person()
    # 装饰过程
    tie = Tie(person)
    suit = Suit(tie)
    shoes = Shoes(suit)
    shoes.show()
