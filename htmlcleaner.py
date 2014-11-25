import os
import re

inDir = 'raw-html-output/'
outDir = 'final-output/'

for filename in os.listdir(inDir):
	with open(inDir + filename) as inFP:
		outFilename = filename
		outFP = open(outDir + outFilename, 'w+')
		outFP.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n')
		outFP.write('<title>' + filename + '</title>')
		outFP.write('</head>\n<body>\n')
		for line in inFP:
			# remove
			line = re.sub(r'<a(.|\n)*?>', '', line)
			line = re.sub(r'</a>', '', line)
			line = re.sub(r'<span(.|\n)*?>', '', line)
			line = re.sub(r'</span>', '', line)
			line = re.sub(r'<sup(.|\n)*?>(.|\n)*?</sup>', '', line)
			line = re.sub(r'\[edit\]', '', line)

			# simplify
			line = re.sub(r'<h1 (.|\n)*?>', '<h1>', line)
			line = re.sub(r'<h2 (.|\n)*?>', '<h2>', line)
			line = re.sub(r'<h3 (.|\n)*?>', '<h3>', line)
			line = re.sub(r'<h4 (.|\n)*?>', '<h4>', line)
			line = re.sub(r'<p (.|\n)*?>', '<p>', line)
			line = re.sub(r'<pre (.|\n)*?>', '<pre>', line)
			line = re.sub(r'<ul (.|\n)*?>', '<ul>', line)
			line = re.sub(r'<ol (.|\n)*?>', '<ol>', line)
			line = re.sub(r'<li (.|\n)*?>', '<li>', line)

			# files
			# line = re.sub(r'file:', 'http:', line)

			if line.startswith('<h2>References</h2>'):
				break

			outFP.write(line)

		outFP.write('</body>\n</html>')
		outFP.close()
		# os.rename(outDir + outFilename, outDir + filename)
