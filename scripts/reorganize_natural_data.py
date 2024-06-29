#!/usr/bin/python3

import sys
from collections import defaultdict

# script to reorganize the natural Bavarian test data so that it fits the eval script
# main reason: de-ba.nat.conll contains an un-annotated example for slots in base version (215)
def analyze_conll_file(file_path):
    examples = []
    current_example = defaultdict(list)  # Initialize current_example as defaultdict with list

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith('# id:'):
                id = line.split(':')[-1].strip()
                current_example['id'] = id

            elif line.startswith('# intent:'):
                intent = line.split(':')[-1].strip()
                current_example['intent'] = intent

            elif line.startswith('# text:'):
                text = line.split(':')[-1].strip()
                current_example['text'] = text

            elif line.startswith('#'):
                continue  # Skip other lines starting with #

            elif line and line[0].isdigit():  # Check if line starts with a digit
                tokens = line.split('\t')
                current_example['tokens'].append(tokens)

            elif not line:
                if current_example:  # Append current_example if it's not empty
                    examples.append(dict(current_example))  # Convert defaultdict to regular dict
                    current_example = defaultdict(list)  # Reset current_example for next example


    print(examples[:5])

    return examples

def write_examples(examples):
    with open(sys.argv[1], 'w') as f:
        for example in examples:
            f.write(example + '\n')
            #Todo

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reorganize_natural_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[1]
    analyze_conll_file(input_file)
    #write_examples(analyze_conll_file(output_file))
