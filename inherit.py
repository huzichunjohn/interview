class A(object):
    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B, C):
    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")

class E(B, C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

print("#"*20)
a.go()
print("#"*20)
b.go()
print("#"*20)
c.go()
print("#"*20)
d.go()
print("#"*20)
e.go()
print("#"*20)

print("#"*20)
a.stop()
print("#"*20)
b.stop()
print("#"*20)
c.stop()
print("#"*20)
d.stop()
print("#"*20)
e.stop()
print("#"*20)

print("#"*20)
#a.pause()
print("#"*20)
#b.pause()
print("#"*20)
#c.pause()
print("#"*20)
d.pause()
print("#"*20)
#e.pause()
print("#"*20)
