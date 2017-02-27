#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 元类
# class Singleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
# class Foo(object):
#     __metaclass__ = Singleton
#
# class Bar(object):
#     __metaclass__ = Singleton

# 继承
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = object.__new__(cls, *args, **kwargs)
#         return cls._instance
#
# class Foo(Singleton):
#     pass
#
# class Bar(Singleton):
#     pass

# 装饰器
def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class Foo(object):
    pass

@singleton
class Bar(object):
    pass

if __name__ == "__main__":
    foo1 = Foo()
    foo2 = Foo()
    print id(foo1) == id(foo2)

    bar1 = Bar()
    bar2 = Bar()
    print id(bar1) == id(bar2)
