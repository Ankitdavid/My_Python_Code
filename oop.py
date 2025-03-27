# # Creating Class
# class student:
#     college = "MIMT College"
#     def __init__(self, fullname, marks1, marks2, marks3): # This is a parameterized constructor and self is a reference to the current instance of the class and fullname is a parameter
#         self.name = fullname # This is an attribute
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
#         print("Adding new student in Database...")
    
#     def Welcome(self): # This is a method created inside the class
#         sum = self.marks1 + self.marks2 + self.marks3
#         print("Total Marks: ", sum, "\nAverage Marks: ", sum/3) # This is a local variable
#         print("Welcome", self.name, "to", student.college) # This is a class attribute
    
#     @staticmethod
#     def Greet(): # This is a static method
#         print("Your in NCR Number 1 College")
    
    
# # Creating Object(instance)
# s1 = student("Joshua David", 85, 90, 80) # This is an instance
# print("Name: ", s1.name, "\nMath: ", s1.marks1, "\nPython: ", s1.marks2, "\nJava: ", s1.marks3, "\nCollege: ", s1.college)
# s1.Welcome() # calling the method first time
# s1.Greet() # calling the static method

# s2 = student("Ankit David", 90, 95, 85) 
# print("Name: ", s2.name, "\nMath: ", s2.marks1, "\nPython: ", s2.marks2, "\nJava: ", s2.marks3, "\nCollege: ", s2.college)
# s2.Welcome() # calling the method second time
# s2.Greet() # calling the static method

# # Example of car company
# class Car:
#     brand = "Brand:" "  " "TAVA"
#     carname = "Name:" " " "Curvv"
#     model = "Model:" " " "2025"
#     variant = "Variant:" " " "+A"
#     color = "Color:" " " "Black"
#     price = "Price:" " " "Rs. 19 Lakh"
           # def __init__(self): # # This is a default constructor if we will not make by default Python will make it.
           #     print("Adding new car in Database...")
           #     pass
    
# car1 = Car()
# print(car1.companyname)
# print(car1.carname)
# print(car1.model)
# print(car1.variant)
# print(car1.color)
# print(car1.price)
    
# # create account class with 2 attributes - balance & account no.
# # create methods for debit, credit & printing the balance.

# class account:
#     def __init__(self, bal,acc):
#         self.balance = bal
#         self.account_no = acc
        
#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited from your account")
#         print("Total balance =", self.balance )
    
#     # Credit method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited from your account")
#         print("Total balance =", self.balance )
    
#     # Final balance
#     def final_balance(self):
#         return  self.balance
#         print("Rs.", amount, "was credited from your account")
        
# acc1 = account(10000, 123456)
# acc1.debit(2000)
# acc1.credit(4000)
       
# # del keyword (used to delete object properties or object itself)(del s1.name)(del s1)

# class student: 
#     def __init__(self,name):
#         self.name = name
        
# s1 = student("Rahul")
# print(s1.name)    

# del s1.name # deleting the name property of s1
# print(s1)

# del s1 # deleting the object s1
# print(s1)

# # private variables

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # while using double underscore (__) so is become private
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        
# acc1 = Account(123456, 1234)

# print(acc1.acc_no)
# print(acc1.reset_pass())

# # single inheritance

# class car: # parent/base class
#     @staticmethod
#     def start():
#         print("Car started..")
   
#     @staticmethod
#     def stop():
#         print("Car stopped..")
        
# class toyotacar(car): # child/derived class
#     def __init__(self, name):
#         self.name = name

# car1 = toyotacar("Fortuner")
# car2 = toyotacar("Prius")

# print(car1.name)
# car1.start()
# car1.stop()
# print(car2.name)
# car2.start()
# car2.stop()

# # multiple inheritance

# class car:
#     @staticmethod
#     def startc():
#         print("Car started..")

#     @staticmethod
#     def stopc():
#         print("Car stopped..")

# class bike:
#     @staticmethod
#     def startb():
#         print("Bike started..")

#     @staticmethod
#     def stopb():
#         print("Bike stopped..")

# class carbike(car, bike):
#     def __init__(self, name):
#         self.name = name

# carbike1 = carbike("BMV M5")
# carbike2 = carbike("Bajaj")

# print(carbike1.name)
# carbike1.startc()
# carbike1.stopc()
# print(carbike2.name)
# carbike2.startb()
# carbike2.stopb()
          
# # multi-level inheritance
       
# class car: # parent/base class
#     @staticmethod
#     def start():
#         print("Car started..")
   
#     @staticmethod
#     def stop():
#         print("Car stopped..")
        
# class toyotacar(car): # child class for car and parent class for fortuner
#     def __init__(self, brand):
#         self.brand = brand

# class fortuner(toyotacar): # child class for toyotacar
#     def __init__(self, type):
#         self.type = type

# car1 = fortuner("SUV")
# car1.start()
# car1.stop()

# # hirarchical inheritance

# class car: # parent/base class
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class toyota(car): #child/derived class
#     def __init__(self, name):
#         self.name = name
        
# class mahindra(car): #child/derived class
#     def __init__(self, name):
#         self.name = name
        
# class TATA(car): #child/derived class
#     def __init__(self, name):
#         self.name = name

# car1 = toyota("Fortuner")
# car2 = mahindra("Scorpio")
# car3 = TATA("Nano")

# print(car1.name)
# car1.start()
# car1.stop()
# print(car2.name)
# car2.start()
# car2.stop()
# print(car3.name)
# car3.start()
# car3.stop()

# # hybrid inheritance

# class car: # parent/base class
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class ford_sr(car): #child/derived class for car and parent/base class for endeavour
#     def __init__(self, srname): # (sr=showroom)
#         self.srname = srname
        
# class ford_sc(car): #child/derived class for car and parent/base class for endeavour
#     def __init__(self, scname): #(sc=service center)
#         self.scname = scname

# class endeavour(ford_sr, ford_sc): # child class which inherits for ford_sr and ford_sc
#     def __init__(self, type):
#         self.type = type

# car1 = ford_sr("ABC showroom")
# car2 = ford_sc("XYZ service center")
# car3 = endeavour("SUV")

# print(car1.srname)
# print(car2.scname)
# print(car3.type)
# car1.start()
# car1.stop()

# # super() method is used to access methods of the parent class

# class car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..") 
        
# class fordcar(car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()
          
# car1 = fordcar("Figo", "Hybrid")
# print(car1.name)
# print(car1.type)

# # Polymorphism

# # operator overloading

# print(5 + 5)
# print("Jungle"+"Book") #concatenate
# print([1,2,3] + [4,5,6]) #merge

# # addtion and subtraction of two complex numbers

# class complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(self.real,"i +", self.img, "j")
        
#     def __add__(self, num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return complex(newreal, newimg)
    
#     def __sub__(self, num2):
#         newreal = self.real - num2.real
#         newimg = self.img - num2.img
#         return complex(newreal, newimg)
        
# num1 = complex(5, 6)
# num1.shownumber()

# num2 = complex(3, 4)
# num2.shownumber() 

# num3 = num1 + num2
# num3.shownumber()       

# num3 = num1 - num2
# num3.shownumber()   
    
# # find the area and parimeter of any circle,and take radius as input from the user while using class and object concept

# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
# radius = int(input("Enter the radius of the circle: "))
# c = circle(radius)
# print("Area of the circle is:", c.area())
# print("Perimeter of the circle is:", c.perimeter())

# # define a employee class with attributes role, department & salary.This class also has a showdetails() method.
# # and create an engineer class which inherits properties from employee class and has additional attributes name & age

# class employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
        
#     def showdetails(self):
#         print("Role:", self.role)
#         print("Department:", self.dept)
#         print("Salary:", self.salary)

# class engineer(employee):
#     def __init__(self, name, age):
#         self.name = "Name = "+name
#         self.age = "Age = "+age
#         super().__init__("Engineer", "IT", "80,000")
        
# engg1 = engineer("Joshua", "25")
# print(engg1.name)
# print(engg1.age)
# engg1.showdetails()

# # create a class called order which stores item & its price.use dunder function __gt__() to convey that:
# # order1 > order2 id price of order1 > price of order2

# class order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
       
#     def __gt__(self, odr2):
#         return self.price > odr2.price
    
# odr1 = order("apple", 80)
# odr2 = order("banana", 50)

# print(odr1 > odr2)

# # class method or decorator

# class person:
#     name = "anonymous"
    
#     @classmethod
#     def change_name(cls, new_name):
#         cls.name = new_name
        
# p1 = person()
# p1.change_name("Joshua")
# print(person.name)

# # property decorator

# class student:
#     def __init__(self, python, java, c):
#         self.python = python
#         self.java = java
#         self.c = c
        
#     @property
#     def percentage(self):
#         return str((self.python + self.java + self.c)/3) + "%"
    
# stu1 = student(80, 90, 70)
# print(stu1.percentage)

# stu1.c = 85
# print(stu1.percentage)