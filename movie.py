#Get a movie name. Find out how many words are in that movie. 

movie_name = input("Enter the movie name: ")
print("Movie name: ",movie_name)

word_count = 1

for count in movie_name:
    if count == " ":
        word_count += 1

print("The number of words in the movie are: ", word_count)


Output:
Enter the movie name: The Shawshank Redemption
Movie name:  The Shawshank Redemption
The number of words in the movie are:  3
