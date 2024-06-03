#!/usr/bin/python3

import re
import pandas as pd


def read_data(path):
    """Read data from a Feather file."""
    try:
        data = pd.read_feather(path)
        return data
    except Exception as e:
        print(f"Error reading the Feather file: {e}")
        return None


def filter_sentences(data):
    """Filter sentences that contain letters."""
    regex = re.compile('[a-zA-Z]')
    filtered_sentences = []
    for _, row in data.iterrows():
        sentence = row['sentence'].strip()
        if regex.search(sentence):
            filtered_sentences.append(sentence)
    return filtered_sentences


def write_to_file(sentences, path):
    """Write the filtered sentences to a text file."""
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(' '.join(sentences))
        print(f"File successfully written to {path}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    # Path to the Feather file
    path_to_bar = "../bar"
    # Path to save the concatenated text
    bar_save_path = "../bar.txt"

    # Read the data
    data = read_data(path_to_bar)
    if data is None:
        return

    # Filter sentences
    sentences = filter_sentences(data)

    # Write to file
    write_to_file(sentences, bar_save_path)


if __name__ == "__main__":
    main()
