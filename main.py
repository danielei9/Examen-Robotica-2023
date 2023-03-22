from functions import *
def main():
    try:
        print(readData("./winequality.csv"))
    except Exception as e:
        print("Ha ocurrido la excepción: ", e)
main()