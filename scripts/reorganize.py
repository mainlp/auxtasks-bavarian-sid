def reorganize_examples(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if lines[i].startswith("# id"):
                example_id = lines[i].strip()
                text_en = lines[i + 2].strip()
                text = lines[i + 3].strip()
                intent_line = lines[i + 1].strip()

                # Find the intent line and move it below text
                while not intent_line.startswith("# intent"):
                    i += 1
                    intent_line = lines[i].strip()

                # Write the example with reorganized structure
                f.write(example_id.replace("id = ", "id: ") + '\n')
                f.write(text_en.replace("text_en = ", "text_en: ") + '\n')
                f.write(text.replace("text = ", "text: ") + '\n')
                f.write(intent_line.replace("intent = ", "intent: ") + '\n')

                # Move to the next example
                i += 4  # Skipping the lines of the current example
                while i < len(lines) and not lines[i].startswith("# id"):
                    f.write(lines[i])
                    i += 1
            else:
                i += 1

# Example usage
input_file = "de-ba.valid.conll"
output_file = "de-ba-mod.valid.conll"
reorganize_examples(input_file, output_file)