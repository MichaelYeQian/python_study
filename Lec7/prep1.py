def count_word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    word_frequency ={}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
        return word_frequency

sentence = input("Enter a sentence:")
frequency = count_word_frequency(sentence)
print("Word Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
