"""
Input string is 'aba1aaba2bab3ababa'. Find the number of times the substring aba appears 
in the input string. 
"""
input_string = "aba1aaba2bab3ababa"
print("Input String: ",input_string)
sub_string = "aba"
count = 0
flag = True
start = 0

while flag:
    a = input_string.find(sub_string,start)
    if a == -1:
        flag = False
    else:
        count += 1
        start = a + 1
print("Number of times aba appears: ",count)

Output:
Input String:  aba1aaba2bab3ababa
Number of times aba appears:  4
