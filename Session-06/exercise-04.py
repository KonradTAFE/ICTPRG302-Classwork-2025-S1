# filename: exercise-04.py
# Write a Python script that asks the user for a sentence, and then counts the words in the sentence,
# and displays the results to the user.
#

# Ask user for sentence
the_sentence = input('Enter a sentence (without punctuation): ')
sentence = the_sentence.lower()
clean_sentence = ""

for character in str(sentence):
    if character.isalpha() or character == " ":
        clean_sentence += character

# Create an empty dictionary called word_counts
word_counts = {}

# Split the sentence into words
sentence_split = clean_sentence.split()

# For each word in the sentence:
#   If word is in the word_counts dictionary:
#       Increment the count for the word
#   Else:
#       Make the count for the word 1

for word in sentence_split:
    word_counts[word] = word_counts.get(word, 0) + 1
print(the_sentence)
print(clean_sentence)
for key, value in word_counts.items():
    print(key, value)

# For each word in the word_count dictionary:
#   Display word, count
# The output should be similar to this:
#
# Word Count
# The 2
# quick 1
# brown 1
# fox 1
# Sample sentences:
#
# The quick brown fox jumps over the lazy dog who was watching the tabby cat
# Mary had a little lamb, it's fleece as white as snow, and everywhere that mary went the lamb was sure to go
# She sells seashells by the sea shore. The shells she sells are surely seashells. So if she sells shells on the seashore, I'm sure she sells seashore shells.