class Dog(object):
    def __init__(self,name):
        self.name=name

    @staticmethod
    def eat(food):
        print("I wanna eat %s"%(food))

Dog.eat("banana")
