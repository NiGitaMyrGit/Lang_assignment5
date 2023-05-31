# Lang_assignment5 - Danish Conversational data, extensions and limitations
This is the repository for the fifth assignment in the course Language Analytics from the bachelors elective course Cultural Data Science at Aarhus University

## 1. Contributions
The code was written independently by me.
**Help Sources**
freeCodeCamp.org: "Natural Language Processing with spaCy & Python - Course for Beginners" https://www.youtube.com/watch?v=dIUTsFT2MeQ

## 2. Methods
As your everyday linguist, I wanted to test out what the extension and limits of current models are, when trying having to a Danish conversation manuscript. 
The transcript provided as a textfile 'anne_og_beate.txt' in the folder ```in```. T
I have used the Danish spaCy model `nlp = spacy.load("da_core_news_sm")` to perform POS-tagging and dependency Parsing. 
**Part-Of-Speech (POS)** tagging is a grammatical tagging of lexemes with the following categories:
  ADJ: adjective
  ADP: adposition
  ADV: adverb
  AUX: auxiliary
  CCONJ: coordinating conjunction
  DET: determiner
  INTJ: interjection
  NOUN: noun
  NUM: numeral
  PART: particle
  PRON: pronoun
  PROPN: proper noun
  PUNCT: punctuation
  SCONJ: subordinating conjunction
  SYM: symbol
  VERB: verb
  X: other
 *source* [Universal POS tags](https://universaldependencies.org/u/pos/)

**Dependency Parsing** is a Natural Language Processing (NLP) texhnique that analyse the grammatical *structures* of the syntax, and how the words in a sentence depend on each other and form a structure. The dependy parsing both POS-tag, gives a dependy label and a head token.
For the sentiment analysis I have implented [Sentida](https://github.com/Guscode/Sentida), a Danish sentiment analysis tool, which provide a positive score (<0.0 or a negative score >0.0)
To convert the `.txt-file` to a dataframe the pandas command `pd.DataFrame()` was used.

  ROOT: Root of a sentence or a clause
  acl: Clausal modifier of noun
  acomp: Adjectival complement
  advcl: Adverbial clause modifier
  advmod: Adverbial modifier
  agent: Agent
  amod: Adjectival modifier
  appos: Appositional modifier
  attr: Attribute
  aux: Auxiliary
  auxpass: Auxiliary (passive)
  case: Case marker
  cc: Coordinating conjunction
  ccomp: Clausal complement
  compound: Compound
  conj: Conjunct
  csubj: Clausal subject
  csubjpass: Clausal subject (passive)
  dative: Dative
  dep: Unspecified dependency
  det: Determiner
  dobj: Direct object
  expl: Expletive
  intj: Interjection
  mark: Marker
  meta: Meta modifier
  neg: Negation modifier
  nmod: Nominal modifier
  npmod: Noun phrase as adverbial modifier
  nsubj: Nominal subject
  nsubjpass: Nominal subject (passive)
  nummod: Numeric modifier
  oprd: Object predicate
  parataxis: Parataxis
  pcomp: Complement of preposition
  pobj: Object of preposition
  poss: Possession modifier
  preconj: Preconjunct
  predet: Predeterminer
  prep: Prepositional modifier
  prt: Particle
  punct: Punctuation
  quantmod: Modifier of quantifier
  relcl: Relative clause modifier
  xcomp: Open clausal complement
*source* [spaCy Label Scheme](https://spacy.io/models/en#en_core_web_lg)

### 2.1 Data
The data was retrieved from [Samtalebank](https://samtalebank.talkbank.org/access/Sam2.html) in the folder called "Sam2" which is a collection of transcriptions of Danish conversations. The transcripts are equipped with a set of symbols and special characters, that showcases notational symbols for pronunciational and temporal features of speech. Since no models are able to interpret these symbols (for now), the conventions for which symbols to use varies, and I am not a programmer these symbols have been removed by simply searching and replacing.
The transcripts where, when downloaded, in a '.cha' format, which is the format used for the transcription software CLAN. The files can be converted either by running the command `CHAT2TEXT` inside the software, or simply be changing the file extension and opening the file in a text-editor. 

## 3. Usage
The scripts where made in python 3.10.7. Should any errors occur, contrary to expectation, when running the script, please try to install this python version.
### 3.1 Install packages
From the command line, make sure your arel ocated in the main directory. Run the command `bash setup.sh` to install the required packages.
### 3.2 Run the scripts
In the folder ```src```, three pythonscripts are located: ```pos_tag.py```, ```dendency_gone_wrong.py``` and ```sentiment.py```. The `pos_tag.py` script outputs a .csv-table called Anne_og_Beate_POS.csv, with a column on the right called "POS" where it 


## 3.3  Results discussion
The POS-tagging is working ok and Sentiment analysis with the Danis sentiment analysis also ok. 
I have had problems in how I could make the output a CSV-file without overcomplicating things. Especially with the sentiment analysis it proved hard, since the sentida will not work with a pandas dataframe. This is also why the output only have two columns "Text" and "Sentiment". It's too bad, since thsi means the sentiment analysis was also run on the speaker. Luckily the speakers doesn't form any meaningful word, and should not skew the results too much.
A problem though, is the fact that the transcript is not always written not as real words, but in some contexts rely on the way they sound such as `å` being `og`(*and*). This mostly occurs with conjunctions, and more complicated words, if pronounced 'normally' follow the danish dictionary. If I wanted to improve things, I probably should've made a stopwordlist. Though I tried to remove trailing white-space, it seems that some trailing white-space still persist.


### 3.2 POS tagging
The Pos tagging seems to work rather well with only minor mistakes, both due to the pronouncial spellings and interjections such as 'øh' or 'øhm'(*uhm*). When these interjections occur, it seems to give it a random POS-tag.These words should've been sorted out in a non-existent data augmentation process.
Example:
|1|Speaker|Text|Sentiment|
|---|---|---|---|
|5|BE|å så tænker jeg hva fanden jeg skal lave den her øh feature om|ADP ADV VERB PRON VERB NOUN PRON AUX VERB DET ADV NOUN NOUN ADP|

The words are parsed mostly correct. The 'å' which in correct ortographic spelling would be an 'og' (*and*) is said to be an adposition though it is and adverb. This is understandable, since the model is trained on ortographic spelling.
'hva' is furthermore an auditory spelling, which in ortographic manners would have been an 'hvad'(*what*) is a pronoun but is labeles as a verb. Here it can also be seen how the 'øh' is parsed as an adverb. 

The results are, given the fact that this is not ortographic data, pretty okay, and the mdoel is able to grasp the big picture.
### 3.3 dependency parsing
The dependency parsing does not yield any amaxing results. I ended up uploading it, to showcase when things go rather awry, and to showcase the limitations when working with semi-augmented conversational data. 
The dependency parsing do POS tagging like seen in the previous section and also some Dependency labeling, but rather poorly.
Example

|1|Speaker|Text|Token|POS|Dependency Label|Head|
|---|---|---|---|---|---|---|
|2|*AN|havde du egentlig øh nået a lave dine feature|"|AUX PRON ADV VERB VERB X VERB DET NOUN|aux nsubj advmod ROOT xcomp nmod:poss punct|det obl	øh øh øh øh øh feature a feature nået|



### 3.4 sentiment analysis
An example from the ```Anne_og_Beate_sentiment.csv```
|1|Text|Sentiment|
|---|---|---|
|377|*AN :ah men det var så klamt også bare da jeg så billedet var jeg|	-0.4833333333333333|
|379|*AN : ved at brække mig igen|-0.533333333333334|
|385|*AN :hold kæft jeg synes det var godt de andre altså|0.26111111111111146|
|386|:sådan Anders Fogh gjorde det var helt vildt godt|	0.3500000000000003|

Since the sentence i line 377 and 379 contains the lexemes 'klamt' and 'brække', it would make senese that these are rated negatively, while the sentences in line 385 and 386 contains the lexemes 'godt' and 'vildt godt' these rated as positive. Furthermore I am impressed that the sentiment analysis rate line 386 higher than 385, where the adverb 'vildt' modifies that adjective 'godt', and (probably) by that rates the sentence as more postive than without the adverb.
The results are far from perfect, but it works to an extend.

For the 


## 4. Contact
For any questions, please write Nikita J. Myrting on the email: 201906799@post.au.dk.
