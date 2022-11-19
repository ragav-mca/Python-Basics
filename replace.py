#Get a name. Replace all the 'a' with 'c'. Print the name. 

name = input("Enter the name: ")
result = []

for i in name:
    if i == "a":
        i ="c"
    result.append(i)
print(result)
print("".join(result))