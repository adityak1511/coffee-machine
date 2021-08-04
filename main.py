import os
import json
from coffee_machine import CoffeeMachine
from validator import InputProcessor


def yield_test_case_files():
    """
    Return the test case json files one by one.
    """
    for dir_path, dir_names, files in os.walk('./test_cases'):
        for file in files:
            if file.endswith('json'):
                yield file


def get_json_content(file):
    """
    Parse the json content out of each file.
    """
    file_path = os.path.join(os.path.dirname(__file__), f'test_cases/{file}')
    try:
        with open(file_path, 'r') as f:
            json_str = f.read()
            f.close()
    except IOError:
        print('File not found: ' + str(file_path))
        return None
    return json.loads(json_str)


if __name__ == "__main__":
    """
    The entry point for our project. We process the test cases one by one.
    """
    for test_case_file in yield_test_case_files():
        print(f'\n------Processing file {test_case_file}:------\n')
        input_json = get_json_content(test_case_file)
        if not input_json:
            continue
        is_valid, outlet_count, total_items_quantity, beverage_dicts = InputProcessor().get_input_params(input_json)
        if not is_valid:
            continue
        machine = CoffeeMachine(outlet_count, total_items_quantity, beverage_dicts)
        machine.serve_beverages()
