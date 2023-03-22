import csv 
def readData(csvName):
    """
    csvName --> readData --> {}
    """
    result = {}
    with open (csvName,'r') as csvFile:
        reader = csv.reader(csvFile)
        counter = 1
        for row in reader:
            print(row)
            dataCount = 0
            dictionary = {}
            for data in row:
                if(data != ''):
                    if(dataCount == 0):
                        dictionary['type'] = data
                    if(dataCount == 0):
                        dictionary['fixed acidity'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                    if(dataCount == 0):
                        dictionary['type'] = data

                dataCount = datacount + 1

            result["dato" + str(counter)] = {}
            result["dato" + str(counter)] = {}
            counter = counter + 1 


