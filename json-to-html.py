import json

jsonFP = open('items.json')
data = json.load(jsonFP)

outputFP = open('output.html', 'w')

for item in data:
	outputFP.write(item['content'].encode('utf-8'))
	outputFP.write('\n')

outputFP.close()
jsonFP.close()