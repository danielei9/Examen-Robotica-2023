from functions import *
def main():
    try:
        # wines = readData("./wineTest.csv")
        wines = readData("./winequality.csv")
        (redWines,whiteWines) = split(wines)
        whiteList = reducer(whiteWines,"alcohol")
        redList = reducer(redWines,"alcohol")
        silhouette(whiteList,redList)
        print(lista)
    except Exception as e:
        print("Ha ocurrido la excepción: ", e)
main()