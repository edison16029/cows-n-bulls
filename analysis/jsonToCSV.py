import json
import csv

def load_words(filename):
    try:
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


filename = "_CNBFourLetterWordsScored"
jsonDictionary = load_words(filename + ".json")

with open( filename + ".csv", "w+", newline = "") as csvFile:
	csvWriter = csv.writer(csvFile)
	csvWriter.writerow(jsonDictionary[0].keys())
	for word in jsonDictionary:
		#print(type(word))
		csvWriter.writerow(word.values())
	csvFile.close()