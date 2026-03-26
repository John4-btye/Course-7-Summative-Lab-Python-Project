import json
import os

FILE_PATH = "data/storage.json"


def initialize_storage():
    """Ensure storage file exists with valid structure."""
    if not os.path.exists(FILE_PATH):
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        with open(FILE_PATH, "w") as f:
            json.dump({"users": []}, f, indent=4)


def load_data():
    """Load data safely from JSON file."""
    initialize_storage()

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Handle corrupted file
        print("Warning: storage.json is corrupted. Resetting file.")
        return {"users": []}
    except Exception as e:
        print(f"Error loading data: {e}")
        return {"users": []}


def save_data(data):
    """Save data safely to JSON file."""
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")