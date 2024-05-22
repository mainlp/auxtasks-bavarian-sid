#!/usr/bin/python3

# open respective conll file from xSID
with open('a_connl_file.conll', 'r') as f:  
    lines = f.readlines()

# modify it for annotation purposes: 
# - adds a unique id to each example
# - turns english example '# text: ' to '# text-en: ' and adds a '# text: ' for translated example
# - removes '# slots: ' line with specific slot inidices based on characters
# set name for modified conll file

current_id = 1
with open('modified_conll.conll', 'w') as f:
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
