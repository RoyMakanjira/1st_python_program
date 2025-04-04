#  Roy the Makanjira calculater
def subtraction(r , y):
    return r - y

def addition(r , y):
    return r + y

def multiplication(r , y):
    return r * y

def division(r , y):
    if y == 0:
     return "it can't ERROR !!!"
    return r / y

print("How do you want to calculate")
print("1. Subtraction")
print("2. Addition")
print("3.Multiplication")
print("4.Division")

choice = input("Enter How you want to calculate (1/2/3/4): ")

number_1 = int(input("Put the first number"))
number_2 = int(input("put the second number"))

if choice == "1":
   print(f"the result is: {subtraction(number_1,number_2)} ")
elif choice == "2":
   print(f"the result is: {addition(number_1,number_2)} ")

elif choice == "3":
   print(f"the result is :{multiplication(number_1,number_2)}")
elif choice == "4":
   print(f"the result is : {division(number_1,number_2)}")
else:
   print("invalid !!!!!!!!!!!!!")


# def greet():
#       print("Hello Rooooooooooooooy ")
# greet()

# def greet(name , surname):
#       print(f"hie {name} {surname}")
# greet("Roy","Makanjira") 