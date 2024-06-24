#!/bin/bash
# script to prepare the natural bavarian evaluation data from NaLiBaSID
# needs to be and gets removed when quitting runtime of notebook!
# command from BaySIDshot:  bash scripts/prepare_evaldata_natural.sh

# in Colab
mkdir -p /content/BaySIDshot/natural_eval_data
cp /content/BaySIDshot/NaLiBaSID/data/data.zip /content/BaySIDshot/natural_eval_data/
unzip -P MaiNLP /content/BaySIDshot/Raw_data/data.zip -d /content/BaySIDshot/natural_eval_data/
rm -f /content/BaySIDshot/natural_eval_data/data.zip


# on local machine - do not push this - data should stay "private"!
#mkdir -p /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data
#cp /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/NaLiBaSID/data/data.zip /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/
#unzip -P MaiNLP /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/Raw_data/data.zip -d /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/natural_eval_data/data.zip
