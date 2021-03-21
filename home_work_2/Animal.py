# -*- coding: utf-8 -*-
import yaml


class Animal:

    def __init__(self, n, c, a, g):
        self.name = n
        self.color = c
        self.age = a
        self.gender = g

    def call(self):
        print("动物会叫")

    def run(self):
        print("动物会跑")


class Cat(Animal):
    hair = "shorthair"

    def __init__(self, n, c, a, g, ):
        Animal.__init__(self, n, c, a, g)


    def catch(self):
        print("猫捉老鼠了")

    def call(self):
        print("猫会喵喵叫")


class Dog(Animal):
    hair = 'longhair'

    def __init__(self, n, c, a, g):
        Animal.__init__(self, n, c, a, g)


    def keep(self):
        print("狗在看家")

    def call(self):
        print("狗会汪汪叫")


# def print_obj(obj):
#     print(obj.__dict__)


if __name__ == '__main__':
    with open("data.yaml.")as f:
        datas = yaml.safe_load(f)
        data1 = datas["cat1"]
        data2 = datas["dog1"]
    cat1 = Cat(data1[0], data1[1], data1[2], data1[3])
    print(data1)
    cat1.call()
    cat1.catch()
    dog1 = Dog(data2[0], data2[1], data2[2], data2[3])
    print(data2)
    dog1.call()
    dog1.keep()
