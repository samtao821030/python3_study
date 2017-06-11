class Dog(object):
    def __init__(self):
        pass

    def eat(self,food):
        print("狗开始吃%s啦！"%(food))


d=Dog()

choice = input(">>:").strip()

print(hasattr(d,choice))
print(getattr(d,choice)("香蕉"))