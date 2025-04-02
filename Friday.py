# import os
# file_path ="MONDAY.txt"

# if os.path.exists ("MONDAY.txt"):
#     print(f"the file.{file_path }exists")
# else:
#     print("the file doesn't exist")



# def power (base , exponent):
#     return base ** exponent
# print(power(2,3))

# default arguments 

# def greet(name="Steph Curry"):
#     print(f"hello ,{name}")
# greet()

# #  Nested Functions
# def outer():
#     print(" this is outer function")
#     def inner():
#         print("this is the inner function")
#     inner()
# outer()




# def global_function():
#     print("this is a global function")
# global_function()

# def another_function():
#     global_function()
# another_function()

# file handling that allows us to read and manipulate files 


# file = open("filename" ,"mode")
# file.close()
# with open("index.txt","r"):
    
# file=open("index.txt","r") 
# content = file.read()
# print(content)
# file.close

# with open("index.txt","w") as file:
#     content=file.read()
#     print(content)

# with open ("index.txt","w") as f:
#     lines=[]
#     f.write("hello how are you\n")

import os
if os.path.exists("index.txt"):
    print("the file exists ")
    os.remove("index.txt")
else:
    print("the file does not exist")

os.rmdir("Golden State Warriors")

