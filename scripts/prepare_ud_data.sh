#!/bin/bash
# script to prepare the UD_Bavarian-MaiBaam data to be used with MaChAmp and as train and dev 90-10 split
# command from BaySIDshot:  bash scripts/prepare_ud_data.sh

# in Colab
mkdir -p content/BaySIDshot/UD_data
cp /content/BaySIDshot/UD_Bavarian-MaiBaam/bar_maibaam-ud-test.conllu /content/BaySIDshot/UD_data
python3 /content/BaySIDshot/machamp/scripts/misc/cleanconl.py /content/BaySIDshot/UD_data/bar_maibaam-ud-test.conllu
python3 /content/BaySIDshot/scripts/testsplit_conllu.py /content/BaySIDshot/UD_data/bar_maibaam-ud-test.conllu

# on loacal machine
#mkdir -p /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/UD_data
#cp /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/UD_Bavarian-MaiBaam/bar_maibaam-ud-test.conllu /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/UD_data
#python3 /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/machamp/scripts/misc/cleanconl.py /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/UD_data/bar_maibaam-ud-test.conllu
#python3 /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/scripts/testsplit_conllu.py /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/UD_data/bar_maibaam-ud-test.conllu
