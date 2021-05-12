import math

number = int(input("How many cows are there: "))

even = 0
odd = 0

for i in range(number):
    x = int(input("Enter the tag: "))
    if x%2 == 0:
        even += 1
        
odd = number - even

if odd == 0:
    groups = 1
elif even == 0:
    if odd%3 == 0:
        groups = odd*(2/3)
    elif odd%3 == 1:
        groups = ((odd-1)*(2/3)) - 1
    else:
        groups = ((odd-2)*(2/3)) + 1
elif even == odd:
    groups = odd*2
elif even > odd:
    groups = (odd*2) + 1
elif odd > even:
    x = 0
    if (odd - even)%3 == 0:
        x = (odd-even)*(2/3)
    elif (odd - even)%3 == 1:
        x = (((odd-even)-1)*(2/3)) + 1
    else:
        x = (((odd-even)-2)*(2/3)) + 1
    groups = (even * 2) + x

groups = math.floor(groups)
print("There are", groups, "groups of cows.")
