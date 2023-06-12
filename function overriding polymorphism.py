# class car:
#     def fun(self,name=''):
#         print("welcome to swastik motor = "+name)
# obj=car()
# obj.fun()
# obj.fun("BMW")

class Name:
    def first_name(self):
        print("My first name is kunal")
class Last(Name):
    def first_name(self):
        super().first_name() #using super function we called the base class function having same name
        print("My Last name is Brahmankar ")

object=Last()
object.first_name()