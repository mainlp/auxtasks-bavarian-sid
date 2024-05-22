#!/usr/bin/python3

import re

# regex tokenizer for input sentence - this is how I also splitted the annotation
def tokenize_text(text):
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return tokens

# set conll file to be postprocessed here:
with open('de-ba.pred.conll', 'r') as f:
    lines = f.readlines()

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
            print(f"Error: Incorrectly annotated line - more or less than 4 colums in example {current_example['id']}: \n{line}")
                
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
        
        # Check for missmatches and where they are
        mismatches = []
        min_length = min(len(translation_tokens), len(annotation_tokens))
    
        for index in range(min_length):
            if translation_tokens[index] != annotation_tokens[index]:
                mismatches.append({'index': index, 'expected': translation_tokens[index], 'actual': annotation_tokens[index]})

        if len(translation_tokens) > len(annotation_tokens):
            for index in range(min_length, len(translation_tokens)):
                mismatches.append({'index': index, 'expected': translation_tokens[index], 'actual': None})
                
        elif len(annotation_tokens) > len(translation_tokens):
            for index in range(min_length, len(annotation_tokens)):
                mismatches.append({'index': index, 'expected': None, 'actual': annotation_tokens[index]})
                
                
        if mismatches:
            for mismatch in mismatches:
                print(f"Error: Tokens mismatch for example {example['id']} at index {mismatch['index']+1}: Expected '{mismatch['expected']}' but got '{mismatch['actual']}'")

        
        # Check for correct anntation ids
        annotation_ids = list(map(int, [token[0] for token in example['tokens']]))
        
        for i in range(1, len(annotation_ids)):
            if annotation_ids[i] != annotation_ids[i - 1] + 1 or annotation_ids[i] < annotation_ids[i - 1] or annotation_ids[i] <= annotation_ids[i - 1]:
                print(f"Error: Incorrect annotation IDs in example {example['id']}")



