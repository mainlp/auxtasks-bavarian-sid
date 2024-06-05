#!/usr/bin/python3

import sys
import os
import random


# script to train-dev split cleaned bar_maibaam-ud-test.conllu data with a 90-10 split for aux task training

def read_conllu_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().strip().split('\n\n')
    return data


def write_conllu_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        count = 0
        for example in data:
            count += 1
            f.write(example + '\n\n')
        print("Wrote ", count, "examples to ", filename)


def filter_examples(data):
    print("All examples: ", len(data))
    # simply filtering for examples that start with # sent_id = xsid
    # come from xSID data and could mess up SID task results there!
    filtered = [example for example in data if not example.startswith('# sent_id = xsid')]
    print("Filtered examples: ", len(filtered))

    return filtered


def split_data(data, train_ratio=0.9):
    random.shuffle(data)
    split_idx = int(train_ratio * len(data))
    return data[:split_idx], data[split_idx:]


def main(input_filename):
    data = read_conllu_file(input_filename)
    filtered_data = filter_examples(data)
    train_data, valid_data = split_data(filtered_data)

    output_dir = os.path.dirname(input_filename)
    base_name = os.path.splitext(os.path.basename(input_filename))[0]
    base_name = base_name.replace('-test', '')

    train_filename = os.path.join(output_dir, f"{base_name}-train.conllu")
    valid_filename = os.path.join(output_dir, f"{base_name}-valid.conllu")

    write_conllu_file(train_filename, train_data)
    write_conllu_file(valid_filename, valid_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 testsplit_conllu.py <input_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    main(input_filename)
