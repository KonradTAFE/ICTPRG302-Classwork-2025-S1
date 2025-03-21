filehandle = open("mbox-short.txt", "r")
lines = filehandle.readlines()
for line in lines:
    if line.startswith("From"):
        print(line.strip())
filehandle.close()