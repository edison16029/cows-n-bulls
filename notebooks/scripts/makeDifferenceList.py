import json
def load_words(filename):
	try:
		with open(filename,"r") as english_dictionary:
			print("File Found")
			valid_words = json.load(english_dictionary)
			return valid_words
	except Exception as e:
		return str(e)




wordsAPIDict = load_words("_CNBFourLetterWordsWordsAPI.json")
GHCDict = load_words("_CNBFourLetterWordsGHC.json")


print("wordsAPIDict Count : ",len(wordsAPIDict))
print("GHCDict Count : ",len(GHCDict))

wordsAPISet = set(wordsAPIDict.keys())
GHCSet = set(GHCDict.keys())

wordsAPIMinusGHC = wordsAPISet - GHCSet
GHCMinuswordsAPI = GHCSet - wordsAPISet

print("Difference  wordsAPIMinusGHC = ",len(wordsAPIMinusGHC))
print("Difference  GHCMinuswordsAPI = ",len(GHCMinuswordsAPI))

wordsAPIMinusGHCDict = {}
for word in wordsAPIMinusGHC:
	wordsAPIMinusGHCDict[word] = 1

output_filename = 'wordsAPIMinusGHC.json'
with open(output_filename,'w') as f:
	json.dump(wordsAPIMinusGHCDict,f,indent=2)


GHCMinuswordsAPIDict = {}
for word in GHCMinuswordsAPI:
	GHCMinuswordsAPIDict[word] = 1

output_filename = 'GHCMinuswordsAPI.json'
with open(output_filename,'w') as f:
	json.dump(GHCMinuswordsAPIDict,f,indent=2)