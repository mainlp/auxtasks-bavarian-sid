#!/bin/bash
mkdir -p dialects_eval_data
cd dialects_eval_data

# copy dialects eval data together:
# adapt absolute paths for out of colab cases!

cp /content/BaySIDshot/de-by.test.conll .
cp /content/BaySIDshot/de-by.dev.conll .

cp /content/BaySIDshot/xsid/data/xSID-0.5/de-ba.test.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.5/de-ba.valid.conll .

python3 /content/BaySIDshot/scripts/reorganize_miriams_data.py de-ba.test.conll
python3 /content/BaySIDshot/scripts/reorganize_miriams_data.py de-ba.valid.conll

cp /content/BaySIDshot/xsid/data/xSID-0.4/de.test.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.4/de.valid.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.4/de-st.test.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.4/de-st.valid.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.4/en.test.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.4/en.valid.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.4/gsw.test.conll .
cp /content/BaySIDshot/xsid/data/xSID-0.4/gsw.valid.conll .

cd ..