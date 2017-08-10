import fileinput

# Note: Print adds returns so use rstrip

file = "index.html"
tag = "<script type"
found = 0

for line in fileinput.input(file, inplace=True, backup=".bak"):
    if line == "\n" or line == "\r\n":
        print(line).rstrip()
    elif line.startswith(tag):
        found = 1
        print(line).rstrip()
    elif not (line.startswith(tag)) and found == 1:
        found = 0
        print "test"
        print(line).rstrip()
    else:
        print(line).rstrip()