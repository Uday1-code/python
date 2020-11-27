"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - Taking three input values and finding the roots of the equation
"""
import math

class Quadratic:

    def __init__(self, coefficient_a, coefficient_b, coefficient_c):

        self.coefficient_a = coefficient_a
        self.coefficient_b = coefficient_b
        self.coefficient_c = coefficient_c

    def calculateDeltaValue(self):

        deltaValue = self.coefficient_b * self.coefficient_b - 4 * self.coefficient_a * self.coefficient_c
        return abs(deltaValue)

    def calculateRoots(self):
	#calulating the roots
        delta = (self.calculateDeltaValue())
        rootOne = (-self.coefficient_b + math.sqrt(delta)) / (2 * self.coefficient_a)
        rootTwo = (-self.coefficient_b - math.sqrt(delta)) / (2 * self.coefficient_a)
        return rootOne, rootTwo
while True:
	#handling the exceptions
    try:
        aValue = int(input("Enter the value for coefficient a: "))
        bValue = int(input("Enter the value for coefficient b: "))
        cValue = int(input("Enter the value for coefficient c: "))
        break
    except ValueError:
        print("Enter valid integer")

#Main method
if __name__ == "__main__":
    quadratic = Quadratic(aValue, bValue, cValue)
    root1, root2 = quadratic.calculateRoots()
    print(f"Roots of given quadratic equation is: {root1} and {root2}")
