import json
import csv

csvFileName = "./_CNBFourLetterWordsDefined.csv"
jsonFileName = "_CNBFourLetterWordsDefinedUpdated.json"

data = []
with open(csvFileName) as csvFile:
	csvReader = csv.DictReader(csvFile)
	for row in csvReader:
		data.append(dict(row))


with open(jsonFileName , "w") as jsonFile:
	jsonFile.write(json.dumps(data, indent = 4))