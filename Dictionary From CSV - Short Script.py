




import csv

def dict():
    file = open('products.csv','r')
    csvReader = csv.reader(file)
    titles = next(csvReader)
    blank = []

    for line in csvReader:
        blankd = {}
        blankd[titles[0]] = line[0]
        blankd[titles[1]] = line[1]
        blankd[titles[2]] = line[2]
        blank.append(blankd)
    for i in blank:
        print(i)
dict()
