#!/usr/bin/python3

# a short script to prepare the mlm data in order to include as many structurally different sentences to the training data as possible

import sys
import pandas as pd

def read_data(path):
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"Error reading Bavarian-German CSV file: {e}")
        return None

def sort_sentences(data):
    # function that sorts the sentences being written into the mlm train file
    # it takes all of those that are annotated as being different in structure to German first
    # background - these should always be used within MaChAmp for MLM even though max_sents is reduced a lot
    different_sentences = []
    similar_sentences = []
    sentence_count = 0
    for _, row in data.iterrows():
        sentence = row['Bavarian'].strip() + '\n'
        if ((row['Grammar differs?'] == True and row['Reasons?'] == '') or
                (row['Grammar differs?'] == True and row['Reasons?'] != '')):
            different_sentences.append(sentence)
            sentence_count += 1
        else:
            similar_sentences.append(sentence)
            sentence_count += 1

    sorted_sentences = different_sentences + similar_sentences
    print(f"Collected {sentence_count} sentences. The first {len(different_sentences)} sentences are examples in which Bavarian differs structurally from German.")

    return sorted_sentences

def write_to_file(sentences, path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(''.join(sentences))
        print(f"{len(sentences)} Bavarian sentences successfully written to {path}")
    except Exception as e:
        print(f"Error writing Bavarian MLM Data to file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 testsplit_conllu.py <input_file_path> <output_dirextory_path>")
        sys.exit(1)

    path_to_bar = sys.argv[1]
    test_save_path = sys.argv[2] + "mlm_bar_ann_1_test.txt"
    train_save_path = sys.argv[2] + "mlm_bar_ann_1_train.txt"
    dev_save_path = sys.argv[2] + "mlm_bar_ann_1_dev.txt"

    data = read_data(path_to_bar)
    if data is None:
        exit()

    sorted_sentences = sort_sentences(data)
    total_sentences = len(sorted_sentences)

    # Splitting overall test data intp into train and dev data, 90-10
    train_size = int(0.9 * total_sentences)
    train_sentences = sorted_sentences[:train_size]
    dev_sentences = sorted_sentences[train_size:]

    write_to_file(sorted_sentences, test_save_path)
    write_to_file(train_sentences, train_save_path)
    write_to_file(dev_sentences, dev_save_path)
