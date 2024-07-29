#!/usr/bin/python3

# a short script to reorganize the Bavarian natural evaluation data to fit to the evaluation method of this work

import sys
from collections import defaultdict

# script to reorganize the natural Bavarian test data so that it fits the eval script
# main reason: de-ba.nat.conll contains an un-annotated example for slots in base version (215)
def analyze_conll_file(file_path):
    examples = []
    current_example = defaultdict(list)

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

            elif line.startswith('# text-en:'):
                text_en = line.split(':')[-1].strip()
                current_example['text-en'] = text_en

            # Skip other lines starting with #
            elif line.startswith('#'):
                continue

            # Check if line starts with a digit
            elif line and line[0].isdigit():
                tokens = [token.strip() for token in line.split('\t')]
                if len(tokens) == 3 and 'intent' in current_example and tokens[2].strip() == current_example['intent']:
                    # if there is only 3 elements annotated and the intent as third element is correct,
                    # add "O" as default for the slot label! (seems that there were problems in 1 example)
                    tokens.append("O")
                elif len(tokens) != 4:
                    continue
                if 'text' not in current_example:
                    current_example['text'] = tokens[1]
                else:
                    current_example['text'] += ' ' + tokens[1]

                current_example['tokens'].append(tokens)

            elif not line:
                if current_example:
                    examples.append(dict(current_example))
                    current_example = defaultdict(list)

    return examples

def write_examples(examples, output_file):
    with open(output_file, 'w') as f:
        for example in examples:
            f.write(f"# id: {example['id']}\n")
            f.write(f"# text: {example['text']}\n")
            if 'text-en' in example:
                f.write(f"# text-en: {example['text-en']}\n")
            f.write(f"# intent: {example['intent']}\n")
            for tokens in example['tokens']:
                f.write('\t'.join(tokens) + '\n')
            f.write('\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reorganize_natural_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[1]

    examples = analyze_conll_file(input_file)
    write_examples(examples, output_file)
