#Get a movie name. Find out how many words are in that movie. 

movie_name = input("Enter the movie name: ")
print("The movie name is: ",movie_name)

word_count = 1

for count in movie_name:
    if count == " ":
        word_count += 1

print("The number of words in the movie are: ", word_count)


