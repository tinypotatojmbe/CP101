# Record Keeping App - Version 2
def record_keeping_app():
    records = {}  # Initialize an empty dictionary to store records

    while True:
        print("\nChoose an option:")
        print("1. Add Data")
        print("2. Delete Data")
        print("3. End")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            records[key] = value  # Add the key-value pair to the dictionary
            print("Current Records:", records)  # Display the current records

        elif choice == '2':
            key = input("Enter Key to delete: ")
            if key in records:
                del records[key]  # Remove the item from the dictionary
                print(f"'{key}' has been deleted.")
            else:
                print(f"Key '{key}' not found.")
            print("Current Records:", records)  # Display the current records

        elif choice == '3':
            print("THANK YOU")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")

# Run the Record Keeping App
record_keeping_app()
