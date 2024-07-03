#!/usr/bin/python3

import sys
import re


def tokenize_text(text):
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return tokens


# Check if a filename argument is provided
if len(sys.argv) < 2:
    print("Usage: python3 postprocess_conll_files.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Open the specified file
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

# Collect all examples
examples = []
current_example = {}

for line in lines:
    if line.startswith('# id:'):
        if current_example:
            examples.append(current_example)
            current_example = {}
        current_example['id'] = int(line.split(':')[1].strip())

    elif line.startswith('# text:'):
        current_example['text'] = line.split(':', 1)[1].strip()

    elif line.strip() and not line.startswith('#'):
        current_example.setdefault('tokens', []).append(line.split('\t'))
        if len(line.split('\t')) != 4:
            print(
                f"Error: Incorrectly annotated line - more or less than 4 columns in example {current_example['id']}: \n{line}")

# Check annotations
for example in examples:
    if not example['text']:
        print(f"Error: Missing translation for example {example['id']}")
    else:
        translation = example['text']
        translation_tokens = tokenize_text(translation)

        if not example['tokens']:
            print(f"Error: No annotations found for example {example['id']}")
            continue

        annotation_tokens = [token[1] for token in example['tokens']]

        # Check for mismatches
        mismatches = []
        min_length = min(len(translation_tokens), len(annotation_tokens))

        for index in range(min_length):
            if translation_tokens[index] != annotation_tokens[index]:
                mismatches.append(
                    {'index': index, 'expected': translation_tokens[index], 'actual': annotation_tokens[index]})

        if len(translation_tokens) > len(annotation_tokens):
            for index in range(min_length, len(translation_tokens)):
                mismatches.append({'index': index, 'expected': translation_tokens[index], 'actual': None})

        elif len(annotation_tokens) > len(translation_tokens):
            for index in range(min_length, len(annotation_tokens)):
                mismatches.append({'index': index, 'expected': None, 'actual': annotation_tokens[index]})

        if mismatches:
            for mismatch in mismatches:
                print(
                    f"Error: Tokens mismatch for example {example['id']} at index {mismatch['index'] + 1}: Expected '{mismatch['expected']}' but got '{mismatch['actual']}'")

        # Check for correct annotation IDs
        annotation_ids = list(map(int, [token[0] for token in example['tokens']]))

        for i in range(1, len(annotation_ids)):
            if annotation_ids[i] != annotation_ids[i - 1] + 1 or annotation_ids[i] < annotation_ids[i - 1] or \
                    annotation_ids[i] <= annotation_ids[i - 1]:
                print(f"Error: Incorrect annotation IDs in example {example['id']}")

