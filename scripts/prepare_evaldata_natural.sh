#!/bin/bash

# script to prepare the natural bavarian evaluation data from NaLiBaSID
# needs to be and gets removed when quitting runtime of notebook!
# command from BaySIDshot:  bash scripts/prepare_evaldata_natural.sh

# in Colab
mkdir -p /content/BaySIDshot/natural_eval_data
cp /content/BaySIDshot/NaLiBaSID/data/data.zip /content/BaySIDshot/natural_eval_data/
unzip -P MaiNLP -o /content/BaySIDshot/natural_eval_data/data.zip -d /content/BaySIDshot/natural_eval_data/
mv -f /content/BaySIDshot/natural_eval_data/de-ba.MAS.test.conll /content/BaySIDshot/natural_eval_data/de-ba-MAS.test.conll
python3 /content/BaySIDshot/scripts/reorganize_natural_data.py /content/BaySIDshot/natural_eval_data/de-ba-MAS.test.conll
mv -f /content/BaySIDshot/natural_eval_data/de-ba.xMAS.test.conll /content/BaySIDshot/natural_eval_data/de-ba-xMAS.test.conll
python3 /content/BaySIDshot/scripts/reorganize_natural_data.py /content/BaySIDshot/natural_eval_data/de-ba-xMAS.test.conll
mv -f /content/BaySIDshot/natural_eval_data/de-ba.nat.conll /content/BaySIDshot/natural_eval_data/de-ba-nat.test.conll
python3 /content/BaySIDshot/scripts/reorganize_natural_data.py /content/BaySIDshot/natural_eval_data/de-ba-nat.test.conll
rm -f /content/BaySIDshot/natural_eval_data/de-ba.MAS.valid.conll
rm -f /content/BaySIDshot/natural_eval_data/de-ba.xMAS.valid.conll
rm -f /content/BaySIDshot/natural_eval_data/de-ba.valid.conll
rm -f /content/BaySIDshot/natural_eval_data/de-ba.test.conll
rm -f /content/BaySIDshot/natural_eval_data/lt.nat.conll
rm -f /content/BaySIDshot/natural_eval_data/lt.test.conll
rm -f /content/BaySIDshot/natural_eval_data/lt.valid.conll
rm -f /content/BaySIDshot/natural_eval_data/data.zip


# on local machine - do not push this - data should stay "private"!
#mkdir -p /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data
#cp /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/NaLiBaSID/data/data.zip /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/
#unzip -P MaiNLP -o /content/BaySIDshot/natural_eval_data/data.zip -d /content/BaySIDshot/natural_eval_data/
#mv -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba.MAS.test.conll /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba-MAS.test.conll
#python3 /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/scripts/reorganize_natural_data.py /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba-MAS.test.conll
#mv -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba.xMAS.test.conll /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba-xMAS.test.conll
#python3 /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/scripts/reorganize_natural_data.py /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba-xMAS.test.conll
#mv -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba.nat.conll /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba-nat.test.conll
#python3 /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/scripts/reorganize_natural_data.py /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba-nat.test.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba.MAS.valid.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba.xMAS.valid.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba.valid.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/de-ba.test.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/lt.nat.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/lt.test.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/lt.valid.conll
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/data.zip
