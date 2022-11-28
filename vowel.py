"""
Get a word from the user. If the word has any vowels, print Has vowels.
Check if the word has Y. Then also print Has vowel. Check for vowel separately and Y separately. 
Repeat these steps until user gives a word that has Y or X in the word. 
"""
vowels_1 = ["a","e","i","o","u"]
vowel_2 =["y"]
vowel_count = 0

while True:
    a = input("Enter the word: ")
    if "x" in a or "y" in a:
        break
    else:
        print("Enter the word with x or y to end")

for char1 in a:
    if char1 in vowels_1:
        vowel_count += 1 
        print("The user word", a ,"has vowels")
    elif char1 in vowel_2:
        vowel_count += 1 
        print("The user word has y and the word", a ,"is a vowel")
    else:
        if vowel_count == 0:
           print("The user word a has no vowels")

Output:
Enter the word: apple
Enter the word with x or y to end
Enter the word: python
The user word a has no vowels
The user word has y and the word python is a vowel
The user word python has vowels
