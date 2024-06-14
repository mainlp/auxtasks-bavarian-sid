#!/usr/bin/python3

import sys
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
from safetensors.torch import load_file

# Define intents and slots
intents = [
    "weather / find", "alarm / set_alarm", "alarm / show_alarms",
    "reminder / set_reminder", "alarm / modify_alarm", "weather / checkSunrise",
    "weather / checkSunset", "alarm / snooze_alarm", "alarm / cancel_alarm",
    "reminder / show_reminders", "reminder / cancel_reminder", "alarm / time_left_on_alarm",
    "AddToPlaylist", "BookRestaurant", "PlayMusic", "RateBook", "SearchCreativeWork",
    "SearchScreeningEvent"
]

slots = [
    "O", "B-location", "I-location", "B-datetime", "I-datetime", "B-weather/attribute",
    "B-reference", "I-weather/attribute", "B-reminder/todo", "I-reminder/todo",
    "B-alarm/alarm_modifier", "B-recurring_datetime", "I-recurring_datetime", "I-reference",
    "B-reminder/reminder_modifier", "Orecurring_datetime", "B-negation", "B-timer/attributes",
    "B-news/type", "I-reminder/reminder_modifier", "B-weather/temperatureUnit",
    "I-alarm/alarm_modifier", "B-entity_name", "I-entity_name", "B-playlist", "I-playlist",
    "B-music_item", "B-artist", "I-artist", "B-party_size_number", "B-sort", "B-restaurant_type",
    "B-restaurant_name", "I-restaurant_name", "B-served_dish", "B-facility",
    "B-party_size_description", "I-party_size_description", "B-cuisine", "I-cuisine", "I-sort",
    "I-restaurant_type", "I-served_dish", "I-facility", "B-condition_temperature",
    "B-condition_description", "B-service", "I-service", "B-album", "I-album", "B-genre",
    "I-genre", "B-track", "I-track", "I-music_item", "B-rating_value", "B-best_rating",
    "B-rating_unit", "B-object_name", "I-object_name", "B-object_part_of_series_type",
    "B-object_select", "B-object_type", "I-object_select", "I-object_type",
    "I-object_part_of_series_type", "B-movie_name", "I-movie_name", "B-object_location_type",
    "I-object_location_type", "B-movie_type", "I-movie_type"
]

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
    input_text = "wecka"

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Assume outputs contains both intent and slot logits
    intent_logits = outputs.logits[:, :len(intents)]
    slot_logits = outputs.logits[:, len(intents):]

    # Apply softmax to get probabilities
    intent_probabilities = torch.nn.functional.softmax(intent_logits, dim=-1)
    slot_probabilities = torch.nn.functional.softmax(slot_logits, dim=-1)

    # Get the predicted class
    predicted_intent_class = torch.argmax(intent_probabilities, dim=-1)
    predicted_slot_class = torch.argmax(slot_probabilities, dim=-1)

    # Print predicted classes and probabilities
    predicted_intent = intents[predicted_intent_class.item()]
    predicted_slot = slots[predicted_slot_class.item()]

    print(f"For {input_text}, the model predicts:")
    print(f"Predicted intent: {predicted_intent}")
    print(f"Intent probabilities: {intent_probabilities}")
    print(f"Predicted slot: {predicted_slot}")
    print(f"Slot probabilities: {slot_probabilities}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 predict_own.py <model_dir>")
        sys.exit(1)

    model_dir = sys.argv[1]
    predict_own(model_dir)
