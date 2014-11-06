import json
import re
import math

jsonFP = open('items.json')
data = json.load(jsonFP)

outputFP = open('houtput.html', 'w')

numParagraphs = 0
paragraphCount = {}
localWordsDicts = []

stopWords = ['the', 'a', 'is', 'as', 'of', 'so', 'it', 'these', 'our', 'us', 'however', 'but', 'hence', 'by', 'therefor']

for item in data:
    if not item['content'].encode('utf-8').startswith('<p>'):
        continue

    numParagraphs += 1
    localWords = {}
    paragraph = item['content'].encode('utf-8').split()

    for word in paragraph:

        word = re.sub(r'[\.\,\(\)\:\;\'\"\{\}\[\]]', '', word)
        word = re.sub(r'<(.*?)>', '', word)
        word = word.lower()

        if word in stopWords:
             continue

        if word in localWords.keys():
            localWords[word] += 1
        else:
            localWords[word] = 1

            if word in paragraphCount.keys():
                paragraphCount[word] += 1
            else:
                paragraphCount[word] = 1

    localWordsDicts.append(localWords)

for dictionary in localWordsDicts:
    for word in dictionary.keys():
        dictionary[word] = (dictionary[word]*1.0 / len(dictionary)) * math.log(numParagraphs / paragraphCount[word])

print "numParagraphs = " + str(numParagraphs)

i = 0
stopWordsWikipedia = ['See also', 'References', 'Contents', 'External links', 'Further reading', 'Notes', 'Footnotes']

for item in data:
    item = item['content'].encode('utf-8')

    if item.startswith('<p>'):
        outputFP.write('<h3>')
        outputFP.write(" ".join(sorted(localWordsDicts[i], key = localWordsDicts[i].__getitem__, reverse = True)[:10]))
        outputFP.write('</h3>')
        outputFP.write('\n')
        i += 1

    if item.startswith('<h2>'):
        stop = False
        for word in stopWordsWikipedia:
            if word in item:
                stop = True
                break
        if stop is True:
            continue

    outputFP.write(item)
    outputFP.write('\n')

outputFP.close()
jsonFP.close()