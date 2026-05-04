from journal import (
    add_entries,
    load_entries,
    save_entries,
    search_entries,
    view_entries,
)


def main():

    journals = load_entries()
    while True:
        print("1. Add new journal")
        print("2. View entries")
        print("3. Search")
        print("4. Exit")
        user_input = input("What do you want to do? \n > ").lower()
        if user_input in ("one", "1", "add entries"):
            entries = add_entries()
            journals.append(entries)
            save_entries(journals)
        elif user_input in ("two", "2", "view entries"):
            view_entries(journals)
        elif user_input in ("three", "3", "search"):
            search_input = input("Search.. \n > ")
            search_entries(journals, search_input)
        elif user_input in ("four", "4", "exit"):
            break
        else:
            print("Please choose valid option.")


if __name__ == "__main__":
    main()
