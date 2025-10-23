


#verifying if a sentence contains a specific string, 
#then adding each of them in a dict with its count

sentence = "Data is the new oil they say. Some say it is not true, while some say it is not."

sentence_words = sentence.split()

print(sentence_words)

words_count = {}

for word in sentence_words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
print(words_count)