# Lang_assignment5 - Danish Conversational data, extensions and limitations
This is the repository for the fifth assignment in the course Language Analytics from the bachelors elective course Cultural Data Science at Aarhus University

## 1. Contributions
The code was written independently by me. 
## 2. Methods
As your everyday linguist, I wanted to test out what the extension and limits of current models are, when trying having to a Danish conversation manuscript. 
The transcript provided as a textfile 'anne_og_beate.txt' in the folder ```in```. T
I have used the Danish spaCy model `nlp = spacy.load("da_core_news_sm")` to perform POS-tagging and dependency tagging. 
For the sentiment analysis I have implented [Sentida](https://github.com/Guscode/Sentida), a Danish sentiment analysis tool. 
To convert the .txt-file to a dataframe the pandas command `pd.DataFrame()` was used.

### 2.1 Data
The data was retrieved from [Samtalebank](https://samtalebank.talkbank.org/access/Sam2.html) in the folder called "Sam2" which is a collection of transcriptions of Danish conversations. The transcripts are equipped with a set of symbols and special characters, that showcases notational symbols for pronunciational and temporal features of speech. Since no models are able to interpret these symbols (for now), the conventions for which symbols to use varies, and I am not a programmer these symbols have been removed by simply searching and replacing.
The transcripts where, when downloaded, in a '.cha' format, which is the format used for the transcription software CLAN. The files can be converted either by running the command `CHAT2TEXT` inside the software, or simply be changing the file extension and opening the file in a text-editor. 

## 3. Usage
The scripts where made in python 3.10.7. Should any errors occur, contrary to expectation, when running the script, please try to install this python version.
### 3.1 Install packages
From the command line, make sure your arel ocated in the main directory. Run the command `bash setup.sh` to install the required packages.
### 3.2 Run the scripts
In the folder ```src``` the 
In the main directory 

## 3.3  Results discussion
Dependecy parsinG is a no go, but POS-tagging is working ok and sentiment analysis with the danis hsentiment analysis 
