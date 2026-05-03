import json
from datetime import date, datetime


def load_entries():
    with open("journal.json", "r") as file:
        content = json.load(file)
    return content


def save_entries(entries):
    with open("journal.json", "w") as file:
        json.dump(entries, file)


def add_entries():
    entry_title = input("whats the title? \n > ")
    entry_content = input("whats today's toughts? \n > ")
    formatted_time = date.today().strftime("%d-%m-%Y")
    entries = {"date": formatted_time, "title": entry_title, "journal": entry_content}
    return entries


def view_entries(entries):
    for entry in entries:
        print(
            f"Date: {entry['date']} \n Title: {entry['title']} \n Journal: {entry['journal']}"
        )
