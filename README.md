# Python-Spelling-Corrector

Correcteur orthographique basé sur celui de [Peter Norvig](http://norvig.com/)

Présentation
------------

Coming soon

Données utilisées
-----------------

* [Dictionnaire du bon language - N-J. Carpentier](http://www.gutenberg.org/files/43926/43926-0.txt)
* [Candide - Voltaire](http://www.gutenberg.org/cache/epub/4650/pg4650.txt)

Résultats
---------
```python
c = Corrector()

c.correct('orthografe')
>> orthographe

c.correct('bnojou')
>> bonjour
```
