#!/usr/bin/python3

import re
import pandas as pd


def read_data(path):
    try:
        data = pd.read_feather(path)
        return data
    except Exception as e:
        print(f"Error reading the Feather file: {e}")
        return None


def filter_sentences(data):
    regex = re.compile('[a-zA-Z]')
    filtered_sentences = []
    sentence_count = 0
    for _, row in data.iterrows():
        sentence = row['sentence'].strip()
        if regex.search(sentence):
            filtered_sentences.append(sentence)
            sentence_count += 1
    print(f"Collected {sentence_count} sentences that consist of at least one word.")
    return filtered_sentences


def write_to_file(sentences, path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(' '.join(sentences))
        print(f"Bavarian MLM Data successfully written to {path}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    path_to_bar = "../bar"
    bar_save_path = "../bar.txt"

    data = read_data(path_to_bar)
    if data is None:
        return
    sentences = filter_sentences(data)
    write_to_file(sentences, bar_save_path)


if __name__ == "__main__":
    main()
