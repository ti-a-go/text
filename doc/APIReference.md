# API Reference

## Create Document

`POST /doc`

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

## Get Document

`GET /doc/{id}`

response
```json
{
  "id":"b5d070ef-056e-43bf-a902-70f069ab9939",
  "genre":"quote",
  "author":"Mussum",
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

## List Documents

`GET /docs`

response
```json
[
   {
      "id":"972385c4-4c0f-4d27-aec4-3c3adf9eef97",
      "title":"Brasil",
      "genre":"Wikipedia page"
   },
   {
      "id":"a3d39d44-1796-4f04-a371-5760305cb27f",
      "title":"Mexico",
      "genre":"Wikipedia page"
   },
   {
      "id":"769bbac6-406c-4154-b210-03aee6e07bb0",
      "title":"Egito",
      "genre":"Wikipedia page"
   }
]
```

## Search Document

`GET /doc/search

body:
```json
{
  "title": "Dom Casmurro",
  "genre": "novel",
  "author":"Machado de Assim"
}
```

response
```json
[
   {
      "id":"886624cd-821a-4ca1-b982-61c01faf1726",
      "genre": "novel",
      "author":"Machado de Assim"
   }
]
```