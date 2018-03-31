# Python-Spelling-Corrector

**Correcteur orthographique utilisant la fréquence d'utilisation des mots dans un dataset de livres.**

Quatre langues sont actuellements supportées :
  - Français
  - Anglais
  - Espagnol
  - Allemand

Il est aussi possible d'utiliser ce correcteur avec les sources et l'alphabet de son choix et ainsi l'utiliser pour d'autre langue.

Données utilisées
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
  
Example d'utilisation
---

```python
c = Corrector()

c.correct('orthografe')
>> orthographe

c.correct('bnojou')
>> bonjour
```

Référence
---

Correcteur orthographique basé sur celui de [Peter Norvig](http://norvig.com/)
