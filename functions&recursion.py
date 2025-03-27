## function

# def greet(name):
#     print(f"Hello {name}!")
#     print("How are you?")

# greet("John")
# greet("Jane")

## function definition

# def cal_sum (a, b): # parameters
#     return a + b
    
# print(cal_sum(5, 10)) # first time function called; arguments
# print(cal_sum(15, 20)) # second time function called; arguments
# print(cal_sum(25, 30)) # third time function called; arguments

# # average of 3 numbers
# def cal_avg(a, b ,c):
#     return (a + b + c) / 3

# print(cal_avg(10, 20, 30))

## function with default parameters
# def cal_prod(a = 5, b = 10):
#     return a * b

# print(cal_prod())

# # WAF to print the length of a list.(list is the parameter)

# cities = ["Noida","London", "Paris", "New York", "Tokyo","Delhi"]
# heroes = ["Batman", "Superman", "Spiderman", "Ironman","Thor"]

# def list_length(lst):
#     return len(lst)

# print(list_length(cities))
# print(list_length(heroes))

## WAF to print the element of a list in a single line.(list is the parameter)

# state = ["Uttar Pradesh", "Delhi", "Punjab", "Haryana", "Rajasthan", "Gujarat", "Maharashtra", "Bihar",]

# def print_list(lst):
#     for item in lst:
#         print(item, end = "  ")

# print_list(state)

# # WAF to find the factorial of n.(n is the parameter)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print("Factorial of", n, "is:",fact)
        
# cal_fact(5)

## or

# n = int(input("Enter a number: "))
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print("Factorial of", n, "is:",fact)
        
# cal_fact(n)

# # WAF to convert USD to INR.
# usd_val = int(input("Enter the INR amount: "))
# def cal_conv(usd_val):
#     inr_val = usd_val * 87.47
#     print(usd_val, "USD :", inr_val, "INR")

# cal_conv(usd_val)

## Recursion

# # Print n to 1 backwards
# def show(n):
#     if(n == 0): # base case
#         return
#     print(n)
#     show(n-1)
    
# show(5)

# # factorial using recursion

# n = int(input("Enter a number: "))
# def fact(n):
#     if(n == 0 or n == 1): # base case
#         return 1
#     else:
#         return n * fact(n-1)
    
# print("Factorial of", n, "is:", fact(n))
    
# # write a recursive function to calculate the sum of first  n natural numbers

# n = int(input("Enter a number: "))
# def sum(n):
#     if(n == 0): # base case
#         return 0
#     else:
#         return n + sum(n-1)

# print("Sum of first", n, "natural numbers is:", sum(n))

# write a recursive function to print all element in list.

def print_list(lst, idx):
    if(idx == len(lst)): # base case
        return
    else:
        print(lst[idx])
        print_list(lst, idx+1)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print_list(fruits, 0)