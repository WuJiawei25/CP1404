"""
Word Occurrences
Estimate: 30 minutes
Actual:   30 minutes
"""
text = input("Text: ")

words = text.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

sorted_words = sorted(word_counts.keys())

max_word_length = 0
for word in sorted_words:
    if len(word) > max_word_length:
        max_word_length = len(word)

for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_counts[word]}")