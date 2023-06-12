class A:
    def a_fun(self):
        print("here we used the class A")

class B(A):
    def b_fun(self):
        print("here we used the class B")

class C(B):
    def c_fun(self):
        print("here we used the class C")

object=C()
object.a_fun()
object.b_fun()
object.c_fun()