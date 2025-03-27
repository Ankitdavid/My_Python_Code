## List

# data = [] ## empty list
# print(type(data))
# print(data)

# student = ["Ankit", 74.9, 25, "UP"]
# print(student)
# print(type(student))
# print(len(student))
# print(student[0])#indexing
# print(student[0],end=" ") # printing list in same line
# print(student[1],end=" ") # printing list in same line
# print(student[2],end=" ") # printing list in same line
# print(student[3],end=" ") # printing list in same line
# print(student[-3])#negative indexing
# print(student[2])
# print(student[-1])
# student[0] = "Ankit David"
# print(student)
# print(student[0:4:3])#slicing
# print(student[-3:-1])#negative slicing

## list methods

# list = [2, 1, 3, 6, 5, 4, 7, 9, 8]
# list.append(10)
# print(list)
# list.insert(10, 11)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.remove(11)  
# print(list)
# list.pop(2)
# print(list)
# list.reverse()
# print(list)
# list.clear()
# print(list)

# # Reverse and extend a string

# str = "Ankit"
# str = list(str)
# str.extend("David")
# print(str) 
# str.reverse()
# print(str)

## Tuple

# data = () ## empty tuple
# print(type(data))
# print(data)

# tup = (1, 2, 4, 3, 1, 5)
# print(tup)
# print(type(tup))
# print(len(tup))
# print(tup[0])#indexing
# print(tup[-1])#negative indexing
# print(tup[1:4:2])#slicing
# print(tup[-3:-1])#negative slicing
# tup.index(1)
# print(tup.index(1))
# tup.count(1)
# print(tup.count(1))

## WAP to ask the user to enter names of their 3 friends and store them in a list

# name = list(input("Enter the name of your 3 friends: ").split())
# print(name)

## OR

# friends = []
# friends.append(input("Enter the name of your first friend: "))
# friends.append(input("Enter the name of your second friend: "))
# friends.append(input("Enter the name of your third friend: "))
# print(friends)

## WAP to check if the list contain a palindrom of elements 

# pal = list(input("Enter the list of elements: "))
# pal1 = pal.copy()
# pal1.reverse()
# if(pal1 == pal):
#     print("The list is a palindrome")
# else:
#     print("The list is not a palindrome")