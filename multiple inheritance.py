class A:
    def fun_a(self):
        print("this is base class A")
class B:
    def fun_b(self):
        print("this is base class B")
class C(A,B):
    def fun_c(self):
        print("this is deived class from class A and class B")

object=C()
object.fun_a()
object.fun_c()
object.fun_b()