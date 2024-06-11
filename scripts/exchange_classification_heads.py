#!/usr/bin/python3

import sys
import torch
from transformers import AutoModelForSequenceClassification

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 exchange_classification_heads.py <model0_path> <model1_path>, <model_out_path>")
        sys.exit(1)

    # Load the first model and extract its classification layer
    #model0_path = '/content/drive/MyDrive/Masterarbeit/test_exchange_heads.0/*/model_*'
    model0_path = sys.argv[1]
    model0 = AutoModelForSequenceClassification.from_pretrained('microsoft/mdeberta-v3-base')
    model0.load_state_dict(torch.load(model0_path))

    # Extract the classification layer from the first model
    classification_layer = model0.classifier

    # Load the second model
    #model1_path = '/content/drive/MyDrive/Masterarbeit/test_exchange_heads.1/*/model_*'
    model1_path = sys.argv[2]
    model1 = AutoModelForSequenceClassification.from_pretrained('microsoft/mdeberta-v3-base')
    model1.load_state_dict(torch.load(model1_path))

    # Set the classification layer of the first model as the classification layer in the second model
    model1.classifier = classification_layer

    # Save the modified second model
    #model_out_path = '/content/drive/MyDrive/Masterarbeit/'
    model_out_path = sys.argv[3]
    torch.save(model1.state_dict(), model_out_path)

    print("Successfully replaced the classification layer and saved the modified second model.")
