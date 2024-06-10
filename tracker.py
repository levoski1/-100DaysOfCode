import json
import os
import datetime
import pprint


def show_result(filename: str) -> list:
    """
    Show the result stored in a JSON file.

    Parameters:
        filename (str): The name of the file to read.

    Returns:
        list: The data loaded from the file as a list of dictionaries.
    """
    if os.path.exists(filename):
        if os.path.getsize(filename):  # Check if the file is not empty
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
    else:
        print("The file doesn't exist or is empty.\n")


def save_result(filename: str, data: dict) -> None:
    """
    Save data to a JSON file.

    Parameters:
        filename (str): The name of the file to write to.
        data (dict): The data to be saved to the file.
    """
    if os.path.exists(filename):
        if os.path.getsize(filename):
            with open(filename, 'r', encoding='utf-8') as fp:
                jsonload = json.load(fp)
            if list(data.keys())[0] in jsonload.keys():
                print(f"The data for {list(data.keys())[0]} already exists. Skipping.")
                return
            else:
                for key, value in data.items():
                    jsonload[key] = value
                    break
                with open(filename, 'w', encoding='utf-8') as fp:
                    json.dump(jsonload, fp, indent=4)
                    print("Data saved successfully.")
                    return
        with open(filename, 'w', encoding='utf-8') as fp:
            for key, value in data.items():
                data[key] = value
                json.dump(data, fp, indent=4)
                print("Data saved successfully.")
                break
    else:
        print("The file doesn't exist or is empty.\n")


def update_file(filename: str, formal_data: dict) -> list:
    """
    Update data in a JSON file.

    Parameters:
        filename (str): The name of the file to update.
        formal_data (dict): The data to be updated in the file.

    Returns:
        list: The updated data from the file as a list of dictionaries.
    """
    if os.path.exists(filename):
        if os.path.getsize(filename):  # Check if the file is not empty
            with open(filename, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            for key in formal_data.keys():
                if key not in save_data:
                    print(f"The date {key} doesn't exist in the file.")
                    return
                save_data[key] = formal_data.get(key)
            with open(filename, 'w', encoding='utf-8') as fp:
                json.dump(save_data, fp, ensure_ascii=False, indent=4)
                print('\nData updated successfully.')
    else:
        print("The file doesn't exist or is empty.\n")


def delete_data(filename: str, data: str) -> str:
    """
    Delete data from a JSON file.

    Parameters:
        filename (str): The name of the file to delete data from.
        data (str): The key of the data to be deleted from the file.

    Returns:
        str: The value associated with the deleted key.
    """
    if os.path.exists(filename):
        if os.path.getsize(filename):
            with open(filename, 'r', encoding='utf-8') as fp:
                load_data = json.load(fp)
            if data in load_data:
                save = load_data.pop(data)
                with open(filename, 'w', encoding='utf-8') as fp:
                    json.dump(load_data, fp, indent=4)
                print("Data deleted successfully.")
                return save
            else:
                print(f"The date {data} doesn't exist in the file.")
    else:
        print("The file doesn't exist or is empty.\n")


filename = 'data/progress.json'


# Main function
def main():
    print('''
    1. Show Results
    2. Save Progress
    3. Update Progress
    4. Delete Progress
            ''')

    while True:
        try:
            user_response = int(input('Please choose an option: '))
            print()

            if user_response == 1:
                get_user = show_result(filename)
                if get_user:
                    pprint.pprint(get_user)
                return

            elif user_response == 2:
                while True:
                    save = input('Did you resist the urge today? (YES/NO): ')
                    if save.upper() in ('YES', 'NO'):
                        time = datetime.datetime.now().strftime('%d-%m-%y')
                        data = {time: save.upper()}
                        save_result(filename, data)
                        return
                    else:
                        print('Please enter "YES" or "NO".\n')

            elif user_response == 3:
                while True:
                    print('Date format: D-M-Y (e.g: 04-07-24)')
                    time = input('Enter the date you want to update: ')
                    updated_response = input('What is the new response? (YES/NO): ')
                    if updated_response.upper() in ('YES', 'NO'):
                        data = {time: updated_response.upper()}
                        update_file(filename, data)
                        return
                    print('Please enter "YES" or "NO".\n')

            elif user_response == 4:
                while True:
                    print('Date format: D-M-Y (e.g: 04-07-24)')
                    user = input('Enter the date you want to delete: ')
                    delete_data(filename, user)
                    return

        except ValueError:
            print('Invalid Response! Please choose from the options.\n')


if __name__ == '__main__':
    main()
