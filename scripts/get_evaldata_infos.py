#!/usr/bin/python3

import sys
from collections import defaultdict

def analyze_conll_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    examples = []
    current_example = {}
    intents = defaultdict(int)
    slot_types = defaultdict(int)
    id_counter = 0

    for line in lines:
        if line.startswith('# id:'):
            id_counter += 1
            if current_example:
                examples.append(current_example)
                current_example = {}
            current_example['id'] = int(line.split(':')[1].strip())

        elif line.startswith('# intent:'):
            intent = line.split(':')[1].strip()
            intents[intent] += 1
            current_example['intent'] = intent

        elif line.strip() and not line.startswith('#'):
            tokens = line.split('\t')
            current_example.setdefault('tokens', []).append(tokens)
            if len(tokens) != 4:
                print(
                    f"Error: Incorrectly annotated line - more or less than 4 columns in example {current_example['id']}: \n{line}\n Slot cannot be extracted correctly.")
            else:
                slot_type = tokens[3].strip()
                slot_types[slot_type] += 1

    if current_example:
        examples.append(current_example)

    return id_counter, intents, slot_types


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_evaldata_infos.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    id_counter, intents, slot_types = analyze_conll_file(file_path)

    print(f"Number of examples: {id_counter}")
    print(f"Intents ({len(intents)}):")
    for intent, count in sorted(intents.items(), key=lambda item: item[1], reverse=True):
        print(f"  {intent}: {count}")

    print(f"Slot Types ({len(slot_types)}):")
    for slot_type, count in sorted(slot_types.items(), key=lambda item: item[1], reverse=True):
        print(f"  {slot_type}: {count}")
