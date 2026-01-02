# ask user for name
name = input("What is your name? ")

# remove whitespace from str
# name = name.strip()

# capitalize user's name (ONLY FIRST WORD)
# name = name.capitalize()

# capitalize user's FULL name AND remove whitespace
name = name.strip().title()

# note: can avoid all lines above with:
# name = input("What is your name? ").strip().title.()

# say hello to user
print(f"hello {name}")