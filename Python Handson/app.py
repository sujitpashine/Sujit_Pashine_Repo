#Declare Array and print
from ast import And

nums = [1, 2, 3, 4]
print(nums)

nums.append(5)
print(nums)

x = nums.pop()
print(x)
print(x)

nums.append(9)
print(nums)

x = nums.pop()
print(x)

x = nums.pop(2)
print(x)

for x in nums:
    x = x + 2
    print(nums)
print("Done")

# with open("sample.txt", 'r') as f:
#     for l in f.readlines(): print(l, end="\n")

#Create a list containing squares of numbers from 1 to 10 (HINT:use List Comprehension).
#1
a = [1,2,3,4,5,6,7,8,9,10]
x = 0
while x < len(a):
    a[x] = a[x] * a[x]
    x += 1 
print(a)
#2
a = []
x = 1
while x < 11:
    a.append(x*x)
    x += 1
print (a)
#3
a = []
for x in range(11): 
    x = x*x 
    a.append(x)
print(a[1:11])

#Code to check if the year is a leap year.
year = input('Enter the year: ')
year = int(year)

leap_year = year%4
if leap_year == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year" )

#Write a function to check if the year number is a leap year.
def leap(y):
    a=y%4
    if a == 0:
       print(y, "is a leap year")
    else:
       print(y, "is not a leap year")

leap(2008)

#Write a function to take an array and return another array 
#that contains the members of the first array that are even.

def even(x):
    a = 0 
    c = []
    while a < len(x):
        if x[a]%2 == 0:
           c.append(x[a])
        a += 1   
    print(c)

x = [1,4,18,6,2,8,16,12,14,10,3,5,7,9]
x.sort()
print(x)
even(x)  

#Write a function that takes 2 arrays and prints the members of the first
#array that are present in the second array.(HINT:use Membership Comprehension)

def array(a , b):
    x, y = 0, 0
    c = []
    while x < len(a):
        y = 0
        while y < len(b):
            if a[x] == b[y]:
                c.append(a[x])
                print(a[x])
            y += 1
        x += 1
    print(c)

a = [1,2,3,4,5,6,7,8,9,10]
b = [2,3,6,7,9]
array (a, b)

#Write a code to generate 20 Febunacci sequence in list

a, b, c = 0, 1, 0
i = 0
d = []
d.append(a)
d.append(b)
while i < 20:
    c = a + b
    d.append(c)
    a = b
    b = c
    i += 1
print(d)

#1. Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40, 50, 60):
#   a. Concatenate the two tuples and store it in “t_combine”
a = (10, 20, 30)
b = (40, 50, 60)

t_combine = a + b
print(t_combine) 

#   b. Repeat the elements of “t_combine” 3 times

a = (10, 20, 30)
b = (40, 50, 60)

t_combine = (a + b) * 3
print(t_combine) 

#   c. Access the 3rd element from “t_combine”

a = (10, 20, 30)
b = (40, 50, 60)

t_combine = a + b
print(t_combine[2])

#   d. Access the first three elements from “t_combine”

a = (10, 20, 30)
b = (40, 50, 60)

t_combine = a + b
print(t_combine[0:3])

#   e. Access the last three elements from “t_combine”

a = (10, 20, 30)
b = (40, 50, 60)

t_combine = a + b
print(t_combine[3:6])

#2. Create a list ‘my_list’ with these elements:
#a. First element is a tuple with values 1, 2, 3
#b. Second element is a tuple with values “a”, “b”, “c”
#c. Third element is a tuple with values True, False

my_list = [(1,2,3), ("a","b","c"), ("True", "False")]
print(my_list)

#3. Append a new tuple – (1, ‘a’, True) to ‘my_list’:
#a. Append a new list – *“sparta”, 123+ to my_list

my_list.append((1,'a','True'))
print(my_list)

new_list = ["*sparta",'123+']
my_list.append(new_list)
print(my_list)

#4. Create a dictionary ‘fruit’ where:
#a. The first key is ‘Fruit’ and the values are (“Apple”, “Banana”, “Mango”, “Guava”)
#b. The second key is ‘Cost’ and the values are (85, 54, 120, 70)
#c. Extract all the keys from ‘fruit’
#d. Extract all the values from ‘fruit’

fruit = {"Apple":85, "Banana":54, "Mango":120, "Guava":70}
print(fruit)

x = fruit.keys()
print(x)

y = fruit.values()
print(y)

#5. Create a set named ‘my_set’ with values (1, 1, “a”, “a”, True, True) and print the result.

my_set = {1, 1,"a", "a", True, True}
print(my_set)
 


               










  
