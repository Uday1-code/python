"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - Replace of Username by using User Input
"""


class PowerOfTwo :
    def __init__(self,Number) :
        self.Number= Number
    def CheckNumber(self):
        if 0 <= self.Number < 31:
            self.PowerTable()
        else :
            print('Out of Range')
            for x in range(self.Number+1):
                print("Square of {0} is {1} ".format(x,x**2))
if __name__=='__main__' :
    try :
        Number=input("Enter a number")
        object=PowerOfTwo(Number)
        object.CheckNumber()
    except :
        print('Exception Ocured')



