"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - Replace of Username by using User Input
"""

class Leapyear :
    def __init__(self):
        self.number
    def checkLeapYear(year):
        if len(str(year)) == 4:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                print(str(year) + " is Leap year")
        else:
            print(str(year) + " is not Leap year")
    else:
            print( "Please enter valid year")
yearValue = int(input("Enter year: "))
if __name__ == "__main__":
    yearValue = int(input("Enter year: "))
    try :
        object=Leapyear()
        object.checkLeapYear()
    except :
        print('Exception Occured')
