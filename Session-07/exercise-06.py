filehandle = open("mbox-short.txt", "r")
lines = filehandle.readlines()
found_lines = []
for line in lines:
    if line.startswith("From"):
        if line not in found_lines:
            found_lines.append(line.strip())
for i in found_lines:
    print(i[0:49])

filehandle.close()
