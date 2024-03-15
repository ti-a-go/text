# Playground for Textual Data Analysis

Python packages that helps you to process textual data using NLP Python libraries like Spacy, Stanza, NLTK etc.

The main interface with the playground is Jupyter notebooks.

The playground have a package to access data from many data sources like wikipedia, twitter, from the disk etc.

### Features

- Process text data using Spacy and Stanza libraries
- Access data from Wikipedia
- Copy a file with textual data into data/ folder and access it from the notebooks
- Get the tokens frequency and other metrics
- Extract n-grams from a text


# Run

```bash
docker compose up
```

### Services

Jupyter Lab

Database

# Data

Sources:
- [x] Wikipedia
- [x] From disk
- [ ] Github
- [ ] Twitter
- [ ] Web scrap
- [ ] Kaggle
- [ ] Public APIs
- [ ] Domínio Público


# Features

## N-grams extractor

The package `ngram` has methods to extract n-grams given simple rules.

```python
from nlp.ngram import bigram, trigram
from nlp.spacy import create_doc
from dataset import wikipedia_page

page = wikipedia_page("Mussum")
doc = create_doc(page.content)
bigrams = bigram(doc)
trigrams = trigram(doc)
```

`bigrams` and `trigrams` variables are lists of tuples.

## Dictionary of Occurrences

One idea is to have a kind of "language dictionary" of occurrences. That is, a place that stores all occurrences of a particular token.

In linguistic analysis sometimes we need to compare several occurrences of a specific word.

So we need to be able to input a word and get a list of all occurrences in the Documents the app have stored.

# Python Interface

## Functions

```python
from dataset import wikipedia_page, datasets, load

from nlp.ngram import bigram, trigram

from nlp.spacy import create_doc
from nlp.spacy.matrics import frequency
from nlp.spacy.matcher import matcher

from nlp.stanza import create_doc

from nlp.nltk import postags
```

## Constants

```python
from nlp.spacy.matcher import patterns
from nlp.spacy.matcher.patterns import DET_NOUN, DET_NOUN_ADJ, ADV_VERB, VERB_ADV
```

# Backlog

## Web Interfaces

The plan is to have others interface like REST API and a user interface.

### REST API Reference

#### Create Document

POST /doc
body:
```json
{
  "text": "Minhi vidis é um livris abertis.",
  "author": "Mussum",
  "genre": "quote"
}
```
response:
```json
{
  "id": "84323e2e-0f14-45d4-b83b-9685c12c9629",
  "text": "Minhi vidis é um livris abertis.",
  "author": "Mussum",
  "genre": "quote"
}
```

#### Get Document

GET /doc/{id}

response
```json
{
   "text":"Minhi vidis é um livris abertis.",
   "ents":[
      {
         "start":0,
         "end":5,
         "label":"LOC"
      }
   ],
   "sents":[
      {
         "start":0,
         "end":32
      }
   ],
   "tokens":[
      {
         "id":0,
         "start":0,
         "end":5,
         "tag":"PROPN",
         "pos":"PROPN",
         "morph":"Gender=Masc|Number=Sing",
         "lemma":"Minhi",
         "dep":"nsubj",
         "head":4
      },
      {
         "id":1,
         "start":6,
         "end":11,
         "tag":"NOUN",
         "pos":"NOUN",
         "morph":"Gender=Masc|Number=Plur",
         "lemma":"vidis",
         "dep":"flat:name",
         "head":0
      },
      {
         "id":2,
         "start":12,
         "end":13,
         "tag":"AUX",
         "pos":"AUX",
         "morph":"Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
         "lemma":"ser",
         "dep":"cop",
         "head":4
      },
      {
         "id":3,
         "start":14,
         "end":16,
         "tag":"DET",
         "pos":"DET",
         "morph":"Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
         "lemma":"um",
         "dep":"det",
         "head":4
      },
      {
         "id":4,
         "start":17,
         "end":23,
         "tag":"NOUN",
         "pos":"NOUN",
         "morph":"Gender=Masc|Number=Plur",
         "lemma":"livris",
         "dep":"ROOT",
         "head":4
      },
      {
         "id":5,
         "start":24,
         "end":31,
         "tag":"ADJ",
         "pos":"ADJ",
         "morph":"Gender=Fem|Number=Sing",
         "lemma":"abertis",
         "dep":"amod",
         "head":4
      },
      {
         "id":6,
         "start":31,
         "end":32,
         "tag":"PUNCT",
         "pos":"PUNCT",
         "morph":"",
         "lemma":".",
         "dep":"punct",
         "head":4
      }
   ]
}
```