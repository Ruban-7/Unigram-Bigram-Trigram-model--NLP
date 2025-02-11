def bigram(sentence):
    words = sentence.split()
    return list(zip(words,words[1:]))

sentence = "The quick brown fox jumps over the lazy dog"
print(bigram(sentence))