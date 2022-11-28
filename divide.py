"""
Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided. 
"""
x = int(input("Enter the number: "))
y = 3
print("Number: ",x)
countdiv = 0

while x // y > 3:
    x = x // y
    print("Result: ",x)
    countdiv += 1
print("Number of times divided: ",countdiv)
