class A:
    def a_fun(self):
        print("here we used the class A")

class B(A):
    def b_fun(self):
        print("here we used the class B")

class C(A):
    def c_fun(self):
        print("here we used the class C")
class D(A):
    def d_fun(self):
        print("here we used class D")

object=B()
object.b_fun()
object=C()
object.c_fun()
object=D()
object.d_fun()
object=A()
object.a_fun()