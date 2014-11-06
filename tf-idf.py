import re

localWords = {}
stopWords = ['the', 'a', 'is', 'as', 'of']
text = 'This is a longer test, test test test.'
text = text.split()

for w in text:
    w = re.sub(r'[\.\,\(\)\:\;\'\"]', '', w)
    w = w.lower()

    if w in stopWords:
        continue

    if w in localWords.keys():
        localWords[w] += 1
    else:
        localWords[w] = 1

    print w

for w in localWords.keys():
    localWords[w] = localWords[w]*1.0 / len(text)

print localWords