import json
import sys

from pathlib import Path
from rich.console import Console
from rich.table import Table, box

console = Console()

SOURCE_FOLDER = Path(__file__).parent
MAIN_FOLDER = SOURCE_FOLDER.parent
DATA_PATH = MAIN_FOLDER / "data" / "bugslist.json"

def load_bugs_data():
    try:
        with open(DATA_PATH) as file:
            bugs_output = json.load(file)
            return bugs_output

    except FileNotFoundError: print("Error: File not found, please check the file path and try again.")
    except json.JSONDecodeError: print("Error: Invalid syntax in JSON file, please check your file for any errors and try again.")
    except Exception as e: print(f"An unexpected error occurred: {e}")
    
    return None

def check_first_time(all_bugs):
    if all_bugs is None or not all_bugs: return True
    else: return False

def greetings(is_first_time):
    numbered_options = [1, 2, 3, 4, 5]
    print("\n\nCommand Line Interface Bug Tracker\n")

    if is_first_time: print(f"{numbered_options[0]}. Add your first bug")
    else: print(f"{numbered_options[0]}. Add a new bug")

    print(f"{numbered_options[1]}. View all bugs")
    print(f"{numbered_options[2]}. Update a bug")
    print(f"{numbered_options[3]}. Clear all bugs")
    print(f"{numbered_options[4]}. Exit\n\n")

    user_response = input(f"Please select an option number: {numbered_options[0]}-{numbered_options[-1]}\n> ")
    return user_response

def go_back_option():
    print("\n")
    go_back = input("Go back (Y/n)\n> ")

    if go_back == "Y" or go_back == 'y': main()
    elif go_back == "N" or go_back == 'n': pass
    else: pass

def add_bugs():
    numbered_options_status = [1, 2, 3]
    numbered_options_priority = [1, 2, 3, 4]

    name = input("\nBug name\n> ")

    print("\nBug status?\n")
    print(f"{numbered_options_status[0]}. On hold")
    print(f"{numbered_options_status[1]}. In progress")
    print(f"{numbered_options_status[2]}. Completed")

    status = input(f"\nPlease select an option number: {numbered_options_status[0]}-{numbered_options_status[-1]}\n> ")

    print("\nBug priority?\n")
    print(f"{numbered_options_priority[0]}. Low")
    print(f"{numbered_options_priority[1]}. Medium")
    print(f"{numbered_options_priority[2]}. High")
    print(f"{numbered_options_priority[3]}. Critical")

    priority = input(f"\nPlease select an option number: {numbered_options_priority[0]}-{numbered_options_priority[-1]}\n> ")

    if status == str(numbered_options_status[0]): status = "On hold"
    elif status == str(numbered_options_status[1]): status = "In progress"
    elif status == str(numbered_options_status[2]): status = "Completed"

    if priority == str(numbered_options_priority[0]): priority = "Low"
    elif priority == str(numbered_options_priority[1]): priority = "Medium"
    elif priority == str(numbered_options_priority[2]): priority = "High"
    elif priority == str(numbered_options_priority[3]): priority = "Critical"

    return name, status, priority

def save_bugs_data(all_bugs):
    try:
        with open(DATA_PATH, 'w') as file:
            json.dump(all_bugs, file, indent=4)
            return True
        
    except Exception as e:
        print(f"Failed to save data: {e}")
        return False
    
def view_all_bugs(all_bugs):
    table = Table(
        title="All Bugs\n",
        show_header=True,
        box=box.SIMPLE_HEAD
    )

    if not all_bugs:
        print("\nNo bugs to view!")
        return
    
    table.add_column("Name")
    table.add_column("Status")
    table.add_column("Priority")
    
    for bug_dictionary in all_bugs:
        for bug_name, details in bug_dictionary.items():
            status_text = details['status']
            priority_text = details['priority']

            if status_text == 'Completed': colored_status = f"[#009903]{status_text}[/#009903]"
            elif status_text == 'In progress': colored_status = f"[#dfaf87]{status_text}[/#dfaf87]"
            elif status_text == 'On hold': colored_status = f"[#afafaf]{status_text}[/#afafaf]"
            else: colored_status = status_text

            if priority_text == 'Critical': colored_priority = f"[#870000]{priority_text}[/#870000]"
            elif priority_text == 'High': colored_priority = f"[#cf0000]{priority_text}[/#cf0000]"
            elif priority_text == 'Medium': colored_priority = f"[#cf6b00]{priority_text}[/#cf6b00]"
            elif priority_text == 'Low': colored_priority = f"[#009903]{priority_text}[/#009903]"
            else: colored_priority = priority_text

            table.add_row(bug_name, colored_status, colored_priority)

    console.print(table)
    print("\n")

def clear_all_bugs():
    print('\n')
    clear_bugs_input = input("Are you sure you want to clear all bugs? (Y/n)\n> ")
    if clear_bugs_input == 'Y' or clear_bugs_input == 'y':
        return True
    return False

def get_update_details():
    update_numbered_options_status = [1, 2, 3]
    update_numbered_options_priority = [1, 2, 3, 4]

    print("\nUpdated bug status?\n")
    print(f"{update_numbered_options_status[0]}. On hold")
    print(f"{update_numbered_options_status[1]}. In progress")
    print(f"{update_numbered_options_status[2]}. Completed")

    updated_status = input(f"\nPlease select an option number: {update_numbered_options_status[0]}-{update_numbered_options_status[-1]}\n> ")

    print("\nUpdated bug priority?\n")
    print(f"{update_numbered_options_priority[0]}. Low")
    print(f"{update_numbered_options_priority[1]}. Medium")
    print(f"{update_numbered_options_priority[2]}. High")
    print(f"{update_numbered_options_priority[3]}. Critical")

    updated_priority = input(f"\nPlease select an option number: {update_numbered_options_priority[0]}-{update_numbered_options_priority[-1]}\n> ")

    if updated_status == str(update_numbered_options_status[0]): updated_status = "On hold"
    elif updated_status == str(update_numbered_options_status[1]): updated_status = "In progress"
    elif updated_status == str(update_numbered_options_status[2]): updated_status = "Completed"

    if updated_priority == str(update_numbered_options_priority[0]): updated_priority = "Low"
    elif updated_priority == str(update_numbered_options_priority[1]): updated_priority = "Medium"
    elif updated_priority == str(update_numbered_options_priority[2]): updated_priority = "High"
    elif updated_priority == str(update_numbered_options_priority[3]): updated_priority = "Critical"

    return updated_status, updated_priority

def update_bugs(all_bugs):
    if not all_bugs:
        print("No bugs to update")
        return
    
    view_all_bugs(all_bugs)
    bug_found = False
    bug_name = input("\nType the name of the bug you want to update\n> ")

    for bug_dictionary in all_bugs:
        if bug_name in bug_dictionary:
            bug_found = True

            new_status, new_priority = get_update_details()
            bug_dictionary[bug_name]['status'] = new_status
            bug_dictionary[bug_name]['priority'] = new_priority

            save_bugs_data(all_bugs)
            print(f"\nUpdated bug: {bug_name}")
            break
    

def main():
    all_bugs = load_bugs_data()
    is_first_time = check_first_time(all_bugs)
    user_response = greetings(is_first_time)

    if all_bugs is None: all_bugs = []

    if user_response == str(1):
        bug_name, bug_status, bug_priority = add_bugs()
        all_bugs.append({
            bug_name: {
                'status': bug_status,
                'priority': bug_priority
            }
        })

        save_bugs_data(all_bugs)
        print("Bug added.")
        go_back_option()
        
    elif user_response == str(2):
        view_all_bugs(all_bugs)
        go_back_option()

    elif user_response == str(3):
        update_bugs(all_bugs)
        go_back_option()

    elif user_response == str(4): 
        if clear_all_bugs():
            all_bugs = []
            save_bugs_data(all_bugs)
            print("All data successfully deleted")
        else:
            print("Cancelled")

        go_back_option()

    elif user_response == str(5):
        print("Exited program.")
        sys.exit()
main()