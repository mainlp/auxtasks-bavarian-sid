#!/bin/bash

# script to prepare the mlm bavarian data from dialect-BLI to be used in my experiments here
# command from BaySIDshot:  bash scripts/prepare_mlm_data.sh

# in Colab (gets removed when quitting runtime of notebook)
mkdir -p /content/BaySIDshot/MLM_data
python3 /content/BaySIDshot/scripts/prepare_mlm_data.py /content/BaySIDshot/dialect-BLI/labelled_data/bitext/bar/ann_1.csv /content/BaySIDshot/MLM_data/

# on local machine:
#mkdir -p /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/MLM_data/
#python3 /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/scripts/prepare_mlm_data.py /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/dialect-BLI/labelled_data/bitext/bar/ann_1.csv /Users/xavermariakrueckl/PycharmProjects/BaySIDshot/manual_data/MLM_data/