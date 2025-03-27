## dict

# data = {} ## empty dictionary
# print(type(data))
# print(data)

# info = {
#     "name": "Joshua","surname" : "David","age": 24,"city": "New Delhi"
# }

# print(info)
# print(info["name"])
# print(info["surname"])
# print(info["age"])
# print(info["city"])

# info["age"] = 25
# print(info["age"])

# info["country"] = "India"
# print(info)

# del info["country"]
# print(info)

# print(info.keys())
# print(info.values())
# print(info.items())
 
# pair = list(info.items())
# print(pair[0])

# print(info.get("age"))

# info.update({"M.No": 12345})
# print(info)

# new_info = {"AM.No": 67890}
# info.update(new_info)
# print(info)

## nested dict

# students_data = {
#     "student1": {"name": "Joshua","surname" : "David","age": 24,"city": "New Delhi"},
#     "student2": {"name": "Rahul","surname" : "Sharma","age": 23,"city": "Mumbai"},
#     "student3": {"name": "Rohan","surname" : "Kumar","age": 25,"city": "Pune"},
# }

# print(students_data)
# print(students_data["student1"]["name"])    
# print(students_data["student2"]["city"])
# print(students_data["student3"]["age"])

## set

# data = set() #empty set
# print(type(data))
# print(data)

# collection = {1,2,2,2,1,"hello","hello","MSI",4,7}
# print(collection)
# print(type(collection))
# print(len(collection))

# collection.add(3)
# collection.add("hi") # add() method is used to add elements in set
# collection.add((4,5,6)) # tuple can be added in set
# collection.add((1,2,3))
# print(collection)

# collection.remove((1,2,3))
# collection.remove("hello") # remove() method is used to remove elements in set
# collection.remove(4) # if element is not present then it will give an error say "KeyError"
# collection.discard(7) # remove() method is used to remove elements in set
# collection.discard(8) # if element is not present then it will not give any error
# collection.pop() # remove() method is used to remove elements in set
# print(collection) 
# collection.clear() # clear() method is used to clear all the elements in set
# print(collection)

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.union(set2)) # union() method is used to combine or merge two set values & return a new set 
# print(set1.intersection(set2)) # intersection() method is used to find common elements in two set values & return a new set

## WAP to enter marks  of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

# result = {}
# result["maths"] = int(input("Enter marks of maths: "))
# result["science"] = int(input("Enter marks of science: "))
# result["english"] = int(input("Enter marks of english: "))
# print(result)

## Figure out a way to store 9 & 9.0 as separate values in a set 

# values = {(9,9.0)}
# print((values))
# print(type(values))

## OR

# values = {9,"9.0"}
# print(values)
# print(type(values))

## OR

values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)
print(type(values))