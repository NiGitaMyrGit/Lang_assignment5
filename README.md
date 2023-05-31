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
Part-Of-Speech (POS) tagging is a grammatical tagging of lexemes. 
Dependency Parsing is a Natural Language Processing (NLP) texhnique that analyse the grammatical *structures* of the syntax, and how the words in a sentence depend on each other and form a structure. The dependy parsing both POS-tag, gives a dependy label and a head token.
For the sentiment analysis I have implented [Sentida](https://github.com/Guscode/Sentida), a Danish sentiment analysis tool, which provide a positive score (<0.0 or a negative score >0.0)
To convert the `.txt-file` to a dataframe the pandas command `pd.DataFrame()` was used.

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
A problem though, is the fact that the transcript is not always written not as real words, but in some contexts rely on the way they sound such as `å` being `og`. This mostly occurs with conjunctions, and more complicated words, if pronounced 'normally' follow the danish dictionary. If I wanted to imporve things, I probably should've made a stopwordlist.
An example from 
|Text|Sentiment|
|---|---|
|AN :hold kæft jeg synes det var godt de andre altså|0.26111111111111146|
|:sådan Anders Fogh gjorde det var helt vildt godt|	0.3500000000000003|


## 4. Contact
For any questions, please write Nikita J. Myrting on the email: 201906799@post.au.dk.
