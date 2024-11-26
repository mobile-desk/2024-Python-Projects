def merge_files(file1_path, file2_path, output_file_path):
    try:
        # Open the first file and read its content
        with open(file1_path, 'r') as file1:
            content1 = file1.read()
        
        # Open the second file and read its content
        with open(file2_path, 'r') as file2:
            content2 = file2.read()
        
        # Write the contents of both files into the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(content1)
            output_file.write("\n")  # Optional: Add a newline between contents
            output_file.write(content2)
        
        print(f"Files '{file1_path}' and '{file2_path}' merged into '{output_file_path}' successfully.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Example usage
file1_path = 'file1.txt'  # Replace with your first file path
file2_path = 'file2.txt'  # Replace with your second file path
output_file_path = 'merged_output.txt'  # Specify the output file name

# Create example files for demonstration
def create_example_files():
    with open(file1_path, 'w') as f1:
        f1.write("This is the content of the first file.\nIt has multiple lines.")
    
    with open(file2_path, 'w') as f2:
        f2.write("This is the content of the second file.\nIt also has multiple lines.")

# Create example files
create_example_files()

# Merge the two files
merge_files(file1_path, file2_path, output_file_path)