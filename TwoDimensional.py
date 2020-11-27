import matrix as matrix


class twoDimensional :

    def Parameters(self):
        while True :
            try :
                Rows= int(input("Number of rows:"))
                Columns = int(input("Number of columns:"))
                if(Rows or Columns < 0):
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


if __name__ == "__main__":
    object = twoDimensional()
    object.Parameters()
    object.printArray()
