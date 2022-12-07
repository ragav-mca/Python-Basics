"""
Validate user input for username. Conditions - username length should be between 4 and 8, 
should not start with a number, should not start or end with '_', and only alphabets, numbers
and '_' is allowed.
When the user enters an username, you should print all possible errors in the username.
For eg - if input is 1b%  - the output should be 'Username length should be >4 <8, 
no numeric at the start and no special chars allowed' 
"""

username = input("Enter the name: ")
a = len(username)
#b = username.isalpha()
print(a)
#print(b)

spl_char = "~`!#$%^&*()-+=;:<>,./@|[]"
if(a < 4 or a > 8) or username[0].isdigit() or username.startswith("_") or username.endswith("_") or username + spl_char:
    print("Username length should be >4 <8, no numeric at the start and no special chars allowed") 

if username.isalpha() or username.isdigit() or "_":
    print(username)

