class A:
    def a_class(self):
        print("This is a base class A")
class B:
    def b_class(self):
        print("This is a base class B")
class C(B):
    def c_class(self):
        print("This is a derived class from B")

class D(A,C):
    def d_class(self):
        print("This is a derived class from base class A and derived class C")

object=D()
object.a_class()
object.b_class()
object.d_class()
object.c_class()
