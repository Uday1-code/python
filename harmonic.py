class Harmonic :
    def __init__(self):
        self.number
    def HarmonicValue(n):
        harmonicValue = 0
        harmonicNumber = int(input("Enter harmonic number: "))
        if n > 0:
            for num in range(1, n + 1):
                harmonicValue = 1 / num
            else:
                print("number should be greater than zero")
        return harmonicValue

if __name__ == "__main__":
    try :
        object=Harmonic()
        object.harmonicValue()
    except :
        print('Exception Occured')
