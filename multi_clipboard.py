from sys import argv
import clipboard
import json
from os import path

# The program handles command-line inputs to implement three main methods.
# Read the current text in the clipboard to utilize and save it in a json file.

JSON_FILE_NAME = "multi_clipboard.json"

def main():

    if not path.exists(JSON_FILE_NAME):
        with open(JSON_FILE_NAME, "w") as file:
            json.dump({}, file)

    if len(argv) == 2:
        if argv[1] == "save":
            save()
        elif argv[1] == "load":
            load()
        elif argv[1] == "list":
            list_clipboard()
        else:
            print("You must enter a valid method from(save/load/list)")
    else:
        print("The command must be: python mult_clipboard method(save/load/list)")


def load_clipboard_data():
    try:
        with open(JSON_FILE_NAME, "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return {}

def save():
    copied_data = clipboard.paste()
    if copied_data.strip():
        key = input("enter a key to refer what you have copied: ").strip().lower()
        clipboard_data = load_clipboard_data()
        clipboard_data[key] = copied_data
        with open(JSON_FILE_NAME, "w") as file:
            json.dump(clipboard_data, file)
    else:
        print("empty clipboard")

def load():
    key = input("enter the key that refer to your copied data: ").strip().lower()
    clipboard_data = load_clipboard_data()
    result = clipboard_data.get(key, "")
    if result:
        print(result)
        clipboard.copy(result)
    else:
        print("Not found")

def list_clipboard():
    clipboard_data = load_clipboard_data()
    if clipboard_data:
        for key, pasted_data in clipboard_data.items():
            print(f"{key}: {pasted_data}")
    else:
        print("No data stored yet!")

main()