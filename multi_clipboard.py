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
        clipboard_data = load_json_data()
        if argv[1] == "save":
            save(clipboard_data)
        elif argv[1] == "load":
            load(clipboard_data)
        elif argv[1] == "list":
            list_clipboard(clipboard_data)
        elif argv[1] == "delete":
            delete(clipboard_data)
        else:
            print("You must enter a valid command")
    else:
        print("The command must be: python mult_clipboard method(save/load/list/delete)")


def load_json_data():
    try:
        with open(JSON_FILE_NAME, "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return {}

def dump_json_data(data):
    with open(JSON_FILE_NAME, "w") as file:
        return json.dump(data ,file)


def save(clipboard_data):
    copied_data = clipboard.paste()
    if copied_data.strip():
        key = input("enter a key to refer what you have copied: ").strip().lower()
        clipboard_data[key] = copied_data
        dump_json_data(clipboard_data)
    else:
        print("empty clipboard")

def load(clipboard_data):
    key = input("enter the key that refer to your copied data: ").strip().lower()
    result = clipboard_data.get(key, "")
    if result:
        clipboard.copy(result)
    else:
        print("Not found")

def list_clipboard(clipboard_data): 
    if clipboard_data:
        for key, pasted_data in clipboard_data.items():
            print(f"{key}: {pasted_data}")
    else:
        print("No data stored yet!")

def delete(clipboard_data):
    key = input("enter the key that refer to your copied data: ").strip().lower()
    clipboard_data.pop(key)
    dump_json_data(clipboard_data)

main()
