import re
import json
from collections import Counter
from urllib.request import urlopen


class Corrector:

    def __init__(self,
                 lang='fr',
                 sources=None,
                 letters=None):
        """ Init corrector """
        (self.sources) = (sources) or self.fetch_settings(lang, 'sources')
        (self.letters) = (letters) or self.fetch_settings(lang, 'letters')
        self.words = self.get_words()

    def fetch_settings(self, lang, keys):
        """ Fetch given settings for a given language """
        if not lang:
            raise Exception('Language must be provided.')
        if not keys:
            raise Exception('Name of settings must be provided.')

        try:
            with open('settings.json', 'r') as file:
                all_settings = json.load(file)
        except FileNotFoundError:
            raise Exception('Sources file must be provided.')

        if type(keys) is not list:
            keys = [keys]

        try:
            settings = (all_settings[lang][key] for key in keys)
        except KeyError:
            raise Exception('Provided language is not supported.')

        return settings

    def get_text(self, urls=None):
        """ Fetch text from sources """
        urls = urls or [source['url'] for source in self.sources]

        if not urls:
            raise Exception('List of URLs must be provided.')

        texts = [urlopen(url).read() for url in urls]

        return b' '.join(texts).decode()

    def get_words(self, text=None):
        """ Get words counter from source texts"""
        text = text or self.get_text()
        words = re.findall(r'\w+', text.lower())

        return Counter(words)

    def get_word_probability(self, word):
        """ Get the probability of a given word """
        if not word:
            raise Exception('Word must be provided.')

        N = sum(self.words.values())
        return self.words[word]/N

    def known_words(self, words):
        """ Get words already known from a given list of words """
        if not words:
            raise Exception('Words array must be provided.')

        return set(word for word in words if word in self.words)

    def level_1_edit(self, word):
        """ Get set of words of one modification from original word """
        if not word:
            raise Exception('Word must be provided.')

        splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
        deletes = [left + right[1:] for left, right in splits if right]
        transposes = [left + right[1] + right[0] + right[2:] for left, right in
                      splits if len(right) > 1]
        replaces = [left + letter + right[1:] for left, right in splits if
                    right for letter in self.letters]
        inserts = [left + letter + right for left, right in splits for letter
                   in self.letters]

        return set(deletes + transposes + replaces + inserts)

    def level_2_edit(self, word):
        """ Get set of words of two modifications from original word """
        if not word:
            raise Exception('Word must be provided.')

        return (level_2 for level_1 in self.level_1_edit(word) for level_2 in
                self.level_1_edit(level_1))

    def get_candidates(self, word):
        """ Get correction candidates of a given word """
        if not word:
            raise Exception('Word must be provided.')

        return (self.known_words([word]) or
                self.known_words(self.level_1_edit(word)) or
                self.known_words(self.level_2_edit(word)) or
                [word])

    def correct(self, word):
        """ Correct word with the top probability candidate """
        if not word:
            raise Exception('Word must be provided.')

        return max(self.get_candidates(word), key=self.get_word_probability)
