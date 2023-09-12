#!/usr/bin/python3
""" Load, add, save """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main(args):
    """
    Main function to add items to a JSON file.

    Args:
        args (list): A list of items to add to the JSON file.

    Returns:
        None
    """
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(args)
    save_to_json_file(existing_list, "add_item.json")


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
