# class student:
#     def hello(self):
#         print("Hello, I am a student")

# s1 = student()
# s1.hello()


class student:
    name = "Unnati"  #class attribute
    def __init__(self,name,age):
        self.name = name  #instance attribute
        self.age = age
    
    def info(self): #instance method
        print(f"Students details are Name: {self.name} and Age: {self.age}")

    @classmethod
    def classinfo(cls): #class method
        print(f"The class attribute is {cls.name}")
    
    @staticmethod
    def staticinfo(): #static method
        print("This is a static method")
    
s1 = student("Unnati", 126)
s2 = student("Vansh" , 130)

s1.info()
s2.info()

