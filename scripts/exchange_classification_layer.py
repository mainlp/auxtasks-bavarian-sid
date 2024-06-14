#!/usr/bin/python3

import sys
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 exchange_classification_layer.py <model0_dir> <model1_dir> <model_out_dir>")
        sys.exit(1)

    model0_dir = sys.argv[1]
    model1_dir = sys.argv[2]
    model_out_dir = sys.argv[3]

    # Load the first model and extract its classification layer
    model0 = AutoModelForSequenceClassification.from_pretrained(model0_dir)

    # Extract the classification layer from the first model
    classification_layer = model0.classifier

    # Load the second model
    model1 = AutoModelForSequenceClassification.from_pretrained(model1_dir)

    # Set the classification layer of the first model as the classification layer in the second model
    model1.classifier = classification_layer

    # Save the modified second model
    model1.save_pretrained(model_out_dir)

    # Also save the tokenizer if needed
    tokenizer = AutoTokenizer.from_pretrained(model0_dir)
    tokenizer.save_pretrained(model_out_dir)

    print("Successfully replaced the classification layer and saved the modified second model.")
