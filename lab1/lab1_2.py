import re

text = input()
words = re.split('; |, | ', text)

new_words = [w[1:] for w in words]
new_text = ' '.join(new_words)

print(new_text)