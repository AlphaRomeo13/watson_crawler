import json
import uuid
import re

jsonFP = open('items.json')
data = json.load(jsonFP)

codeJsonFP = open('code.json', 'r+')
codeDict = json.load(codeJsonFP)
codeJsonFP.close()

codeId = ''

for item in data:
	fn = item['title'][0].encode('utf-8')
	fn = re.sub(' ', '-', fn)
	fn = ''.join([c for c in fn if c.isalnum() or c in ['-']]).rstrip()
	outputFP = open('raw-html-output/' + fn + '.html', 'a+')

	content = item['content']
	if content.encode('utf-8').startswith('<pre'):
		codeId = str(uuid.uuid4())
		codeDict[codeId] = content
		outputFP.write('<p>WHATSON? ' + codeId + '</p>\n' + content.encode('utf-8'))

	else:
		outputFP.write(content.encode('utf-8'))

	outputFP.write('\n')

	outputFP.close()

with open('code.json', 'w+') as outfile:
	json.dump(codeDict, outfile)

jsonFP.close()