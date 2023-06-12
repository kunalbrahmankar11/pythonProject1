class A:
    def a_fun(self):
        print("here we used the class A")

class B(A):
    def b_fun(self):
        print("here we used the class B")

object=B()
object.b_fun()
object.a_fun()