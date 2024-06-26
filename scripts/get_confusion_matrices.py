#!/usr/bin/python3

import os
import sys
from collections import defaultdict
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_conll_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    examples = []
    current_example = {}
    intents = defaultdict(int)
    slot_types = defaultdict(int)
    extracted_intents = []
    id_counter = 0

    for line in lines:
        line = line.strip()

        if line.startswith('# intent:'):
            if current_example:
                examples.append(current_example)
                if 'intent' in current_example:
                    extracted_intents.append(current_example['intent'])
                current_example = {}
            intent = line.split(':')[1].strip()
            intents[intent] += 1
            current_example['id'] = id_counter
            current_example['intent'] = intent
            id_counter += 1

        elif line and not line.startswith('#'):
            tokens = line.split('\t')
            # maybe use defaultdict for current_example as well
            current_example.setdefault('tokens', []).append(tokens)
            if len(tokens) == 4:
                slot_type = tokens[3].strip()
                slot_types[slot_type] += 1
            else:
                continue

    if current_example:
        examples.append(current_example)

    return examples


def get_matching_pred_file(language, pred_dir):
    pred_file = language + ".test.conll.out"
    pred_file_path = os.path.join(pred_dir, pred_file)
    return pred_file_path if os.path.exists(pred_file_path) else None


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def process_files(gold_dir, pred_dir, language):
    gold_file_path = os.path.join(gold_dir + '/' + language + ".test.conll")

    if not os.path.isfile(gold_file_path):
        print(f"File for {language}.test.conll does not exist.")
        return None, None

    pred_file_path = get_matching_pred_file(language, pred_dir)

    if pred_file_path:
        gold_examples = analyze_conll_file(gold_file_path)
        pred_examples = analyze_conll_file(pred_file_path)

        gold_intents = [example['intent'] for example in gold_examples]
        pred_intents = [example['intent'] for example in pred_examples]

        if len(gold_intents) != len(pred_intents):
            print(
                f"Warning: Number of intents in gold file ({language}) and pred file ({os.path.basename(pred_file_path)}) do not match.")
            return None, None

        print(f"Processed {language}.test.conll and {os.path.basename(pred_file_path)}")
        return gold_intents, pred_intents
    else:
        print(f"No matching pred file found for {language}")
        return None, None


def create_confusion_matrix(gold_intents, pred_intents):
    unique_intents = sorted(set(gold_intents + pred_intents))
    cm = confusion_matrix(gold_intents, pred_intents, labels=unique_intents)
    return cm


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 get_confusion_matrices.py <gold_dir> <pred_dir> <language>")
        print("Language can be 'en', 'de', 'de-ba', 'de-by', 'de-st', 'gsw', ... depending on content of gold/pred dir!")
        sys.exit(1)

    gold_dir = sys.argv[1]
    pred_dir = sys.argv[2]
    language = sys.argv[3]

    #input the experiment name to be set in title - if not name from pred_dir is taken
    experiment_name = input("Enter Experiment Name to be Set as Plot Title: ")

    if experiment_name:
        experiment = experiment_name
    else:
        experiment = pred_dir.split("/")[-1].split("_")[1:]
        experiment = "_".join(experiment)

    if not os.path.isdir(gold_dir) or not os.path.isdir(pred_dir):
        print("Both arguments for directories must be directories.")
        sys.exit(1)

    gold_intents, pred_intents = process_files(gold_dir, pred_dir, language)

    # Create confusion matrix
    if gold_intents and pred_intents:
        cm = create_confusion_matrix(gold_intents, pred_intents)
        unique_intents = sorted(set(gold_intents + pred_intents))

        # Plot confusion matrix using seaborn
        plt.figure(figsize=(12, 8))
        ax = sns.heatmap(cm, annot=True, cmap='Greys', fmt='d', xticklabels=unique_intents, yticklabels=unique_intents,
                         annot_kws={"fontweight": "bold"})

        # Set x and y axis labels to bold
        ax.set_xticklabels(ax.get_xticklabels(), fontweight='bold')
        ax.set_yticklabels(ax.get_yticklabels(), fontweight='bold')

        plt.title(f'Confusion Matrix over Intents for {language} in Experiment {experiment}\n', fontsize=18, fontweight="bold")
        plt.xlabel('Predicted Intents', fontsize=14, fontweight="bold")
        plt.ylabel('Actual Intents', fontsize=14, fontweight="bold")
        plt.tight_layout()

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        if os.path.exists(desktop_path):
            plt.savefig(os.path.join(desktop_path, language + '_' + experiment + '.png'), dpi=300)
            print(f"Figure saved to {os.path.join(desktop_path, language + '_' + experiment + '.png')}")
        else:
            print("Desktop path does not exist. Figure was not be saved but is displayed.")
            plt.show()
