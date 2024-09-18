def readFile(fileName):
    data = open(fileName).read()
    array = data.split("\n")[1:]
    return array

print(readFile("occupations.csv"))