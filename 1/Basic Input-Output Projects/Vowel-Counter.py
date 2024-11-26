def check_vowel(content):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0


    for char in content:
        if char.lower() in vowels:
            count += 1
    return count
    

def read_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        check_vowel(content)
    return content

# Example usage

file_path = input("Enter the file path [make sure to include the file extension example 'C:\Users\USER\Documents\file.txt']: ")

check_vowel(read_file(file_path))

