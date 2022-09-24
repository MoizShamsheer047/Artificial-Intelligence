# LAB TASK 1
list1 = []
list2 = []
le1 = int(input("Enter The Length Of List1 "))
le2 = int(input("Enter The Length Of List2 "))
for i in range(le1):
    n = int(input("Enter The Value for List1 "))
    list1.append(n)
for i in range(le2):
    n = int(input("Enter The Value for List2 "))
    list2.append(n)
list3 = []
list3 = list1 + list2
print(list3)

for i in range(len(list3)):
    for j in range(len(list3)):
        if list3[j] > list3[i]:
            temp = list3[j]
            list3[j] = list3[i]
            list3[i] = temp
print(list3)

# LAB TASK 2
list1 = []
list2 = []
le1 = int(input("Enter The Length Of List1 "))
le2 = int(input("Enter The Length Of List2 "))
for i in range(le1):
    n = int(input("Enter The Value for List1 "))
    list1.append(n)
for i in range(le2):
    n = int(input("Enter The Value for List2 "))
    list2.append(n)
list3 = []
list3 = list1 + list2
print(list3)

for i in range(len(list3)):
    for j in range(len(list3)):
        if list3[j] > list3[i]:
            temp = list3[j]
            list3[j] = list3[i]
            list3[i] = temp
print(list3)
print("Largest element of array is ")
print(list3[len(list3) - 1])
print("Smallest element of array is ")
print(list3[0])

#LAB TASK 3
import math

x = -3.14
h = 0.001
while x < 3.15:
    z = x + h
    sin = (math.sin(z) - math.sin(x)) / h
    cos = math.cos(x)
    print("The value of PI is: ", x)
    print("The value of SIN(X) is: ", sin)
    print("The value of COS(X) is: ", cos)
    print()
    x += 0.01

# LAB TASK 4

dict = {("Moiz", "Shamsheer"): "01-04-2002", ("Aqib", "Khan"): "01-16-2000", ("Ali", "Ahmed"): "05-12-2001"}
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for first, last in dict:
    print(first, last)
name = input("Who's birthday do you want to look up? ")
names = name.split()
search = (names[0].capitalize(), names[1].capitalize())
if search in dict:
    print(name.upper(), " birthday is on ", dict[search])
else:
    print("Record Not Found")

# LAB TASK 5
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
key = ["name", "salary"]
my_dict = {k: sample_dict[k] for k in key}
print(my_dict)
