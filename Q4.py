# Write a program that accepts a string as input, capitalizes the first letter of each word in the string,
# and then returns the result string.
def capitalize_first_letters(input_text):
    words = text.split()
    print(words)

    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


text = input("text:")
result = capitalize_first_letters(text)
print(result)
