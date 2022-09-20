n = int(input("Enter The Number"))
sum = 10
x = n
while sum > 9:
    sum = 0
    while x > 0:
        rem = x % 10
        sum += rem * rem
        x = int(x / 10)
    print("Sum = ", sum)
    if sum == 1:
        print(n, "Is Happy Number \U0001F603")
    else:
        x = sum
if sum < 9 and sum != 1:
    print(n, "Is Sad Number \U0001f972")
