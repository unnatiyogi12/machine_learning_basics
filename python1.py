
# code to swap two numbers

# def swap(x,y):
#     return y,x

# print(swap(5,10))

# program to check whether a number is even or odd
# num = input("Enter a number: ")
# if int(num)%2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# print table of number
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# a = 5
# b = 10
# c = 4

# if a>b and a>c:
#     print(f"{a} is the largest number")
# elif b>a and b>c:
#     print(f"{b} is the largest number")
# else:
#     print(f"{c} is the largest number")

# n = 5

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(n))


# s = "radhika"

# def cnt_vowels(s):
#     count = 0
#     for char in s:
#         if char in 'aeiouAEIOU':
#             count += 1
#     return count

# print(cnt_vowels(s))

# s = "hello world"
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string(s))


# n = 110

# rev = 0
# x = n

# while(n>0):
#     rev = (rev * 10) + (n % 10)
#     n = n//10
# if x == rev:
#     print(f"{x} is a palindrome")


# n = int(input("enter the number:"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i   
# print(f"The sum of first {n} natural numbers is {sum}")

# n = int(input("enter the number:"))

# for i in range(0,n+1):
#     if n == 0:
#         print("0")
#     elif n == 1:    
#         print("1")
#     else:
#         a = 0
#         b = 1
#         print(a)
#         print(b)
#         for j in range(2,n):
#             c = a + b
#             print(c)
#             a = b
#             b = c

# i = input("enter the number:")

# vowels ='aeiouAEIOU'
# if i in vowels:
#     print(f"{i} is a vowel")
# else:
#     print(f"{i} is a consonant")

# n = int(input())
# count = 0
# while(n>0):
#     digit = n%10
#     count = count + digit
#     n = n//10
# print(count)

# l = [12, 7, 9, 21, 5, 18]

# for i in l:
#      maxi = max(l)
#      second_max = max(x for x in l if x != maxi)
# print(f"The maximum value in the list is {maxi}")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# mn = min(num1, num2)

# for i in range(1,mn+1):
#     if(num1%i == 0 and num2%i ==0):
#         hcf = i
# print(f"The HCF of {num1} and {num2} is {hcf}")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# mx = max(num1, num2)
# while(True):
#     if(mx % num1 == 0 and mx % num2 == 0):
#         lcm = mx
#         break
#     mx += 1
# print(f"The LCM of {num1} and {num2} is {lcm}")

# i = int(input("Enter the number:"))
# j = int(input("Enter the number:"))

# op = input("Enter operationc")

# if op == '+':
#     print(f"The sum is {i+j}")
# elif op == '-':
#     print(f"The difference is {i-j}")
# elif op == '*':
#     print(f"The product is {i*j}")
# elif op == '/':
#     print(f"The quotient is {i/j}")
# else:
#     print("Invalid operation")