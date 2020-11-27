"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N.
"""
class Harmonic :
	#creating constructor
 def __init__(self):
        self.number
    def HarmonicValue(n):
        harmonicValue = 0
        harmonicNumber = int(input("Enter harmonic number: "))
	#Taking input values 
       if n > 0:
            for num in range(1, n + 1):
                harmonicValue = 1 / num
            else:
                print("number should be greater than zero")
        return harmonicValue
#main method
if __name__ == "__main__":
    try :
        object=Harmonic()
        object.harmonicValue()
    except :
        print('Exception Occured')
