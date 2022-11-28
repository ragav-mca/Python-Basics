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
    elif i == "e":
        count_e += 1
    
if count_a == 0:
    print("There is no a in the city name")
elif count_e == 0:
    print("There is no e in the city name")

    
Output:
Enter the name: chennai
The number of a or e in the city name is:  2    
