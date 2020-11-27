"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - check given year is leap or not
"""

class Leapyear :
    def __init__(self,yearValue):
        self.number=yearValue
    def checkLeapYear(self):
#checking a year is leap year or not
        if len(str(self.number)) == 4:
            if (self.number % 4 == 0 and self.number % 100 != 0) or self.number % 400 == 0:
                print(str(self.number) + " is Leap year")
            else:
                print(str(self.number) + " is not Leap year")
        else:
            print( "Please enter valid year")

#Main Method
if __name__ == "__main__":
    yearValue = int(input("Enter year: "))
    try :
        object=Leapyear(yearValue)
        object.checkLeapYear()
    except :
        print('Exception Occured')
