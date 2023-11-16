class A():
    def hablar(self):
        print("A")
        
class F(A):
    def hablar(self):
        print("F")
class B(A):
    def hablar(self):
        print("B")

class C(F):
    def hablar(self):
        print("C")

class D(B,C):
    pass    
d=D()
d.hablar()
"D-B-C-F-A"