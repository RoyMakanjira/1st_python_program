# # How to print Something in python
# print("Hello and welcome to Wayne Exercise")
# print("Wayne is one of the Greatest Instructors World wide")
print("welcome to Takunda Muraicho website")
print("hello 123")
# list
uncommon = ["wesly","anna","lyncia","elsie","wayne"]
print(uncommon[0])
print(uncommon[0:3])
print(type(uncommon))



#  Variables
#  strings
name = ("Roy Makanjira")
school = ("uncommon.org")
country = ("Zimbabwe") 
city = ("Harare")

# type casting
print(type(school))

# # integers
age = 22
grade = 7
house_number = 11154 
# type casting
print(type(house_number))

# floats 
Height = 1.25
litres = 2.75
university_grade =2.1
# f strings - these are strings which include variable in it
print(f"hello my name is {name} , i am {age} years of age and also am {Height} meters long. I live at house number{house_number} in {city} the capital city of {country}. I was very privilleged to go {school}")


 #  if statements

first_born = "Brian"
second_born = "ROY"

if first_born == first_born:
    print("you are the first born")
else: print("you are not the first born")

first_born = input("can you give me the name of the first  born child")
second_born = input("can you give me the name of the second born")

if first_born == first_born:
    print("you are not the first born")
else:
    print("you are the first born") 
# input
# name = input("what is your name ")
# girlfriend = input("who i your girlfriend")
# Makore = int(input("How old are you again  "))

# if Makore <=15:
#     print("you are too young to be doing python")
# elif Makore == 0:
#     print("Sorry you haven't been born yet")
# elif Makore >=100:
#      print("you are too old to be doig python")
# else:
#     print("You are doing the right thing now")

# list 
favourite_people = ["Mhamha","Mdara","Siblings","Taku and his Family","Natalie and the uncommon family"]
print(favourite_people)
print(favourite_people[-1])
favourite_people.sort
print(favourite_people[1::3])

#  how to print elements in a list as a list

for person in favourite_people:
    print(person)

# the insert and append method
favourite_people.append(["steph curry","lionel messi"])
print(favourite_people)
# favourite_people.pop([0])
print(favourite_people)


#  while loops 

# pin = input("put your security pin :  ")

# while pin == 2030:
#      print("you gave us the correct pin")
#      break
# if pin == "":
#      print("you did not type in your pin ")
# elif pin != 2030:
#      print("the pin is correct")
# else:
#      print("you don't know your pin munhu waMwari")

     # tuples
fives =(5,10,15,20,25)
tens = (10,20,30,40,50)
print(fives + tens)
print(fives *2)
print(len(fives and tens))

numbers = (1,2,3,4,5)
print(len(numbers))
numbers = list(numbers)

numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers)
numbers = list(numbers)
numbers.sort
print(numbers)
numbers.sort(reverse="True")
print(numbers)

a = 6
b = 5

print(a==b)

if (a==6) :
 print("you are correct" ),
elif (a<6):
   print("you are stupid")
else:
     print("you are wrong")

# sets
     print(type(a))
my_set = {1,2,3,4,5}
my_set2 = {6,7,8,9,10}



union_set= my_set | my_set2
print(union_set)
 
union_set= my_set | my_set2
# or
union_set = my_set.union(my_set2)
print(union_set)
 
int_set = my_set.intersection(my_set2) 
print(int_set)

# dictionaries
my_family = {"father" : "Draymond","Mother" : "Hilarity", "first_child" : "Star", "second_child":"Roy"}
print(my_family)
print(my_family.get("second_child"))
my_family.update({"third_born" : "tanaka"})
print(my_family)
# my_family.pop("third_born")
print(my_family)

#  revision on pain points
#  Dictinary
main_actors = {"Rambo" : "Silvester Stalon", "charm city kings " : " Meek mill" , "Friday" : "Ice cube"}
print(main_actors.get("Friday"))
# print(main_actors.clear()) 
main_actors.update({"Madea" : "Tyler Perry"})
print(main_actors)

# sets
Pcolours = {"red","blue","purple","green"}
Scolours = ("army green", "sky blue", "navy blue")
union_set = Pcolours.union(Scolours)

print(union_set)
# Pcolours.sort({})
print(union_set)

#Integers

age= 23
quantity= 3
num_of_students= 40
print(f"You are {age}years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")




#Integer operations


a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

#Converting other types to Integers

print(int(3.9))
print(int("100"))

#Dictionary
my_dict= {"name": "Roy",
          "age": 22,
          "city": "Harare"}

print(my_dict)

#Accessing values

print(my_dict["name"])
print(my_dict.get("age"))



#Adding & Updating Values

my_dict["email"]= "roymakanjira@mail.com"
my_dict["age"]= 25

print(my_dict)

#Removing Elements

my_dict.pop("city")
del my_dict["age"]
print(my_dict)

#Looping through a dictionary
for key, value in my_dict.items():
    print(key, ":", value)

#Boolean

is_raining = True
if is_raining:
    print("Take an umbrella")

#Boolean operators

x = True
y = False
print(x and y)
print(x or y)
print(not x)

#Slicing a Boolean

bool_list = [True, False, True, True, False, False]
print(bool_list[1:4])
print(bool_list[::2])

#Conditional Statements

age = 18
if age >= 18:
    print("you are an adult")

    age = 16
    if age >= 18:
        print("you are an adult")
    else:
        print("you are a minor")


score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

age = 20
has_ID = True

if age >= 18:
    if has_ID:
        print("you can enter.")
    else:
        print("you need an ID")
else:
    print("you are underage")

    #Logical Operators

x = 5
y = 10

if x > 0 and y > 0:
    print("both are positive.")

if x > 0 or y < 0:
    print("atleast one is positive.")

    if not (x < 0):
        print("x is not negative")

#Input

# age = input("Enter you age:")
# print(type(age))

# age = int(input("Enter your age:"))
# height = float(input("Enter your height:"))

#Tuples

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#Accessing elements
print(my_tuple[0])
print(my_tuple[-1])

#Tuple Operations
#Concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
new_tuple = tuple1 + tuple2 
print(new_tuple)

#Slicing
print(new_tuple[1:4])

print(len(new_tuple))


#Sets

my_set = {1, 2, 3, 4, 5}
print(my_set)

#Set Operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

#Modifying a set
my_set.add(6)
my_set.remove(3)

print("Hello World")
name = "Roy Makanjira"
age = 22
height = 1.65
female = False
friends = ["Tawanda","Wesly","Mac",""]
address = {"country" : "Zimbabwe","city": "Harare","Location":"Budaz",
           "house number":"11154"}
print(f"my name is {name} am {age} years old and Iam a short guy with {height}meters and it is {female} that am female . I have a lot of friends which are {friends} and i live in {address}")

a = 15
b = 5

print(a*b)
print(a/b)
print(a+b)
print(a//b)
print(a**b)
print(a%b)

a < b
print(a<b) 
print(a>b)
print(a==b)
print(a >= b)
print(a<=b)
print(a!=b)

# logical operators
print(a>b and a != b)

if a == b:
    print("same")
elif a>b:
    print("Greater")
elif a<b:
    print("less")
else:
    print("")

temp = 35
sunny = True
if temp >= 30:
    print("it is hot")
elif temp < 30 and not sunny:
    print("cold and cloudy")
elif temp >=30 and sunny ==True:
    print("it is sunny and hot")
else:
    print("it is cold")

password = 12345
username = "admin"

pass1 =int(input("Enter your password: "))
user = input ("Enter your username: ")

if pass1 == password:
    if user == username:
        print("Welcome Admin") 
    else:
        print("invalid credential")
else :
    print("password is not correct  ")


print("hello world")




