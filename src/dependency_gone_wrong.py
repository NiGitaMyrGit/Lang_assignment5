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


def perform_dependency_parsing(df):
    # Load the Danish language model
    nlp = spacy.load("da_core_news_sm")

    # Create new columns for the dependency parsing results
    df['Token'] = ''
    df['POS'] = ''
    df['Dependency Label'] = ''
    df['Head'] = ''

    # Iterate over the rows in the DataFrame
    for index, row in df.iterrows():
        text = row['Text']

        # Skip empty values
        if not text:
            continue

        doc = nlp(text)

        # Extract token, POS, dependency label, and head for each token
        tokens = [token.text for token in doc]
        pos = [token.pos_ for token in doc]
        dep_labels = [token.dep_ for token in doc]
        heads = [token.head.text for token in doc]

        # Assign the parsed values to the corresponding DataFrame columns
        df.at[index, 'Token'] = " ".join(tokens)
        df.at[index, 'POS'] = " ".join(pos)
        df.at[index, 'Dependency Label'] = " ".join(dep_labels)
        df.at[index, 'Head'] = " ".join(heads)

    return df



def main():
    df = load_data()
    df = perform_dependency_parsing(df)
    output_file = os.path.join("out", "Anne_Beate_dependency.csv")
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    main()
