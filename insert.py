import fileinput

# Note: Print adds returns so use rstrip

file = "index.html"
findtag = "<script type"
inserttag = '<script type="text/javascript" src="playermarkers/playermarkers.js"></script>'
found = 0

for line in fileinput.input(file, inplace=True, backup=".bak"):
    if line == "\n" or line == "\r\n":
        print(line).rstrip()
    elif line.startswith(findtag):
        found = 1
        print(line).rstrip()
    elif not (line.startswith(findtag)) and found == 1:
        found = 0
        print inserttag
        print(line).rstrip()
    else:
        print(line).rstrip()