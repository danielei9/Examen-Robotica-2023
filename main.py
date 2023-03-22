from functions import *
def main():
    try:
        wines = readData("./wineTest.csv")
        # wines = readData("./winequality.csv")
        (redWines,whiteWines) = split(wines)
        print(redWines)
    except Exception as e:
        print("Ha ocurrido la excepción: ", e)
main()