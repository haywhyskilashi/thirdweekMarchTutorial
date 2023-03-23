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













