#!/usr/bin/python3
import sys

# script to reorganize xSID test/valid data so that it fits the eval script
def reorganize_examples(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if lines[i].startswith("# "):

                # write the line with reorganized structure ('# id:' instead of '# id =')
                f.write(lines[i].strip().replace(" =", ":") + '\n')
                i += 1

                while i < len(lines) and not lines[i].startswith("# "):
                    f.write(lines[i])
                    i += 1
            else:
                i += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reorganize_xsid_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[1]
    reorganize_examples(input_file, output_file)
