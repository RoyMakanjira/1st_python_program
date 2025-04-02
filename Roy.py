# tup1 =(1,2,3,4,5)
# tup2 = (6,7,8,9,10)
# print(tup1 + tup2)
# print(tup1 *2)

# numbers = (1,2,3,4,5)
# print(len(numbers))
# numbers = list(numbers)

# numbers = (1,2,3,4,5,6,7,8,9,10)
# print(numbers)
# numbers = list(numbers)
# numbers.sort
# print(numbers)
# numbers.sort(reverse="True")
# print(numbers)
# 
# a = 6
# b = 5
# 
# print(a==b)
# 
# if (a==6) :
#  print("you are correct" ),
# elif (a<6):
#    print("you are stupid")
# else:
#      print("you are wrong")
# 
#      print(type(a))
my_set = {1,2,3,4,5}
my_set2 = {6,7,8,9,10}
# 
#      union_set= my_set | my_set2
#      print(union_set)
 
# union_set= my_set | my_set2
# or
union_set = my_set.union(my_set2)
print(union_set)
 
int_set = my_set.intersection(my_set2) 
print(int_set)

