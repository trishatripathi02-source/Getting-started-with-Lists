def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

            print("List of words with first and last alphabets with matching with eachother.\n", lst)
            return ctr

count = match_words(['xyz', 'zyp', 'slp', 'ujo', '445', '657'])
print("Number of words with matching first and last alphabets: ", count)