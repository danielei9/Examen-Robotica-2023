from functions import *
def main():
    try:
        readData("./winequality.csv")
    except Exception as e:
        print("Ha ocurrido la excepción: ", e)
main()