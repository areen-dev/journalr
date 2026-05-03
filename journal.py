import json


def load_entries():
    with open("journal.json", "r") as file:
        content = json.load(file)
    return content


def save_entries(entries):
    with open("journal.json", "w") as file:
        json.dump(entries, file)
