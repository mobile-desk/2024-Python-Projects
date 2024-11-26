sentence = input("Enter a word or sentence: ")
track = {}
for i in sentence:
    if i in track:
        track[i] += 1
    else:
        track[i] = 1


print(track)