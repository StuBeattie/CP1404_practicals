"""Count the occurrence of words in a string"""

word_count = {}
# Get user to write a sentence then use split to break the sentence into individual words
users_string = input("Please write a sentence: ")
words = users_string.split()

# loop through words and count word reoccurrence
for word in words:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1

# create a list from the keys in the dictionary(words) and sort in ascending order
words = list(word_count.keys())
words.sort()

# align the outputs so the numbers are in one nice column
word_length = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, word_length, word_count[word]))
