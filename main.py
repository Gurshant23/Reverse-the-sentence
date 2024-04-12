def reverse_words(text):
    words = text.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence


input_sentence = input("Enter the sentence to be reversed: ")
result = reverse_words(input_sentence)
print(f"Given sentence: {input_sentence}")
print(f"Reversed sentence: {result}")
