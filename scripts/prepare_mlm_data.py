#!/usr/bin/python3

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
        print(f"{len(sentences)} Bavarian MLM Data successfully written to {path}")
    except Exception as e:
        print(f"Error writing Bavarian MLM Data to file: {e}")
def main():
    path_to_bar = '../dialect-BLI/labelled_data/bitext/bar/ann_1.csv'
    #test_save_path = "../manual_data/MLM_data/mlm_bar_ann_1_test.txt"
    train_save_path = "../manual_data/MLM_data/mlm_bar_ann_1_train.txt"
    dev_save_path = "../manual_data/MLM_data/mlm_bar_ann_1_dev.txt"

    data = read_data(path_to_bar)
    if data is None:
        return

    #write_to_file(sort_sentences(data), test_save_path)

    sorted_sentences = sort_sentences(data)
    total_sentences = len(sorted_sentences)

    # Splitting into train and dev data
    train_size = int(0.9 * total_sentences)
    train_sentences = sorted_sentences[:train_size]
    dev_sentences = sorted_sentences[train_size:]

    write_to_file(train_sentences, train_save_path)
    write_to_file(dev_sentences, dev_save_path)

if __name__ == "__main__":
    main()
