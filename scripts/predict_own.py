#!/usr/bin/python3

import sys
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
from safetensors.torch import load_file

def predict_own(model_dir):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    # Load the model configuration
    config = AutoConfig.from_pretrained(model_dir)

    # Initialize the model
    model = AutoModelForSequenceClassification.from_config(config)

    # Load the state dictionary from the safetensors file
    state_dict = load_file(f"{model_dir}/model.safetensors")

    # Load the state dictionary into the model
    model.load_state_dict(state_dict)

    # Set the model to evaluation mode
    model.eval()

    # Example input text
    input_text = "stei an wecka"

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the logits (predictions before softmax)
    logits = outputs.logits

    # Apply softmax to get probabilities
    probabilities = torch.nn.functional.softmax(logits, dim=-1)

    # Get the predicted class
    predicted_class = torch.argmax(probabilities, dim=-1)

    # Check if the configuration includes label information
    if hasattr(config, 'id2label'):
        id2label = config.id2label
    else:
        # Manually define the label mapping (example)
        id2label = {0: "negative", 1: "positive"}

    # Interpret the predicted class
    predicted_label = id2label[predicted_class.item()]

    print(f"Predicted class: {predicted_class.item()}")
    print(f"Probabilities: {probabilities}")
    print(f"Predicted label: {predicted_label}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 predict_own.py <model_dir>")
        sys.exit(1)

    model_dir = sys.argv[1]
    predict_own(model_dir)
