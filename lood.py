## Control flow Structure
## while loop

# count = 1
# while count <= 10: 
#     print("Hello")
#     count += 1
    
# # Print number 1 to 100
    
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
    
# # Print reverse number 100 to 1
    
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
    
# # Print the multiplication table of any number

# n = int(input("Enter a number: "))    
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1

# # print the elements of the following list using while loop [1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(num):
#     print(num[i])
#     i += 1

# # search for a number x in this tuple using while loop and terminate it with break (1,4,9,16,25,36,49,64,81,100)

# num = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter a number: "))
# i = 0
# while i < len(num): 
#     if num[i] == x:
#         print("Number found", i)
#         break ## terminate the loop
#     i += 1
# else:
#     print("Number not found")

# # print the odd number 0 to 10 with the help of while loop and continue

# i = 0
# while i <= 10:
#     if (i % 2 == 0):
#         i += 1
#         continue # skip the rest of the code and continue the loop
#     print(i)
#     i += 1
    
# print("Odd number")

# # WAP to find the sum of first n natural numbers using while loop

# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print("Sum of first n natural numbers is:", sum)

# ## list loop

# # print the elements of the following list using for loop [1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)
    
# # Search for a number x in this tuple using for loop (1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter a number: "))
# idx = 0
# for el in nums:
#     if el == x:    # searching it through linear search
#         print("Number found", el, "Index", idx)
#     idx += 1     

## Range() function

# for i in range(10): # range(stop)
#     print(i)

# for i in range(1, 11): # range(start, stop)
#     print(i)

# for i in range(1, 11, 2): # range(start, stop, step)
#     print(i)

# # print the number from 1 to 1000 what the help of range function

# for i in range(1, 1001):
#     print(i)

# # print the number from 1000 to 1 what the help of range function

# for i in range(1000, 0, -1):
#     print(i)

# # print the number multiplication table of any number n

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

# # pass statement

# for i in range(10):   
#     pass
     
# print("MSI is Good")

# # WAP to find the sum of first n natural numbers using while loop

# n = int(input("Enter a number: "))
# sum = 0

# for i in range(1, n+1):
#     sum += i

# print("Sum of first n natural numbers is:", sum)

# WAP to find the factorial of first n number using for loop

# n = int(input("Enter a number: "))
# fact = 1

# for i in range(1, n+1):
#     fact *= i
    
# print("Factorial of first n number is:", fact)

print([[i+j for i in "abc"]for j in "def"])