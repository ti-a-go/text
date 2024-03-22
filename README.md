# Natural Language Processing

REST API to process and analyse textual data.

# NLP Tasks

- Tokenization
- Part of Speech
- Dependency Parse
- Named Entity Recognition
- N-grams

# Linguístic Analysis

1. Get the tokens frequency and other metrics
2. Token catalog: find occurrences of a given token in a group of documents
3. Token patterns


# Run

```bash
docker compose up
```

# Data Sources

Sources:
- [ ] Wikipedia
- [ ] From disk
- [ ] Github
- [ ] Twitter
- [ ] Web scrap
- [ ] Kaggle
- [ ] Public APIs
- [ ] Domínio Público


# N-grams

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

# Token Occurrences

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
from nlp.spacy.tokens import get_occurrences

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
