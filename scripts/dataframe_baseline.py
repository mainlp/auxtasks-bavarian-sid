import pandas as pd

# baseline data from xSID paper

data_mBERT = {
    'Language': ['en', 'de-st', 'de', 'da', 'nl', 'it', 'sr', 'id', 'ar', 'zh', 'kk', 'tr', 'ja'],
    'slots': [97.6, 48.5, 33.0, 73.9, 80.4, 75.0, 67.4, 71.1, 45.8, 72.9, 48.5, 55.7, 59.9],
    'intents': [99.7, 67.8, 74.2, 87.5, 72.3, 81.7, 75.7, 80.7, 63.1, 83.3, 60.1, 74.7, 53.9]
}

data_XLM15 = {
    'Language': ['en', 'de-st', 'de', 'da', 'nl', 'it', 'sr', 'id', 'ar', 'zh', 'kk', 'tr', 'ja'],
    'slots': [97.0, 39.4, 33.3, 26.3, 30.9, 27.3, 15.9, 14.9, 49.1, 57.6, 10.9, 45.5, 33.4],
    'intents': [99.7, 61.3, 78.5, 56.3, 45.4, 48.0, 41.4, 36.4, 67.5, 78.8, 29.9, 67.3, 39.1]
}

# my data
# mBERT base

data_mBERT_1234 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [52.6, 70.6, 67.2, 40.1, 94.4, 63.1, 70.8, 43.8, 32.6, 68.8, 56.4, 32.4, 47.5],
    'intents': [68.8, 84.8, 73.8, 65.6, 99.0, 76.2, 75.6, 54.8, 61.0, 70.4, 67.4, 70.8, 81.2]
}

data_mBERT_6543 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [51.9, 69.1, 67.8, 41.1, 93.7, 62.9, 68.3, 39.4, 33.1, 69.5, 54.0, 33.5, 49.8],
    'intents': [67.0, 85.8, 73.4, 63.4, 99.2, 75.4, 77.0, 56.8, 55.8, 71.0, 81.4, 72.4, 83.4]
}

data_mBERT_8446 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [52.8, 71.1, 70.1, 42.6, 94.1, 65.3, 70.5, 35.0, 30.8, 71.9, 54.5, 32.8, 46.6],
    'intents': [68.0, 83.8, 77.2, 68.4, 98.8, 76.4, 76.4, 54.8, 53.8, 68.4, 78.4, 70.8, 89.8]
}

average_mBERT = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [52.4, 70.3, 68.4, 41.3, 94.1, 63.8, 69.9, 39.4, 32.2, 70.1, 55.0, 32.9, 48.0],
    'intents': [67.9, 84.8, 74.8, 65.8, 99.0, 76.0, 76.3, 55.5, 56.9, 69.9, 75.7, 71.3, 84.8]
}


# XLMR base

data_XLMR_1234 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [60.1, 81.5, 75.4, 32.8, 93.2, 75.7, 72.9, 50.2, 42.5, 82.4, 64.8, 50.2, 69.6],
    'intents': [77.6, 96.0, 90.8, 72.0, 98.8, 95.0, 77.4, 55.2, 71.4, 83.0, 83.0, 92.6, 95.2]
}

data_XLMR_6543 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [61.3, 81.7, 72.3, 31.1, 94.0, 79.1, 77.5, 52.1, 45.2, 82.7, 61.7, 54.4, 65.4],
    'intents': [80.8, 95.6, 89.4, 69.2, 99.0, 96.4, 83.4, 56.4, 79.2, 87.6, 83.6, 93.0, 96.8]
}

data_XLMR_8446 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [65.4, 79.4, 73.5, 32.5, 94.3, 75.1, 76.5, 50.7, 47.8, 81.5, 65.1, 54.0, 65.5],
    'intents': [75.8, 94.2, 86.6, 71.4, 99.2, 94.4, 80.8, 52.0, 76.8, 82.2, 81.4, 96.6, 96.0]
}

average_XLMR = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [62.3, 80.9, 73.7, 32.1, 93.8, 76.6, 75.6, 51.0, 45.2, 82.2, 63.9, 52.9, 66.8],
    'intents': [78.1, 95.3, 88.9, 70.9, 99.0, 95.3, 80.5, 54.5, 75.8, 84.3, 82.7, 94.1, 96.0]
}


# mDeBERTa base

data_mDeBERTa_1234 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [72.0, 80.9, 84.0, 45.3, 95.4, 79.4, 83.5, 47.2, 52.2, 87.6, 70.7, 58.1, 77.0],
    'intents': [85.4, 97.2, 97.8, 78.6, 99.2, 98.0, 97.0, 76.8, 90.0, 97.6, 91.0, 97.4, 97.8]
}

data_mDeBERTa_6543 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [70.4, 78.5, 83.0, 47.4, 95.0, 74.9, 82.4, 45.0, 52.9, 86.8, 72.1, 59.6, 72.8],
    'intents': [90.6, 94.4, 98.4, 79.0, 99.2, 97.6, 97.4, 82.0, 87.2, 95.8, 89.0, 97.2, 95.4]
}

data_mDeBERTa_8446 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [71.0, 79.7, 82.3, 45.3, 95.0, 80.5, 83.4, 57.1, 52.1, 85.4, 73.4, 57.2, 74.2],
    'intents': [84.6, 97.8, 97.4, 77.2, 99.0, 93.2, 97.8, 78.8, 92.6, 96.2, 87.4, 97.0, 97.4]
}

average_mDeBERTa = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [71.1, 79.7, 83.1, 46.0, 95.1, 78.3, 83.1, 49.8, 52.4, 86.6, 72.1, 58.3, 74.7],
    'intents': [86.9, 96.5, 97.9, 78.3, 99.1, 96.3, 97.4, 79.2, 89.9, 96.5, 89.1, 97.2, 96.9]
}

# gBERT base

data_gBERT_1234 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [19.7, 38.0, 79.3, 49.0, 93.2, 17.5, 27.3, 1.1, 3.9, 45.5, 17.0, 9.5, 16.5],
    'intents': [17.2, 63.2, 84.2, 73.2, 99.2, 47.8, 53.2, 1.2, 30.8, 58.6, 45.2, 46.0, 19.0]
}

data_gBERT_6543 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [20.4, 38.1, 77.7, 42.9, 94.1, 16.6, 29.0, 0.0, 6.7, 45.2, 17.7, 7.5, 14.0],
    'intents': [24.8, 59.6, 81.2, 73.0, 99.2, 47.8, 51.6, 1.2, 36.8, 59.0, 41.0, 45.2, 21.6]
}

data_gBERT_8446 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [19.1, 35.8, 79.4, 47.5, 93.8, 17.4, 27.6, 1.1, 5.6, 42.4, 20.8, 7.8, 12.9],
    'intents': [39.6, 63.0, 83.4, 75.2, 99.2, 45.2, 52.0, 14.4, 37.0, 59.6, 51.0, 48.6, 30.8]
}


average_gBERT = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [19.7, 37.3, 78.8, 46.5, 93.7, 17.2, 28.0, 0.7, 5.4, 44.4, 18.5, 8.3, 14.5],
    'intents': [27.2, 61.9, 82.9, 73.8, 99.2, 46.9, 52.3, 5.6, 34.9, 59.1, 45.7, 46.6, 23.8]
}

# first experiment - mDeBERTa first trained on UD EWT bavarian train english dev then NLU as before:

data_exp21_8446 = {
    'Language': ['ar', 'da', 'de', 'de-st', 'en', 'id', 'it', 'ja', 'kk', 'nl', 'sr', 'tr', 'zh'],
    'slots': [72.6, 78.8, 81.2, 52.0, 95.7, 79.6, 81.4, 55.7, 54.4, 87.0, 73.3, 59.9, 73.9],
    'intents': [86.0, 97.2, 88.4, 77.0, 99.4, 96.6, 94.6, 88.0, 86.0, 98.2, 94.2, 97.4, 97.0]
}


# Create multi-index DataFrame for mBERT
df_mBERT = pd.DataFrame(data_mBERT)
df_mBERT.set_index('Language', inplace=True)
df_mBERT.columns = pd.MultiIndex.from_product([['mBERT-xSID'], df_mBERT.columns])

# Create multi-index DataFrame for XLM15
df_XLM15 = pd.DataFrame(data_XLM15)
df_XLM15.set_index('Language', inplace=True)
df_XLM15.columns = pd.MultiIndex.from_product([['XLM15-xSID'], df_XLM15.columns])

# Create multi-index DataFrame for mBERT_me
df_mBERT_me = pd.DataFrame(average_mBERT)
df_mBERT_me.set_index('Language', inplace=True)
df_mBERT_me.columns = pd.MultiIndex.from_product([['mBERT-ME'], df_mBERT_me.columns])

# Create multi-index DataFrame for XLMR_me
df_XLMR_me = pd.DataFrame(average_XLMR)
df_XLMR_me.set_index('Language', inplace=True)
df_XLMR_me.columns = pd.MultiIndex.from_product([['XLMR-ME'], df_XLMR_me.columns])

# Create multi-index DataFrame for mDeBERTa
df_mDeBERTa = pd.DataFrame(average_mDeBERTa)
df_mDeBERTa.set_index('Language', inplace=True)
df_mDeBERTa.columns = pd.MultiIndex.from_product([['mDeBERTa'], df_mDeBERTa.columns])

# Create multi-index DataFrame for gBERT
df_gBERT = pd.DataFrame(average_gBERT)
df_gBERT.set_index('Language', inplace=True)
df_gBERT.columns = pd.MultiIndex.from_product([['gBERT'], df_gBERT.columns])

# Create multi-index DataFrame for mDeBERTa_exp
df_mDeBERTa_epx = pd.DataFrame(data_exp21_8446)
df_mDeBERTa_epx.set_index('Language', inplace=True)
df_mDeBERTa_epx.columns = pd.MultiIndex.from_product([['mDeBERTa-EXP'], df_mDeBERTa_epx.columns])

# Merge the DataFrames ensuring the correct language order - experiment not included for now!
df_concatenated = pd.concat([df_mBERT, df_mBERT_me, df_XLM15, df_XLMR_me, df_mDeBERTa, df_gBERT], axis=1)




# Calculate the average values excluding "en" for each metric and each model
slots_avg_mBERT = df_concatenated.loc[df_concatenated.index != 'en', ('mBERT-xSID', 'slots')].mean()
intents_avg_mBERT = df_concatenated.loc[df_concatenated.index != 'en', ('mBERT-xSID', 'intents')].mean()

slots_avg_mBERT_me = df_concatenated.loc[df_concatenated.index != 'en', ('mBERT-ME', 'slots')].mean()
intents_avg_mBERT_me = df_concatenated.loc[df_concatenated.index != 'en', ('mBERT-ME', 'intents')].mean()

slots_avg_XLM15 = df_concatenated.loc[df_concatenated.index != 'en', ('XLM15-xSID', 'slots')].mean()
intents_avg_XLM15 = df_concatenated.loc[df_concatenated.index != 'en', ('XLM15-xSID', 'intents')].mean()

slots_avg_XLMR_me = df_concatenated.loc[df_concatenated.index != 'en', ('XLMR-ME', 'slots')].mean()
intents_avg_XLMR_me = df_concatenated.loc[df_concatenated.index != 'en', ('XLMR-ME', 'intents')].mean()

slots_avg_mDeBERTa = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa', 'slots')].mean()
intents_avg_mDeBERTa  = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa', 'intents')].mean()

slots_avg_gBERT = df_concatenated.loc[df_concatenated.index != 'en', ('gBERT', 'slots')].mean()
intents_avg_gBERT = df_concatenated.loc[df_concatenated.index != 'en', ('gBERT', 'intents')].mean()

#slots_avg_mDeBERTa_exp = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa-EXP', 'slots')].mean()
#intents_avg_mDeBERTa_exp = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa-EXP', 'intents')].mean()

# Format the average values to have only one digit after the decimal point
slots_avg_mBERT_formatted = '{:.1f}'.format(slots_avg_mBERT)
intents_avg_mBERT_formatted = '{:.1f}'.format(intents_avg_mBERT)

slots_avg_mBERT_me_formatted = '{:.1f}'.format(slots_avg_mBERT_me)
intents_avg_mBERT_me_formatted = '{:.1f}'.format(intents_avg_mBERT_me)

slots_avg_XLM15_formatted = '{:.1f}'.format(slots_avg_XLM15)
intents_avg_XLM15_formatted = '{:.1f}'.format(intents_avg_XLM15)

slots_avg_XLMR_me_formatted = '{:.1f}'.format(slots_avg_XLMR_me)
intents_avg_XLMR_me_formatted = '{:.1f}'.format(intents_avg_XLMR_me)

slots_avg_mDeBERTa_formatted = '{:.1f}'.format(slots_avg_mDeBERTa)
intents_avg_mDeBERTa_formatted = '{:.1f}'.format(intents_avg_mDeBERTa)

slots_avg_gBERT_formatted = '{:.1f}'.format(slots_avg_gBERT)
intents_avg_gBERT_exp_formatted = '{:.1f}'.format(intents_avg_gBERT)

#slots_avg_mDeBERTa_exp_formatted = '{:.1f}'.format(slots_avg_mDeBERTa_exp)
#intents_avg_mDeBERTa_exp_formatted = '{:.1f}'.format(intents_avg_mDeBERTa_exp)

# Create DataFrames containing the average values
avg_data = {
    ('mBERT-xSID', 'slots'): [slots_avg_mBERT_formatted],
    ('mBERT-xSID', 'intents'): [intents_avg_mBERT_formatted],
    ('mBERT-ME', 'slots'): [slots_avg_mBERT_me_formatted],
    ('mBERT-ME', 'intents'): [intents_avg_mBERT_me_formatted],
    ('XLM15-xSID', 'slots'): [slots_avg_XLM15_formatted],
    ('XLM15-xSID', 'intents'): [intents_avg_XLM15_formatted],
    ('XLMR-ME', 'slots'): [slots_avg_XLMR_me_formatted],
    ('XLMR-ME', 'intents'): [intents_avg_XLMR_me_formatted],
    ('mDeBERTa', 'slots'): [slots_avg_mDeBERTa_formatted],
    ('mDeBERTa', 'intents'): [intents_avg_mDeBERTa_formatted],
    ('gBERT', 'slots'): [slots_avg_gBERT_formatted],
    ('gBERT', 'intents'): [intents_avg_gBERT_exp_formatted]
}
#('mDeBERTa-EXP', 'slots'): [slots_avg_mDeBERTa_exp_formatted],
#('mDeBERTa-EXP', 'intents'): [intents_avg_mDeBERTa_exp_formatted]

df_avg = pd.DataFrame(avg_data, index=['Avg.'])

# Concatenate the average DataFrame with df_concatenated
df_concatenated_with_avg = pd.concat([df_concatenated, df_avg])

print(df_concatenated_with_avg)
