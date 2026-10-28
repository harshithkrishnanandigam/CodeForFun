from collections import Counter
text = input("Enter a sentence or paragraph: ")
text = text.lower()
words = text.split()
cleaned_words = []

for word in words:
    cleaned_word = ''.join(char for char in word if char.isalnum())
    cleaned_words.append(cleaned_word)

word_count = Counter(cleaned_words)
print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

if word_count:
    highest_count = max(word_count.values())
    print("Most repeated word(s):")

    for word, count in word_count.items():
        if count == highest_count:
            print(f"{word}: {count}")