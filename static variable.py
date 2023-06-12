# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# b=student("kunal",19)
# print(b.name,b.age)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# object=person("kunal",19)
# print(object.name)

# class person:
#     people="hungry"  #class variable
#     def __init__(self):
#         self.name="krunal"
#     def show_m(self):
#         print(self.name)
#     @classmethod
#     def now(cls):  #class method
#          cls.people  #accsesing class variable inside class method
# obj=person()
# print(obj.people)
# print(obj.name)

# class car:
#     def __init__(self):
#         self.name="bmw"
#     def vehicle(self):
#         print("the car is awesome",self.name)
# obj=car()
# print(obj.name)
# print(obj.vehicle())


class person:
    def __init__(self):
        self.name="kunal"
object=person()
print(object.name)