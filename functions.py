import csv 
def readData(csvName):
    """
    csvName --> readData --> {}
    """
    result = {}
    with open (csvName,'r') as csvFile:
        reader = csv.reader(csvFile)
        counter = 0
        for row in reader:
            # print(row)
            if(counter > 0):
                dataCount = 0
                dictionary = {}
                for data in row:
                    if(data != ''):
                        if(dataCount == 0):
                            dictionary['type'] = data
                        if(dataCount == 1):
                            dictionary['fixed acidity'] = data
                        if(dataCount == 2):
                            dictionary['volatile acidity'] = data
                        if(dataCount == 3):
                            dictionary['citric acid'] = data
                        if(dataCount == 4):
                            dictionary['residual sugar'] = data
                        if(dataCount == 5):
                            dictionary['chlorides'] = data
                        if(dataCount == 6):
                            dictionary['free sulfur dioxide'] = data
                        if(dataCount == 7):
                            dictionary['total sulfur dioxide'] = data
                        if(dataCount == 8):
                            dictionary['density'] = data
                        if(dataCount == 9):
                            dictionary['PH'] = data
                        if(dataCount == 10):
                            dictionary['sulphates'] = data
                        if(dataCount == 11):
                            dictionary['alcohol'] = data
                    dataCount = dataCount + 1
                if (len(dictionary) == 12):
                    result["dato" + str(counter)] = dictionary
            counter = counter + 1 
        if(len(result) < 10):
            raise ValueError("El fichero tiene menos de 10 líneas, con valor en todos los atributos.")

    return result


