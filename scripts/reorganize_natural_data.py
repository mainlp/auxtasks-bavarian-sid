#!/usr/bin/python3
import sys

# script to reorganize the natural Bavarian test data so that it fits the eval script
# main reason: de-ba.nat.conll contains an un-annotated example for slots in base version (215)
def reorganize_examples(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if lines[i].startswith("# id"):
                example_id = lines[i].strip()
                intent = lines[i + 1].strip()
                text_en = lines[i + 2].strip()
                text = lines[i + 3].strip()

                # write the example with reorganized structure
                f.write(example_id.replace("id = ", "id: ") + '\n')
                f.write(text_en.replace("text-en = ", "text-en: ") + '\n')
                f.write(text.replace("text = ", "text: ") + '\n')
                f.write(intent.replace("intent = ", "intent: ") + '\n')
                i += 4

                while i < len(lines) and not lines[i].startswith("# id"):
                    f.write(lines[i])
                    i += 1
            else:
                i += 1

        f.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reorganize_natural_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[1]
    reorganize_examples(input_file, output_file)
