class Dog(object):
    def __init__(self,name):
        self.name=name

    @property
    def run(self):
        print("我开始跑了！！")

d=Dog("haha")
d.run