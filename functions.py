import csv 
RED_WINE = 'red'
WHITE_WINE = 'white'

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
def split(d):
    """ 
    {} --> split --> ({},{})     
    """
    resultRed = {}
    resultWhite = {}

    redCount = 1
    whiteCount = 1

    for wine in d:
        try:
            if (d[wine]['type'] == WHITE_WINE) :
                del d[wine]['type']
                resultWhite[whiteCount] = d[wine]
                whiteCount = whiteCount + 1
            if (d[wine]['type'] == RED_WINE ):
                del d[wine]['type']
                resultRed[redCount] = d[wine]
                redCount = redCount + 1
        except KeyError:
            # print("No tiene type, fue procesado anteriormente. OK")
            pass


    return (resultRed,resultWhite)

def reducer(d,atributo):
    """ 
    {}, str --> split --> ({},{})     
    """
    lista = []
    for obj in d :
        try:
            lista.append(d[obj][atributo])
        except KeyError:
            raise ValueError("No existe el atributo '" + str( atributo ) + "' en el diccionario.")
    return lista

def silhouette():
    # No entiendo ... 