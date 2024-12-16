#Create a dictionary of words and their frequencies.

text = input("Enter a string: ")

word_freq = {}

words = text.split()

for word in words:
    word = word.lower()  
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
