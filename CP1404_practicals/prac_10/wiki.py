"""Wikipedia script prompts."""

import wikipedia

# Get the user to input a title or phrase to search, then display results.
title_or_phrase = input("Enter title or phrase: ")
while title_or_phrase != "":
    try:
        page = wikipedia.page(title_or_phrase)
        print("{}\n {}\n {}\n".format(page.title, page.summary, page.url))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
