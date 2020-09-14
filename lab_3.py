words = input().split()
counts_words = dict()

for word in set(words):
    key = words.count(word)
    if counts_words.get(key): 
        counts_words[key].append(word)
    else: 
        counts_words[key] = [word]    

max_count_words = counts_words.get(max(counts_words))
max_count_words.sort()
print(max_count_words[0])