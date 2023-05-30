#!/usr/bin/env python3
import pandas as pd
from sentida import Sentida
import os

def load_data(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        lines = df['Text'].tolist()
    else:
        raise ValueError("Unsupported file format. Only .txt and .csv files are supported.")

    lines = [line.strip() for line in lines if line.strip()]
    return lines

def perform_sentiment_analysis(texts):
    sentida = Sentida()
    sentiments = []

    for text in texts:
        sentiment = sentida.sentida(text)
        sentiments.append(sentiment)

    return sentiments


def main():
    file_path = os.path.join("in", "anne_og_beate.txt")
    data = load_data(file_path)
    sentiments = perform_sentiment_analysis(data)

    # Alternatively, you can save the results to a CSV file
    output_data = pd.DataFrame({'Text': data, 'Sentiment': sentiments})
    output_file_path = os.path.join("out", "Anne_og_Beate_sentiment.csv")  # Update with the desired output file path
    output_data.to_csv(output_file_path, index=False)


if __name__ == "__main__":
    main()