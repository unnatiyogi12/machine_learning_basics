# from abc import ABC, abstractmethod

# class abstract(ABC):

#     @abstractmethod

#     def area(self):
#         pass

#     def perimeter(self):
#         pass

# class square(abstract):

#     def __init__(self, side):
#         self.side = side
#         print(f"The side of the square is {side}")

#     def area(self):
#         return self.side * self.side
            
# class rectangle(abstract):

#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#         print(f"The length of the rectangle is {length} and the breadth is {breadth}")   

#     def area(self):
#         return self.length * self.breadth     


# obj = rectangle(10, 5)

# print(obj.area())


# dunder method - start and ends with underscore

# class animal():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

    
#     def __str__(self):
#         return f"helloo how are youu and the name of the animal is {self.name}"
    
#     def __add__(self,other):
#         return self.age + other.age
    
# obj1 = animal("dog", 12)
# obj2 = animal("cat", 8)
# print(obj1 + obj2)
        

# @ => decorator

# def decorate(func):   #captures the original function here sum in this case
    # def sum(a,b):  #this is the wrapper function
#         print("This is decorated function")
#         func(a,b)
#         print("End of decorated function")
#     return sum



# problems :
# 1. arguments of main function sometimes varies and decorate function may not be able to catch the main agrguments
# 2. if we have to decorate multiple functions then we have to write the same code again and again


# @decorate
# def sum(a,b):
#     print(f"your sum is {a+b}")

# sum(5,10)

# using args and kwargs 


# args and kwargs

# are the special keywords in python which are used to handle flexible numbers of arguments in a function
# you can use * and ** for defining args and kwargs

# All about args

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
    
#     print(sum)

# addition(45,67,78,90,36)

# All about kwargs
# kwargs = key word arguments
# use dictionary data structure to handle key word

# def addition(**kwargs):
#     print(kwargs)

# addition(a =80,b=74,c=27)

# def info(**kw):
#     print("your information is")
#     for i in kw:
#         print(f"{i} : {kw[i]}")

# info(name= "aditi", age= 24, city = "gwalior")