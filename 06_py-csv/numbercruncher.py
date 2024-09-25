## Heading
# start 10:27

from pprint import pprint
import random

def readFile(fileName):
    data = open(fileName).read() # store raw file as text
    array = data.split("\n")[1:-2] # split by line breaks, exclude title and total
    
    for i in range(len(array)):
        temp = array[i].rsplit(",", 1) # temporary list holds job and %
        
        if temp[0][0]== "\"":
            temp[0] = temp[0][1:-1] # remove quotes
            
        temp[1] = float(temp[1]) # make the percentage a number
        array[i] = temp # feed into the array
        
    return array

def makeDict(filename):
    data = readFile(filename)
    result = {}
    for i in data:
        result.update({i[0]: i[1]})
    return result

def random(filename):
    data = makeDict(filename)
    n = 0
    temp = {}
    keys = list(data.keys())
    
    values = list(data.values())
    
    for i in range(len(keys)):

        temp.update({keys[i]: values[i]+n})
        n += values[i]
    return temp
        
    
    

print(random("occupations.csv"))