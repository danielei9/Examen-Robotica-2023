import csv 
def readData(csvName):
    """
    csvName --> readData --> {}
    """
    with open (csvName,'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            print(row)