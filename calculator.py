a=int(input("enter number a :\n"))
b=int(input("enter number b :\n"))

user_input=input(
    """enter your choice
      1.enter 1 to addition 
      2.enter 2 to substraction
      3.enter 3 to multiplication
      4.enter 4 to division
      """
    )

if user_input=="1":
    print("the addition of two numbers is",a+b)
elif user_input=="2":
    print("the substraction of two numbers is", a-b)
elif user_input=="3":
    print("the multipication of two numbers is", a*b)
elif user_input=="4":
    if b==0:
        print("division is not possible")
    else:
        print("the division of two numbers is", a/b)
else:
    print("invalid choice")

