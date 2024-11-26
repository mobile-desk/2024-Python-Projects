def read_and_display_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            print("File Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = input("Enter the path of the file to read: ")
read_and_display_file(file_path)


# read csv 
import pandas as pd


df = pd.read_csv('file.csv')
print(df)