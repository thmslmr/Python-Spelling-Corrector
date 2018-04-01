# Spelling Corrector

**Spelling Corrector using the frequence of use of words in a dataset of books.**

Four languages are curently supported :
  - French (default)
  - English
  - Spanish
  - German

It's also possible to use the corrector with custom sources and alphabets for other languages.

Data used
---

- fr :
  * CARPENTIER Nicolas-Joseph, *Dictionnaire du bon language* - [link](http://www.gutenberg.org/files/43926/43926-0.txt)
  * Voltaire, *Candide* - [link](http://www.gutenberg.org/cache/epub/4650/pg4650.txt)
- en :
  * SHAKESPEARE William, *All's Well That Ends Well* - [link](http://www.gutenberg.org/cache/epub/2246/pg2246.txt)
  * SHAKESPEARE William, *Hamlet* - [link](http://www.gutenberg.org/cache/epub/2265/pg2265.txt)
- es :
  * DE CERVANTES Miguel, *Don Quijote* - [link](http://www.gutenberg.org/cache/epub/2000/pg2000.txt)
  * BAROJA Pío, *Los Contrastes de la Vida* - [link](http://www.gutenberg.org/cache/epub/51858/pg51858.txt)
- de :
  * KANT Immanuel, *Kritik der reinen Vernunft* - [link](http://www.gutenberg.org/cache/epub/6342/pg6342.txt)
  * NIETZSCHE Friedrich, *Ecce homo, Wie man wird, was man ist* - [link](http://www.gutenberg.org/cache/epub/7202/pg7202.txt)

Examples of use
---

```python
# French correction
c = Corrector()
c.correct('orthografe')
>> orthographe

# English correction
c = Corrector(lang='en')
c.correct('mroinng')
>> morning
```

References
---

Spelling corrector based on that of [Peter Norvig](http://norvig.com/)
