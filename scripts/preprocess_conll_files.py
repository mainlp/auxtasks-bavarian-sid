#!/usr/bin/python3

import sys

# Check if both filename arguments are provided
if len(sys.argv) < 3:
    print("Usage: python3 preprocess_conll_files.py <input_filename> <output_filename>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# open respective conll file from xSID
with open(input_filename, 'r') as f:
    lines = f.readlines()

# modify it for annotation purposes:
# - adds a unique id to each example
# - turns english example '# text: ' to '# text-en: ' and adds a '# text: ' for translated example
# - removes '# slots: ' line with specific slot inidices based on characters

current_id = 1
with open(output_filename, 'w') as f:
    f.write(f'# id: {current_id}\n')
    current_id += 1
    for i, line in enumerate(lines):
        if not line.strip() and i != len(lines) - 1:
            f.write(f'\n# id: {current_id}\n')
            current_id += 1
        elif not line.startswith('# slots:'):
            if line.startswith('# text:'):
                line = line.replace('# text:', '# text-en:')
                f.write(line)
                f.write('# text: \n')
            else:
                f.write(line)
