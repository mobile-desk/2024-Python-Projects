sentence = input("Enter a word or sentence: ").stripip().lower()
if sentence == sentence[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
