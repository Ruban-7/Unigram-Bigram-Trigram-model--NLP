def Trigram(sentence):
    words = sentence.split()
    return list(zip(words,words[1:],words[2:]))

sentence = "The quick brown fox jumps over the lazy dog"
print(Trigram(sentence))