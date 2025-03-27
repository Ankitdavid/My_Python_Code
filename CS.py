#conditional Statement
# if stetement
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote")

# if-else stetement

# attendance = int(input("Enter your total attendance: "))
# if attendance >= 75:
#     print("You are eligible for exam")
# else:
#     print("You are not eligible for exam")

# elif stetement

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade : A+")
# elif marks >= 80:
#     print("Grade : A")
# elif marks >= 70:
#     print("Grade : B+")
# elif marks >= 60:
#     print("Grade : B")
# elif marks >= 50:
#     print("Grade : C")
# elif marks >= 40:
#     print("Grade : D")
# else:
#     print("Fail")

# nested if-else stetement

# age = int(input("Enter your age: "))
# if age >= 18:
#     if age >= 80:
#         print("You are not eligible to Drive")
#     else:
#         print("you are eligible to Drive")
# else:
#         print("you are not eligible to Drive")

# match case statement

# days = int(input("Enter day number: "))
# match days:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Invalid")
    
#OR        

# def get_weekday_name(week_number):
#     # Define a function that takes a week number as input and returns the corresponding weekday name
#     match week_number:
#         # Use a match statement to handle different cases based on the input week number
#         case 1:
#             return "Monday"
#         case 2:
#             return "Tuesday"
#         case 3:
#             return "Wednesday"
#         case 4:
#             return "Thursday"
#         case 5:
#             return "Friday"
#         case 6:
#             return "Saturday"
#         case 7:
#             return "Sunday"
#         case _:
#             return "Invalid week number"
# # Get input from the user
# week_number = int(input("Enter week number (1-7): "))
# # Get the weekday name
# day_name = get_weekday_name(week_number)
# # Print the weekday name
# print(day_name)  

# WAP to check weather the number is even or odd  

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num," Is Even")
# else:
#     print(num," Is Odd")                                            
    
# WAP to check if a number is a multiple of 7 or not

# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print(num," Is a multiple of 7")
# else:
#     print(num," Is not a multiple of 7")

# WAP to find the greatest of three numbers entered by the user

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num > second_num and first_num > third_num:
    print("The greatest number is:", first_num)
elif second_num > first_num and second_num > third_num:
    print("The greatest number is:", second_num)
else:
    print("The greatest number is:", third_num)