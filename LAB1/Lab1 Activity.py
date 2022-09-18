# Activity 1
num = int(input("Enter Number Please"))
if num % 2 == 0:
    print("The Number Is Even")
else:
    print("The Number Is Odd")

# Activity 2
sum = 0
n = int(input("Enter The Number"))
while n != 0:
    sum = sum + n
    n = int(input("Enter The Number"))
print("Sum is ", sum)

# Activity 3
num = int(input("Enter The Number"))
p = 2
flag = True
while p < num:
    if num % p == 0:
        flag = False
        break
    else:
        p = p + 1
if flag == False:
    print("The Number Is Not Prime")
else:
    print("The Number Is Prime")

# Activity 4
i = 0
sum = 0
while i <= 4:
    n = int(input("Enter The Number"))
    sum = sum + n
    i = i + 1
print("Sum is ", sum)

# Activity 5
sum = 0
i = 0
while i <= 10:
    sum = sum + i
    i = i + 1
print("Sum Is ", sum)

# Activity 6
name = input("Enter Your Name Please")
print("Hello " + name)
job = input("What is your Job please")
print("Your Job is " + job)
num = input("Would You like to tell Your Number please")
print("Your number is " + num)

#Activity 7
import random
sysnum = random.randint(1,9)
usernum = int(input("Enter Your Number"))
if usernum == sysnum:
    print("The Number You Guessed Was Right")
elif usernum > sysnum:
    print("Too high Try again")
elif usernum < sysnum:
    print("Too Low Try again")
else:
    print("Wrong Input")