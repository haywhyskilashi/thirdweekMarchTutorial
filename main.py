#  2D list = list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0][0])
print(food[0][1])
print(food[1][0])
print(food[2][1])
print(food[0][0])


# tuple = collection which is ordered and unchangeable
#used to group together related data

student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("male"))
print((student))

for x in student:
    print(x)

if "bro" in student:
    print("Bro is here")


# SET = collection which is unordered, unidexed.
#       no duplicates values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "knife"}

utensils.update(dishes)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()



for x in utensils:
    print(x)



# dictionary = changeable, unordered collectiong of unique
# key: value pairs fast becuase they use
# hashing, allows to access a value

capitals = {'USA':'Washington DC',
            'India': 'New Delhi', 'china': 'Beijing', 'Russia' :
            'Moscow'}

print(capitals['Russia'])
print(capitals.values())


# index operator[] = gives access to a
# sequences element(str, list, tuples)

name = "bro code"

#if(name[].islower()):
#    name = name.capitalize()


first_name = name[0:3].upper()
print(first_name)

second_name = name[4:].upper()
print(second_name)

last_character = name[-1]
print(last_character)


#functions = a block of code which is
# executed only when it is called


def hello(firstnameS, secondName, age):
    print("HEllo!" + firstnameS + " " + secondName)
    print("You are ", age, " years old")
    print("Have a nice day")

#nameS = "bro"
#hello(nameS)

hello("Bro", "Code", 21)



# Write a Python program to calculate the sum of three given numbers. If the
# values are equal, return three times their sum


x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
z = int(input("Enter the value of z:"))
def sum_thirce(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum

print(sum_thirce(x, y, z))



# Write a Python program to count the
# number 4 in a given list.

my_tuple = (1,2, 3,4,5,4,3,2,1)
count_of_1 = my_tuple.count(4)
print(count_of_1)


# Write a Python program to test whether a
# passed letter is a vowel or not


def vowelorconsonant(x):
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        print("It is a vowel")
    else:
        print("It is a consonant")
vowelorconsonant('c')
vowelorconsonant('o')



# Write a Python program that checks whether a specified
# value is contained within a group of values

def contained_values(groupdata, n):
    for value in groupdata:
        if n == value:
            return True
    return False

print(contained_values([1,5,8,3],3))
print(contained_values([1,5,8,3], -1))



#  Write a Python program to create a
#  histogram from a given list of integers

def histogram(items):
    for n in items:
        output = ' '
        times = n
        while(times > 0):
            output += '*'
            times = times -1
        print(output)
histogram([2,3,6,5])



# Write a Python program that concatenates
# all elements in a list into a string and returns it


def concantenate_list(l):
    ans = ' '
    for i in l:
        ans = ans + str(i)
    return ans

print(concantenate_list([1, 5, 12, 2]))



# Write a Python program to print all even numbers from a given list of numbers in the same order
# and stop printing any after 237 in the sequence

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]


for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)



# Write a Python program that prints out all colors from
# color_list_1 that are not present in color_list_2.


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print("Original set element")
result1 = list(set(color_list_2).difference(color_list_1))
result2 = list(set(color_list_1).difference(color_list_2))

print(result1)
print(result2)




# Write a Python program that will accept the base and
# height of a triangle and compute its area

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area = (height * base) / 2

print(area)




# Write a Python program to sum three
# given integers. However, if two values are equal,
# the sum will be zero

def sumOfThreeIntegers(x, y, z):
    if (x == y or y == x or z == x):
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sumOfThreeIntegers(2,1,3))
print(sumOfThreeIntegers(2,2,2))
print(sumOfThreeIntegers(3,2,2))




# Write a Python program to sum two given integers. However,
# if the sum is between 15 and 20 it will return 20.


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))




# Write a Python program that returns true if the two given integer
# values are equal or their sum or difference is 5.

def Values(x, y):
    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    else:
        return False
print(Values(7, 2))
print(Values(3, 2))
print(Values(7, 3))
print(Values(27, 53))

# Write a Python program to add two objects
# if both objects are integers

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be an integer"
    return a + b
print(add_numbers(10, 20))
print(add_numbers('5', 20))
print(add_numbers(10, 20.23))
























