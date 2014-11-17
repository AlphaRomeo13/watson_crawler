import json
import uuid

jsonFP = open('items.json')
data = json.load(jsonFP)

codeDict = {}
codeId

for item in data:
	fn = item['title'][0].encode('utf-8')
	outputFP = open('output/' + fn + '.html', 'a+')

	content = item['content']
	if content.encode('utf-8').startswith('<pre>'):
		codeId = str(uuid.uuid4())
		codeDict[codeId] = content

	outputFP.write('WHATSON? ' + codeId + ' ' + content.encode('utf-8'))
	outputFP.write('\n')

	outputFP.close()

with open('code.json', 'a+') as outfile:
	json.dump(codeDict, outfile)

jsonFP.close()