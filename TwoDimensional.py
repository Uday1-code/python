"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - creating a two dimensional array and storing values inside it.
"""


import matrix as matrix


class twoDimensional :

    def Parameters(self):
        while True :
		#Exception handling
            try :
                Rows= int(input("Number of rows:"))
                Columns = int(input("Number of columns:"))
                if(Rows or Columns < 0):
		#asking to enter input values
                    print('enter greater values')
                    break
                    continue
                break
            except Exception :
                print('Exception Occured')

        self.array = []
        for column in range(Columns):
            matrix = []
        for row in range(Rows):
            while True:
                try:
                    element = int(input("Enter element in array: "))
                    matrix.append(element)
                    break
                except Exception :
                    print('Exception occured')

        self.array.append(matrix)

    def printArray(self):
        print(self.array)

#main method
if __name__ == "__main__":
    object = twoDimensional()
    object.Parameters()
    object.printArray()
