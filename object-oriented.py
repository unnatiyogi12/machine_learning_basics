# class student:
#     def hello(self):
#         print("Hello, I am a student")

# s1 = student()
# s1.hello()


# class student:
#     name = "Unnati"  #class attribute
#     def __init__(self,name,age):
#         self.name = name  #instance attribute
#         self.age = age
    
#     def info(self): #instance method
#         print(f"Students details are Name: {self.name} and Age: {self.age}")

#     @classmethod
#     def classinfo(cls): #class method
#         print(f"The class attribute is {cls.name}")
    
#     @staticmethod
#     def staticinfo(): #static method
#         print("This is a static method")
    
# s1 = student("Unnati", 126)
# s2 = student("Vansh" , 130)

# s1.info()
# s2.info()


# single level inheritance
# class Factory:
#     def prop(self, material, quantity):
#         material = self.material
#         quantity = self.quantity
#         print(f"The material is {material} and the quantity is {quantity}")

# class car(Factory):
#     def __init__(self, material, quantity, color):
#         self.material = material
#         self.quantity = quantity
#         self.color = color
#         print(f"The color of the car is {color}")

# c1 = car("steel", 100, "red")
# print(c1.prop("steel", 100))
# print(c1.color)


# multiple inheritance
# class Animal:
#     def __init__(self,age):
#         print("Eating")

# class Human:
#     def __init__(self,name,age):
#         print("Walking")

# class Robot( Human, Animal):
#     def work(self):
#         print("Working")
        

# obj = Robot("ram", 25)


# multilevel inheritance

# class Factory:
#     def __init__(self, material, quantity):
#        self.material = material
#        self.quantity = quantity
#        print(f"The material is {material} and the quantity is {quantity}")

# class bhopalFactory(Factory):
#     def __init__(self, material, quantity, color):
#         self.material = material
#         self.quantity = quantity
#         self.color = color
#         print(f"The color of the car is {color}")

# class delhiFactory(Factory):
#         def __init__(self, material, quantity, color):
#             super().__init__(material, quantity) #super() is used to call the parent class constructor
#             self.color = color
#             print(f"The color of the car is {color}")
        
#         def display(self):
#             print(f"The material is {self.material} and the quantity is {self.quantity} and the color is {self.color}")
   
        
# obj = delhiFactory("steel", 100, "red")
# obj.display()

