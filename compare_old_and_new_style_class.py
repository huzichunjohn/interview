#/usr/bin/env python
# -*- coding: utf-8 -*-

# class D:
#     def go(self):
#         print "go D go!"
#
# class C(D):
#     def go(self):
#         D.go(self)
#         print "go C go!"
#
# class B(D):
#     def go(self):
#         D.go(self)
#         print "go B go!"
#
# class A(B, C):
#     def go(self):
#         B.go(self)                     # 显式调用
#         C.go(self)
#         print "go A go!"
#
# a = A()
# a.go()

# output:
# go D go!        1 time
# go B go!
# go D go!        2 time
# go C go!
# go A go!

# class D(object):
#     def go(self):
#         print "go D go!"
#
# class C(D):
#     def go(self):
#         super(C, self).go()
#         print "go C go!"
#
# class B(D):
#     def go(self):
#         super(B, self).go()
#         print "go B go!"
#
# class A(B, C):
#     def go(self):
#         super(A, self).go()        # super
#         print "go A go!"
#
# a = A()
# a.go()

# output:
# go D go!
# go C go!
# go B go!
# go A go!

# 旧式类
# class D:
#     def __init__(self):
#         self.value = 1
#
# class C(D):
#     def __init__(self):
#         self.value = 2
#
# class B(D):
#     pass
#
# class A(B, C):
#     pass
#
# a = A()
# print a.value

# 新式类
class D(object):
    def __init__(self):
        self.value = 1

class C(D):
    def __init__(self):
        self.value = 2

class B(D):
    pass

class A(B, C):
    pass

a = A()
print a.value
