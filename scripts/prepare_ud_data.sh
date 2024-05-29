#!/bin/bash
# script to prepare the UD_Bavarian-MaiBaam data to be used with MaChAmp and as train and dev 90-10 split
mkdir -p UD_data
cd UD_data
cp /content/BaySIDshot/UD_Bavarian-MaiBaam/bar_maibaam-ud-test.conllu .
python3 /content/BaySIDshot/machamp/scripts/misc/cleanconl.py /content/BaySIDshot/UD_Bavarian-MaiBaam/bar_maibaam-ud-test.conllu
python3 /content/BaySIDshot/scripts/testsplit_conllu.py bar_maibaam-ud-test.conllu
cd ..