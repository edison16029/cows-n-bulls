




Files :

1. _CNBFourLetterWordsGHC.json
Word Count : 5548

2. _CNBFourLetterWordsWordsAPI.json
Word Count : 4213

Difference  wordsAPIMinusGHC =  927
> Contains some meaningul words like blog,spam. However most of words dont have definitions.
> Might get a clear picture once we retrieve words only those which have definitions.
Update : Words with meanings are also bad,like xciv etc.

Difference  GHCMinuswordsAPI =  2262
Apart from the plural words, most of the other words are garbage. Even google doesn't have meaning for them.
If we are ignoring plurals, we can ignore this file altogether.
Else we can use this to get a list of words which indicate plurals (by comparing input and output word of req). This list can be used to show errors like "Plurals Not Allowed".

Combined :
Common Words : 3286
Combined Words : 3286 + 927 + 2262 = 6475

Of Combined Words :
Checking in TW - Defined = 2686, Undefined = 3789
	Of TWDefined :
	Upto Difficulty 6, almost all the words are recognisable
	Difficulty 7-10 (inclusive of 10), contains some meaningful words(Eg. Gawp has 10 difficulty) and hence can't be neglected fully.

Checking in WAPI - Defined = 2437, Undefined = 1776


	



 

