#!/usr/bin/env python3
import pandas as pd
import spacy
import os 


def load_data():
    file_path = os.path.join("in", "anne_og_beate.txt")
    # Read the .txt file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove empty lines and lines starting with "@"
    lines = [line.strip() for line in lines if line.strip() and not line.startswith('@')]

    # Split lines into speaker and text using ":"
    data = [line.split(':', 1) for line in lines]

    # Create a pandas dataframe
    df = pd.DataFrame(data, columns=['Speaker', 'Text'])

    # Remove leading and trailing spaces from the columns
    df['Speaker'] = df['Speaker'].str.strip()
    df['Text'] = df['Text'].str.strip()

    return df

def tagging(df):
    # Load the Danish language model
    nlp = spacy.load("da_core_news_sm")

    # Perform POS-tagging
    df["POS"] = df["Text"].apply(lambda x: " ".join([token.pos_ for token in nlp(x)]) if x else "")

    return df


def main():
    df=load_data()
    df = tagging(df)
    output_file = os.path.join("out", "Anne_Beate_POS.csv")
    df.to_csv(output_file, index=False)
    

if __name__ == "__main__":
    main()
