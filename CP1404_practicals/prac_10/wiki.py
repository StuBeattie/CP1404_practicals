"""Wikipedia script prompts."""

import wikipedia

# Get the user to input a title or phrase to search, then display results.
while True:
    try:
        page = input("Enter title or phrase: ")
        if page == "":
            break
        else:
            print(wikipedia.search(page))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
