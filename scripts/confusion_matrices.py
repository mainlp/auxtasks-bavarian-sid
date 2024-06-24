#!/usr/bin/python3

import os
import sys
from collections import defaultdict
import numpy as np
import pandas as pd


def analyze_conll_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    examples = []
    current_example = {}
    intents = defaultdict(int)
    slot_types = defaultdict(int)
    id_counter = 0
    extracted_intents = []

    for line in lines:
        if line.startswith('# id:') or line.startswith('# text:'):
            id_counter += 1
            if line.startswith('# id:'):
                if current_example:
                    examples.append(current_example)
                    if 'intent' in current_example:
                        extracted_intents.append(current_example['intent'])
                    current_example = {}
                current_example['id'] = int(line.split(':')[1].strip())
            elif line.startswith('# text:'):
                if current_example:
                    examples.append(current_example)
                    if 'intent' in current_example:
                        extracted_intents.append(current_example['intent'])
                    current_example = {}
                current_example['id'] = int(id_counter)

        elif line.startswith('# intent:'):
            intent = line.split(':')[1].strip()
            intents[intent] += 1
            current_example['intent'] = intent

        elif line.strip() and not line.startswith('#'):
            tokens = line.split('\t')
            current_example.setdefault('tokens', []).append(tokens)
            #if len(tokens) != 4:
                #print(f"Error: Incorrectly annotated line - more or less than 4 columns in example {current_example['id']}: \n{line}Slot cannot be extracted correctly.")
            #else:
            slot_type = tokens[3].strip()
            slot_types[slot_type] += 1

    if current_example:
        examples.append(current_example)
        if 'intent' in current_example:
            extracted_intents.append(current_example['intent'])

    return examples, intents, slot_types, extracted_intents


def get_matching_pred_file(gold_file, pred_dir):
    pred_file = gold_file + ".out"
    pred_file_path = os.path.join(pred_dir, pred_file)
    return pred_file_path if os.path.exists(pred_file_path) else None


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def process_files(gold_dir, pred_dir):
    gold_files = os.listdir(gold_dir)
    gold_files = [gold_file for gold_file in gold_files if gold_file.endswith('test.conll')]

    gold_intents = []
    pred_intents = []

    for gold_file in gold_files:
        print(gold_file)
        gold_file_path = os.path.join(gold_dir, gold_file)

        if not os.path.isfile(gold_file_path):
            continue

        pred_file_path = get_matching_pred_file(gold_file, pred_dir)

        if pred_file_path:
            gold_result = analyze_conll_file(gold_file_path)
            pred_result = analyze_conll_file(pred_file_path)

            _, gold_intents_dict, _, gold_extracted_intents = gold_result
            _, pred_intents_dict, _, pred_extracted_intents = pred_result

            if len(gold_extracted_intents) != len(pred_extracted_intents):
                print(
                    f"Warning: Number of intents in gold file ({gold_file}) and pred file ({os.path.basename(pred_file_path)}) do not match.")
                continue

            gold_intents.extend(gold_extracted_intents)
            pred_intents.extend(pred_extracted_intents)

            print(f"Processed {gold_file} and {os.path.basename(pred_file_path)}")
        else:
            print(f"No matching pred file found for {gold_file}")

    return gold_intents, pred_intents


def create_confusion_matrix(gold_intents, pred_intents):
    unique_intents = sorted(set(gold_intents + pred_intents))
    intent_to_index = {intent: idx for idx, intent in enumerate(unique_intents)}

    confusion_matrix = np.zeros((len(unique_intents), len(unique_intents)), dtype=int)

    for gold_intent, pred_intent in zip(gold_intents, pred_intents):
        i = intent_to_index[gold_intent]
        j = intent_to_index[pred_intent]
        confusion_matrix[i, j] += 1

    df_confusion = pd.DataFrame(confusion_matrix, index=unique_intents, columns=unique_intents)
    return df_confusion


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 evaluate_files.py <gold_dir> <pred_dir>")
        sys.exit(1)

    gold_dir = sys.argv[1]
    pred_dir = sys.argv[2]

    if not os.path.isdir(gold_dir) or not os.path.isdir(pred_dir):
        print("Both arguments must be directories.")
        sys.exit(1)

    gold_intents, pred_intents = process_files(gold_dir, pred_dir)
    confusion_matrix = create_confusion_matrix(gold_intents, pred_intents)

    print("Confusion Matrix:")
    print(confusion_matrix)
