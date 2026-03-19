import string

def word_frequency(text):
    # remove punctuation
    for char in string.punctuation:
        text = text.replace(char, '')
    
    # convert to lowercase and split
    text = text.lower()
    words = text.split()
    
    # count words
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count


# test paragraph
paragraph = """Python is great. Python is easy to learn and fun to use.
I really like Python because it's simple. Python is used for web dev, data science, and more.
Python rocks!"""

# get the word frequencies
result = word_frequency(paragraph)

# find top 5 most common
top_words = []
for word, count in result.items():
    top_words.append((word, count))

top_words.sort(key=lambda x: x[1], reverse=True)

print("\nTop 5 words:")
for i in range(5):
    print(f"{top_words[i][0]}: {top_words[i][1]}")
