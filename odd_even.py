"""
Generate two random numbers. If both numbers are even, print All even. 
If both numbers are odd, print No even. Otherwise print Some even.
""" 
a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

list1 = []

list1.append(a)
list1.append(b)

even_count = 0
odd_count = 0

for num in list1:
    if num %2 == 0:
        even_count += 1
    elif num %2 != 0:
        odd_count += 1

if even_count == 2:
    print("All even")
elif odd_count == 2:
    print("No even")
else:
    if even_count == 1:
        print("Some even")

print("Even numbers: ", even_count)
print("Odd numbers: ", odd_count)