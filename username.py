"""
Validate user input for username. Conditions - username length should be between 4 and 8, 
should not start with a number, should not start or end with '_', and only alphabets, numbers
and '_' is allowed.
When the user enters an username, you should print all possible errors in the username.
For eg - if input is 1b%  - the output should be 'Username length should be >4 <8, 
no numeric at the start and no special chars allowed' 
"""

username=input("Enter the name: ")
a = len(username)
spl_char = "~`!#$%^&*()-+=;:<>,./@|[]"
b = 0
if a < 4 or a > 8 or username[0].isdigit() or username.startswith("_") or username.endswith("_"):
    b+=1

for i in range(len(spl_char)):
    if spl_char[i] in username:
        b+=1
     
if b>=1:
    print("Username is Invalid")
else:
    print("Username is valid")


Output:
Enter the name: _python
Username is Invalid

Enter the name: python_
Username is Invalid

Enter the name: 2python
Username is Invalid

Enter the name: pyth2on
Username is valid

Enter the name: python
Username is valid

Enter the name: pyth_on
Username is valid
