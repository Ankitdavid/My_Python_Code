## Opening fine and reading file
# f = open("cv.txt", "r")

# data = f.read() # # read all data
# print(data)

# f.close() 

# f = open("cv.txt", "r")

# line1 = f.readline(5) ## read 5 characters
# print(line1)

# f.close()

# f = open("cv.txt", "r")

# line1 = f.readline() # read one line at a time
# print(line1)

# line2 = f.readline() # read one line at a time
# print(line2)

# line3 = f.readline() # read one line at a time
# print(line3)

# f.close()

# # Opening fine and writing file
# f = open("cv2.txt", "w") # # if file does not exist it will create a new file

# f.write("Joshua David\nFresher\nPython Developer") # write data to file

# f.close()

# # opening fine and appending file
# f = open("cv.txt", "a") # if file does not exist it will create a new file

# f.write("M.No: 1234567890\nAddress: xyz") # append data to file

# f.close()

# # opening fine for reading and writing in a file without truncating the file and write it at 
# # the beginning of the file
# f = open("cv.txt", "r+")

# f.write("Mr. ")  
# print(f.read())

# f.close()

# # opening fine for reading and writing in a file, it is truncating the file and then write data, 
# # if file does not exist it will create a new file
# f = open("cv3.txt", "w+") 

# f.write("Java is a programming language\nJava is a platform")
    

# f.close()

# # opening fine for reading and writing in a file, it is appending the file without truncating the file,
# # if file does not exist it will create a new file and write data at the end of the file
# f = open("cv3.txt", "a+")

# f.write("\nJava is a framework\nJava is a library\nJava is a tool")

# f.close()

# # other syntax to open a file, perform task on file like(read, write, append, etc) and close it automatically
# with open("cv.txt", "r") as f: 
#     print(f.read())

# # if the cv4.txt file does not exist it will create a new file
# with open("cv4.txt", "a") as f: 
#     f.write("Hello MSI")

# # delete file operation
# import os

# os.remove("cv4.txt")

# # WAF that replaces all the occurences of "Java" with "Python" in a file

# with open("cv3.txt", "r") as f:
#     data = f.read()
#     data = data.replace("Java", "Python")
#     print(data)
    
# with open("cv3.txt", "w") as f:
#     f.write(data)

# # search if the word "tool" is exists in the file
# def check_for_word():
#     word = "tool"
#     with open("cv3.txt", "r") as f:
#         data = f.read()
#         if word in data:
#             print("Word found")
#         else:
#             print("Word not found")
            
# # WAF to find which line of the file does the word "tool" occur first. print 1 if word not found 

# def check_for_line():
#     word = "tool"
#     data = True
#     line_no = 1
#     with open("cv3.txt", "r") as f:
#          while data:
#              data = f.readline()
#              if word in data:  
#                  print(line_no) 
#                  return 
#              line_no += 1 
#     return -1 

# checnk_for_line()   

# from a file containing numbers separated by commas, print the count of even numbers.(1, 2, 76, 84, 90, 101)

count = 0
with open("cv4.txt","r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1
            
print(count)
    