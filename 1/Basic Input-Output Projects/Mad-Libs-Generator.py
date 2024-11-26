def mad_libs_generator():
    print("Welcome to the Mad Libs Generator!")
    
    # Collecting user inputs
    adjective = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    
    # Creating the story
    story = f"Once upon a time, there was a {adjective} {noun1} who loved to {verb} {adverb}. " \
            f"One day, it met a {noun2} and they became best friends."
    
    # Displaying the story
    print("\nHere is your Mad Libs story:")
    print(story)

# Run the Mad Libs generator
mad_libs_generator()