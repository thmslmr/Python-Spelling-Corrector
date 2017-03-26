import re
from collections import Counter

class Corrector :
	WORDS = None

	def __init__(self) :
		text = open('txt/candide.txt').read() + open('txt/ddbl.txt').read()
		self.WORDS = Counter(self.wordsFromTxt( text ))
		return
	def wordsFromTxt(self, txt) :
		return re.findall( r'\w+', txt.lower() )

	def probabiltyOfWord(self, word) :
		N = sum(self.WORDS.values())
		return self.WORDS[word]/N

	def knownWords(self, words) :
		return set(word for word in words if word in self.WORDS)

	def level_1_edit(self, word) :
		letters = 'abcdefghijklmnopqrstuvwxyz'
		splits = [ (word[:i], word[i:]) for i in range(len(word)+1) ]
		deletes = [ left + right[1:] for left, right in splits if right]
		transposes = [ left + right[1] + right[0] + right[2:] for left, right in splits if len(right) >1 ]
		replaces = [ left + letter + right[1:] for left, right in splits if right for letter in letters ]
		inserts = [left + letter + right for left, right in splits for letter in letters]
		return set(deletes + transposes + replaces + inserts)

	def level_2_edit(self, word) :
		return ( level_2 for level_1 in self.level_1_edit(word) for level_2 in self.level_1_edit(level_1) )

	def candidates(self, word) :
		return (self.knownWords([word]) or self.knownWords( self.level_1_edit(word) ) or self.knownWords( self.level_2_edit(word) ) or [word])

	def correct(self, word) :
		return max(self.candidates(word), key=self.probabiltyOfWord)
