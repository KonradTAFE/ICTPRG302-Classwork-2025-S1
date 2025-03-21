letter = 'a'
occurrences = 0

filehandle = open("romeo-juliet.txt", "r+")
text = filehandle.readlines()
for line in text:
    for char in line:
        if char == letter:
            occurrences += 1
filehandle.write(f"\n\nLetter: {letter}\nOccurrences: {occurrences}")
filehandle.close()
