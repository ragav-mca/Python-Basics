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

Output:
case : 1
Enter the number1: 4
Enter the number2: 8
All even
Even numbers:  2
Odd numbers:  0
    
case : 2
Enter the number1: 12
Enter the number2: 17
Some even
Even numbers:  1
Odd numbers:  1
    
case : 3
Enter the number1: 23
Enter the number2: 27
No even
Even numbers:  0
Odd numbers:  2
