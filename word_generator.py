import random
import json

# Parameters: input, tokenizing or not, number of grams
def collect_ngrams(in_list, tokens = True, n = 1):
    #turn any input into a list
    ngrams = []

    # Conditional to see if input is a single String
    if isinstance(in_list, list) and len(in_list) == 1 and isinstance(in_list[0], str):
        in_list = in_list[0]

        # Tokenize grams into words with .split() or n amount of characters
        if tokens:
            in_list = in_list.split()
        else:
            in_list = list(in_list)
    elif isinstance(in_list, str):
        in_list = in_list.split() if tokens else list(in_list)

    # Adds each gram to the n_gram list
    for i in range(len(in_list) - n + 1):
        if tokens:
            ngrams.append(' '.join(in_list[i:i + n]))
        else:
            ngrams.append(''.join(in_list[i:i + n]))

    # Return the final list
    return ngrams

# Open txt file and tokenize individual words
file = open('training_text', 'r')
file_text = file.read()
file_ngrams = collect_ngrams(file_text)
# Index tracker
key = -1
# Word data in the form of dictionary
words = {}
final_word = ""

# Add all tokens to dictionary
for value in file_ngrams:
    # If the key does not exist, then add
    if value not in words:
        words[value] = []

    # If the key is not greater than -1, then do not attempt to index
    if (key > -1):
        words[file_ngrams[key]].append(value)
    key += 1
    final_word = value

# Add first element to value list of final key to make sure generation never stops
words[final_word].append(file_ngrams[0])

# Open json file for word data
with open('word_data.json', 'w') as outfile:
    json.dump(words, outfile)

# Text generation method
def generate_str(num):
    sentence = ""

    # Get random key
    random_key = random.choice(list(words.keys()))
    random_value = random_key

    # Make sure the initial key is uppercase for natural structure
    while (not random_value[0].isupper()):
        random_key = random.choice(list(words.keys()))
        random_value = random_key

    # Append random values to return string
    for i in range(num):
        sentence += random_value + " "
        random_key = random.choice(words[random_value])
        random_value = random_key

    return sentence