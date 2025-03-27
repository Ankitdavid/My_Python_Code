# string - Concatenation, Length of string, Indexing, String Slicing
str1 = "ankit"
str2 = "DAVID"
print(str1 + str2)#Concatenation without space
print(str1 + " " + str2)#Concatenation with space
final_str = str1 + str2
print(len(final_str))#Length of string
print(final_str[5])#Indexing
print(final_str[-10])#Negitive indexing
print(final_str[5:10])#String Slicing
print(final_str[-10:-5])#String Slicing with negitive indexing
print(final_str[0:9:2])#String Slicing with step, starting from given index number and printing every 2 char
print(final_str[::3])#String Slicing with step, starting from 0 and printing every 3 char 
print(final_str.startswith("An"))#startswith() is used to check if string starts with given value
print(final_str.endswith("it"))#endswith() is used to check if string ends with given value
print(final_str.isupper())#isupper() is used to check if string is in uppercase
print(final_str.islower())#islower() is used to check if string is in lowercase
print(final_str.isalpha())#isalpha() is used to check if string is in alphabets
print(final_str.isalnum())#isalnum() is used to check if string is in alphabets and numbers
print(final_str.isdigit())#isdigit() is used to check if string is in digits
print(final_str.isnumeric())#isnumeric() is used to check if string is in numbers
print(final_str.isdecimal())#isdecimal() is used to check if string is in decimal numbers
print(final_str.split())#split() is used to split string into list
print(final_str.upper())#upper() is used to convert string to uppercase
print(final_str.lower())#lower() is used to convert string to lowercase
print(final_str.capitalize())#capitalize() is used to convert first letter of string to uppercase
print(final_str.title())#title() is used to convert first letter of each word to uppercase
print(final_str.replace("ankit", "Joshua"))#replace() is used to replace string with given value
print(final_str.count("a"))#count() is used to count the number of times a given value appears in string
print(final_str.find("i"))#find() is used to find the index of given value in string