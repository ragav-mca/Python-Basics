# Get a city name from the user. Find out how many 'a' or 'e' is in the city name
"""
city_name = input("Enter the city: ")
print("Number of occurence of a: ",city_name.count("a"))
print("Number of occurence of e: ",city_name.count("e"))
"""
name = input("Enter the name: ")
count_a = 0
count_e = 0
for i in name:
    if i == "a":
        count_a += 1
        print("The number of occurences of a is: ", count_a)
    elif i == "e":
        count_e += 1
        print("The number of occurences of e is: ", count_e)
    
if count_a == 0:
    print("There is no a in the city name")
elif count_e == 0:
    print("There is no e in the city name")

    
Output:
Case 1:
Enter the name: chennai
The number of occurences of e is:  1
The number of occurences of a is:  1
    
Case 2:
Enter the name: madurai
The number of occurences of a is:  1
The number of occurences of a is:  2
There is no e in the city name      
