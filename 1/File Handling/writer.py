def create_and_write_file(file_path):
    initial_content = """This is the initial content of the file.
It contains some example text."""
    
    # Create the file and write initial content
    with open(file_path, 'w') as file:
        file.write(initial_content)
    print(f"File '{file_path}' created and initial content written successfully.")

def update_file(file_path):
    additional_content = "\nThis is the additional content being appended to the file."
    
    # Open the file in append mode to add more content
    with open(file_path, 'a') as file:
        file.write(additional_content)
    print(f"File '{file_path}' updated successfully.")

# Example usage
file_path = 'example.txt'  # Specify the name of the file

# Create and write to the file
create_and_write_file(file_path)

# Update the file
update_file(file_path)