# loops are used to repeat a block of code multiple times
#  there are two primary types of loops [1] while loops and [2] for loops 

# "for" loop is used to iterate over a sequence(list,tuples,dict,string or range)

# syntax:
# for variable in sequence:
   #    statement

fruits = ["a","b","c"]
for fruit in fruits:
    print(fruit)

text = "python"
for character in text:
    print(character)


# functions is a block of reusable code 
# place () after the function name to invoke it

#  why do we need functions ?
# 1. reduce code duplication
# 2. organization of code
# 3. easy to debbug

#  a simple function without parameters

def greet():
    print("Hello welcome to python")

greet()

# Function with 1 parameter
  
def greet(name):
    print(f"Hello, {name}!!")
greet("Roy")
greet("Wesly")
 
#  function with multiple parameters

def add(a,b):
    return a + b
result = add(2,3)
print(result)


# number=0
# while number <100:
#  number+=1
#  print(number)

# number=range(1,20)
for num in range(2,21,2):
    print(num)
    
 