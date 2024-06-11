#!/usr/bin/python3

import sys
import torch

def load_model(filepath):
    return torch.load(filepath, map_location=torch.device('cuda'))

def replace_classification_head(model0_path, model1_path, model_out_path):
    # Load the first model and extract its classification layer
    model0 = load_model(model0_path)
    classification_layer = model0.classifier

    # Load the second model
    model1 = load_model(model1_path)

    # Set the classification layer of the first model as the classification layer in the second model
    model1.classifier = classification_layer

    # Save the modified second model
    torch.save(model1, model_out_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 exchange_classification_heads.py <model0_path> <model1_path> <model_out_path>")
        sys.exit(1)

    replace_classification_head(sys.argv[1], sys.argv[2], sys.argv[3])
    print("Successfully replaced the classification layer and saved the modified second model.")
