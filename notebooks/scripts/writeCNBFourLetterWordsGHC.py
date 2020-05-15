import json
import os, sys

def load_words():
    try:
        filename = "WordListGHC.json"
        # filename = "FourLetterWordsWordsAPI.json"
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

def getCNBFourLetterWords(english_words):
    fourLetterWord = {}
    for word in english_words.keys():
        if len(word)!=4 or len(list(set(word)))!=4 or not word.isalpha():
            continue
        fourLetterWord[word] = 1
    return fourLetterWord

if __name__ == '__main__':
    
    english_words = load_words()
    print("Total GHC Words : ",len(english_words))

    _CNBFourLetterWordsGHC = getCNBFourLetterWords(english_words)
    print("Total CNB Four Letter Words : ",len(_CNBFourLetterWordsGHC))

    output_filename = '_CNBFourLetterWordsGHC.json'
    with open(output_filename,'w') as f:
        json.dump(_CNBFourLetterWordsGHC,f,indent=2)