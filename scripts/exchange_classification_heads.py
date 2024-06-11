#!/usr/bin/python3

import torch
from transformers import AutoModelForSequenceClassification

# Load the first model and extract its classification layer
model1_path = '/content/drive/MyDrive/Masterarbeit/test_exchange_heads.0/*/model_*'
model1 = AutoModelForSequenceClassification.from_pretrained('microsoft/mdeberta-v3-base')
model1.load_state_dict(torch.load(model1_path))

# Extract the classification layer from the first model
classification_layer = model1.classifier

# Load the second model
model2_path = '/content/drive/MyDrive/Masterarbeit/test_exchange_heads.1/*/model_*'
model2 = AutoModelForSequenceClassification.from_pretrained('microsoft/mdeberta-v3-base')
model2.load_state_dict(torch.load(model2_path))

# Set the classification layer of the first model as the classification layer in the second model
model2.classifier = classification_layer

# Save the modified second model
modified_model2_path = '/content/drive/MyDrive/Masterarbeit/'
torch.save(model2.state_dict(), modified_model2_path)

print("Successfully replaced the classification layer and saved the modified second model.")
