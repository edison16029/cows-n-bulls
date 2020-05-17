import json
from profanity_check import predict


FILENAME = "_CNBFourLetterWordsDefinedUpdated.json"
OUTFILE = "_CNBFourLetterWordsScored.json"


def getMask(i, letter):
	mask = list("____")
	mask[i] = letter
	return "".join(mask)

wordList = []
with open(FILENAME, "r") as f:
	wordList = json.load(f)

lexDistribution = {}

# Preparing the LexDistribution dictionary as masks, eg: '_a__'
for word in wordList:
	for i,letter in enumerate(word["word"]):
		key = getMask(i,letter)
		if key not in lexDistribution:
			lexDistribution[key] = 1
		else:
			lexDistribution[key] +=1

for mask in lexDistribution:
	lexDistribution[mask] /= len(wordList)
	#print(mask, lexDistribution[mask])

maxScore = float('-inf')
minScore = float('inf')
# Computing difficulty score for each word
for word in wordList:
	wordScore = 0
	for i,letter in enumerate(word["word"]):
		mask = getMask(i,letter)
		wordScore += lexDistribution[mask]
		word["1gram-score"] = wordScore
		maxScore = max(maxScore, wordScore)
		minScore = min(minScore, wordScore)

print(maxScore, minScore)

for word in wordList:
	if predict([word["word"]]) == 1:
		word["is_profane"] = True
	else:
		word["is_profane"] = False
	word["1gram-score"] = (word["1gram-score"] - minScore) / (maxScore - minScore)
	if word["1gram-score"] < 0.50:
		word["level"] = "hard"
	elif word["1gram-score"] > 0.65:
		word["level"] = "easy"
	else:
		word["level"] = "medium"
	print(word)

with open(OUTFILE, "w") as f:
	json.dump(wordList, f, indent = 4)