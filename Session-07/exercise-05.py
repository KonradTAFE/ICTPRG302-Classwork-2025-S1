filehandle = open("mbox-short.txt", "r")
lines = filehandle.readlines()
found_lines = []
for line in lines:
    if line.startswith("From"):
        if line not in found_lines:
            found_lines.append(line.strip())
print(found_lines)
filehandle.close()
