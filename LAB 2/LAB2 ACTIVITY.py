# Activity 1
list1 = []
print("Enter The Elements Of The First List")
for i in range(0, 5):
    n = int(input("Enter The Element"))
    list1.append(n)
print(list1)

list2 = []
print("Enter The Elements Of The Second List")
for i in range(0, 5):
    n = int(input("Enter The Element"))
    list2.append(n)
print(list2)

list3 = []
list3 = list1 + list2
print(list3)

#Activity 2
word = input("Enter The Word ")
tempword = word[::-1]
if word == tempword:
    print("This is Palindrome")
else:
    print("This is not Palindrome")

# Activity 3
a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = []
for indrow in range(3):
    c.append([])
    for indcol in range(3):
        c[indrow].append(0)
        for indaux in range(3):
            c[indrow][indcol] += a[indrow][indaux] * b[indcol][indaux]
print(c)

# Activity 4
list = [(1, 1), (5, 1), (5, 0), (1, 0)]
length = len(list)
perimeter = 0
for i in range(0, length - 1):
    dist = (((list[i][0] - list[i + 1][0]) ** 2)
            + ((list[i][1] - list[i + 1][1]) ** 2)) ** 0.5
    perimeter = perimeter + dist
perimeter = perimeter + (((list[0][0] - list[length - 1][0]) ** 2)
                         + ((list[0][1] - list[length - 1][1]) ** 2)) ** 0.5

print(perimeter)

# Activity 5
set1 = {0, 1, 2, 3, 4, }
set2 = {5, 6, 7, 8, 9}
e = set()
for i in set1:
    if i not in set2:
        e.add(i)
for i in set2:
    if i not in set1:
        e.add(i)
print(e)

# Activity 6
sample = {("Moiz", "Shamsheer"): "03185069789", ("Aqib", "Khan"): "03065234545", ("Ali", "Ahmed"): "03211887669"}
first = input("Enter First Name ")
last = input("Enter Last Name ")
search = (first, last)
if search in sample:
    print(sample[search])
else:
    print("Record Not Found")
