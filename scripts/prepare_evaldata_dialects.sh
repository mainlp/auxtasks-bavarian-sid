#!/bin/bash
# script to prepare dialects evaluation data
mkdir -p /content/BaySIDshot/dialects_eval_data/

# copy dialects eval data together, paths according to usage in Colab:

cp /content/BaySIDshot/de-by.test.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/de-by.dev.conll /content/BaySIDshot/dialects_eval_data/

cp /content/BaySIDshot/xsid/data/xSID-0.5/de-ba.test.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.5/de-ba.valid.conll /content/BaySIDshot/dialects_eval_data/
python3 /content/BaySIDshot/scripts/reorganize_miriams_data.py /content/BaySIDshot/dialects_eval_data/de-ba.test.conll
python3 /content/BaySIDshot/scripts/reorganize_miriams_data.py /content/BaySIDshot/dialects_eval_data/de-ba.valid.conll

cp /content/BaySIDshot/xsid/data/xSID-0.4/de.test.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.4/de.valid.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.4/de-st.test.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.4/de-st.valid.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.4/en.test.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.4/en.valid.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.4/gsw.test.conll /content/BaySIDshot/dialects_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.4/gsw.valid.conll /content/BaySIDshot/dialects_eval_data/
