#!/usr/bin/python3
import sys

def reorganize_examples(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(input_file, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if lines[i].startswith("# id"):
                example_id = lines[i].strip()
                text_en = lines[i + 2].strip()
                text = lines[i + 3].strip()
                intent_line = lines[i + 1].strip()

                # find the intent line
                while not intent_line.startswith("# intent"):
                    i += 1
                    intent_line = lines[i].strip()

                # write the example with reorganized structure
                f.write(example_id.replace("id = ", "id: ") + '\n')
                f.write(text_en.replace("text_en = ", "text_en: ") + '\n')
                f.write(text.replace("text = ", "text: ") + '\n')
                f.write(intent_line.replace("intent = ", "intent: ") + '\n')

                # move to the next example:
                i += 4
                while i < len(lines) and not lines[i].startswith("# id"):
                    f.write(lines[i])
                    i += 1
            else:
                i += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reorganize_miriams_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    reorganize_examples(input_file)
