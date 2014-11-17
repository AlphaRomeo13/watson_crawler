import json

jsonFP = open('items.json')
data = json.load(jsonFP)

outputFP = open('output.html', 'w')

outputFP.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n</head>\n<body>')

for item in data:
	outputFP.write(item['content'].encode('utf-8'))
	outputFP.write('\n')

outputFP.write('</body>\n</html>')

outputFP.close()
jsonFP.close()