import re
from collections import Counter


class Corrector:

    def __init__(self, lang='fr'):
        text = open('txt/candide.txt').read() + open('txt/ddbl.txt').read()
        self.words = Counter(self.words_from_txt(text))
        return

    def words_from_txt(self, txt):
        return re.findall(r'\w+', txt.lower())

    def probabilty_of_word(self, word):
        N = sum(self.words.values())
        return self.words[word]/N

    def known_words(self, words):
        return set(word for word in words if word in self.words)

    def level_1_edit(self, word):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
        deletes = [left + right[1:] for left, right in splits if right]
        transposes = [left + right[1] + right[0] + right[2:] for left, right in
                      splits if len(right) > 1]
        replaces = [left + letter + right[1:] for left, right in splits if
                    right for letter in letters]
        inserts = [left + letter + right for left, right in splits for letter
                   in letters]

        return set(deletes + transposes + replaces + inserts)

    def level_2_edit(self, word):
        return (level_2 for level_1 in self.level_1_edit(word) for level_2 in
                self.level_1_edit(level_1))

    def get_candidates(self, word):
        return (self.known_words([word]) or
                self.known_words(self.level_1_edit(word)) or
                self.known_words(self.level_2_edit(word)) or
                [word])

    def correct(self, word):
        return max(self.get_candidates(word), key=self.probabilty_of_word)
