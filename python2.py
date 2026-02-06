# l = [40,50,30,50,40]

# cnt = 0
# sum of all elements in list
# for i in l:
#     cnt = cnt + i
# print(f"The sum of all elements in list is {cnt}")

# lst = [1, 2, 2, 3, 1, 4]

# unique_list = []

# for item in lst:
#     if item not in unique_list:
#         unique_list.append(item)

# print(unique_list)


# l = [10, 20, 30, 40, 50]
# to reverse a list
# l = l[::-1]
# print(l)

# t = (10, 20, 30, 40, 50)
# print(t[0])
# print(t[0:len(t)])

# l = [10, 20, 30, 40, 50]
# t = tuple(l)
# print(t)

# dict1 = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York'
# }

# dict2 = {
#     'name': 'george',
#     'age': 32,
#     'city': 'France'
# }

# dict1.update(dict2)
# print(dict1)

# list = [1,2,3,1,2,3,1,1,2]
# def freq(list):

# year = int(input("Enter a year: "))

# if year%100 == 0 and year%400 == 0:
#     print(f"{year} is a leap year")

# elif year%100 != 0 and year%4 == 0:
#     print(f"{year} is a leap year")

# else:
#     print(f"{year} is not a leap year")

# n = int(input("Enter a number: "))

# even = 0
# odd = 0

# for i in range(1,n+1):
#     if(i%2 == 0):
#         even = even + i
#     else:
#         odd = odd + i
# print(f"The sum of even numbers is {even}")
# print(f"The sum of odd numbers is {odd}"

# print("The negative numbers in the list are ")
# for i in l:
#     if i < 0:
#        print(i)
 


# print(f"The positive numbers in the list are ")
# for i in l:
#     if i > 0:
#        print(i)

# mean of the list

# l = [10,20,30,40,50]
# sum = 0
# for i in l:
#     sum = (sum + i)
    
# print(sum/len(l))
        

# l = [12,16,13,25,19]

# maxel = l[0]
# secondmax = l[0]

# for i in l:
#     if i > maxel:
#         secondmax = maxel
#         maxel = i
#     elif i > secondmax and i != maxel:
#         secondmax = i
# print(maxel, secondmax)

# l = [1,3,2,1,2,2,3,1,4]
# to count the frequency of each element in the list
# for i in l:
#     count = 0
#     for j in l:
#         if i== j:
#             count = count + 1
#     print(f"The frequency of {i} is {count}")

# l = [7,10,2,6,5,9,3]

# to sort the list in ascending order

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] > l[j]:
#           l[i], l[j] = l[j], l[i]
# print(l)

# l1 = [7,10,2,6,5,9,3]
# l2 = [10,4,8,11,12,13]

# for i in l1:
#     if i in l2:
#         print(f"{i} is present in both lists")


# l1 = [7,10,2,6,5,9,3]
# l2 = [10,4,8,11,12,13]

# for i in l2:
#     if i not in l1:
#         print(f"{i} is present in l1 lists but not in l2")


# l = [1,2,3,5,6,7,8,9,10]

# length = len(l)
# for i in range(length):
#     if i+1 != l[i]:
#         print(f"The missing number is {i+1}")
#         break

# left rotation of a list

# l = [1,2,3,4,5,6]

# n = int (input("Enter the nubmer of rotations: "))

# for i in range(n):
#     x = l[0]
#     for j in range(1,len(l)):
#         l[j-1] = l[j]
#     l[len(l)-1] = x

# print(l)

# right rotation of a list
# l = [1,2,3,4,5,6]

# n = int (input("Enter the nubmer of rotations: "))
# length = len(l)

# for i in range(n):
#     x = l[length - 1]
#     i = length - 1

#     while(i>0):
#         l[i] = l[i-1]
#         i = i-1
#     l[0] = x
# print(l)


# sorted list or not
# l = [1,12,3,40,5,6]
# for i in range(1,len(l)):
#     if l[i] < l[i-1]:
#         print("The list is not sorted")
#         break
#     else:
#         print("The list is sorted")
#         break

# dictionary

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'e': 500, 'f': 600, 'g':700}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# d1 = {'a': 100, 'b': 200, 'c':300, 'd':400}

# sum = 0 
# for i in d1:
#     sum = sum + d1[i]

# print(f"The sum of all values in the dictionary is {sum}")

# d1 = {'a': 100, 'b': 200, 'c':300, 'd':400}

# target = 300
# for i in d1:
#     if d1[i] == target:
#         print(f"Key for the value {target} is {i}")
#         break
#     else:
#         print("Not found")


# l = [1,2,3,4,5,6]

# newl = []
# for i in range(len(l)):
#     if i % 2 == 0:
#         newl.append(l[i]*l[i])
# print(newl)


from pathlib import Path

filename = "hello.txt"

with open(filename, "r") as file:
    lines = file.readlines()


line_count = len(lines)
word_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

print("Number of lines:", line_count)
print("Number of words:", word_count)
