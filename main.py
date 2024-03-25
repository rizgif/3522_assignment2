# main.py

import pandas as pd

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Process Web Orders")
        print("2. Check Inventory")
        print("3. Exit and Save Report")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            process_web_orders()
        elif choice == '2':
            check_inventory()
        elif choice == '3':
            exit_and_save_report()
            break  # Exits the while loop, thus terminating the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")



def process_web_orders():
    filename = input("Enter the name of the Excel file with web orders: ")
    
    try:
        orders = pd.read_excel(filename)
        # Process orders here
    except FileNotFoundError:
        print("The file was not found. Please make sure the file name is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_inventory():
    pass

def exit_and_save_report():
    pass

if __name__ == "__main__":
    main_menu()
