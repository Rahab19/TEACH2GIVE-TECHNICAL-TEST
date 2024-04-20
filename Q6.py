# Write a program that counts the number of vowels in a sentence.
def count_vowels(text):
    count = 0

    for character in text:
        if character in "aAeEiIoOuU":
            count += 1

    return count


text = input("Text: ")

count = count_vowels(text)

print("Count:", count)
