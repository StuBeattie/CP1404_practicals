"""Wikipedia script prompts."""

import wikipedia

# Get the user to input a title or phrase to search, then display results.
while True:
    try:
        title_or_phrase = input("Enter title or phrase: ")
        if title_or_phrase == "":
            break
        else:
            page = wikipedia.page(title_or_phrase)
            print("{}\n {}\n {}\n".format(page.title, page.summary, page.url))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
