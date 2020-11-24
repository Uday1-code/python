"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - Replace of Username by using User Input
"""

import math
class Factor :
    def __init__(self):
        self.number = number
    def findPrimeFactor(n):
        for num in range(2, int(math.sqrt(n))):
            if num == 2 or num % 2 != 0:
                while n % num == 0:
                    print(num)
                    n = n / num
                    if n > 2:
                     print(int(n))

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    try:
        object=Factor(number)
        object.findPrimeFactor
    except :
        print('Exception Occured')
