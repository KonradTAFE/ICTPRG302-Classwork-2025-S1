filehandle = open("mbox-short.txt", "r")
lines = filehandle.readlines()
found_lines = []
for line in lines:
    if line.startswith("From"):
        found_lines.append(line)
print(found_lines)
filehandle.close()