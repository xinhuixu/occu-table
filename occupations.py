import csv
import random

def buildDict():
    d = {}
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = row['Job Class']
            val = float(row['Percentage'])
            d[key] = val
    return d

def randOcc(d):
    randVal = random.random()*99.8 # [0, 99.8)
    # print randVal
    counter = 0.0
    for key in d:
        percent = d[key]
        counter += percent
        # print counter
        if randVal < counter:
            return key

def main():
    d = buildDict()
    print randOcc(d)
