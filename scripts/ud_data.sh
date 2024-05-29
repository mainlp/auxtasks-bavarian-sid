#!/bin/bash
mkdir UD_data
cp /content/BaySIDshot/UD_Bavarian-MaiBaam/bar_maibaam-ud-test.conllu UD_data
cd UD_data
python3 /content/BaySIDshot/machamp/scripts/misc/cleanconl.py /content/BaySIDshot/UD_Bavarian-MaiBaam/bar_maibaam-ud-test.conllu
python3 /content/BaySIDshot/scripts/testsplit_conllu.py bar_maibaam-ud-test.conllu
cd ..