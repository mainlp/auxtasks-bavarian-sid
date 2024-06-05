#!/bin/bash
# script to prepare the raw bavarian data from NaLiBaSID to be used in my experiments here
# command from BaySIDshot:  bash scripts/prepare_raw_data.sh

# in Colab (gets removed when quitting runtime of notebook)
mkdir -p /content/BaySIDshot/Raw_data
cp /content/BaySIDshot/NaLiBaSID/data/data.zip /content/BaySIDshot/Raw_data/
unzip -P MaiNLP /content/BaySIDshot/Raw_data/data.zip -d /content/BaySIDshot/Raw_data/
rm -f /content/BaySIDshot/Raw_data/data.zip


# on local machine - do not push this!
#mkdir -p /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/Raw_data
#cp /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/NaLiBaSID/data/data.zip /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/Raw_data/
#unzip -P MaiNLP /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/Raw_data/data.zip -d /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/Raw_data/
#rm -f /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/Raw_data/data.zip
