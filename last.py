"""
Same program as above. Instead of adding 'a' at the end of the short name, add the last letter.
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cattt, arrow (length is equal by adding the last letter of Cat)
"""
name1 = input("Enter the name 1: ")
name2 = input("Enter the name 2: ")

print(name1)
print(name2)

strlen1 = len(name1)
strlen2 = len(name2)

print("The string length of name 1: ",strlen1)
print("The string length of name 2: ",strlen2)

max = 0
min = 0

if(strlen1 > strlen2):
    max = name1
    min = name2
elif(strlen2 > strlen1):
    max = name2
    min = name1
else:
    print("Both strings are equal")

print("The maximum of two strings is: ", max)
print("The minimum of two strings is: ", min)

strlen_max = len(max)
strlen_min = len(min)

print("The string length of max is: ",strlen_max)
print("The string length of min is: ",strlen_min)

x = (strlen_max - strlen_min)
print("The count of character to be equalled: ",x)

for i in range(0,x):
    min = min + min[-1]
print("The result after equalling with last char: ",min)
        












