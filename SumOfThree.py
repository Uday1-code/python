"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - sum of three integers which will be add to zero
"""
    def sumToZero(array):
        length = len(array)
        for i in range(length - 2):
            for j in range(length - 1):
                for k in range(length):
                    if array[i] + array[j] + array[k] == 0:
                        print(str(array[i]) + " + " + str(array[j]) + " + " + str(array[k]) + " = 0")


def Array():
    while True:
        try:
            size = int(input("Enter size of array: "))
            break
        except :
            print('Exception Occured')
    array = []
    for idx in range(size):
	#handling the exceptions
        while True:
            try:
                number = int(input("Enter number to add in array: "))
                break
            except Exception as e:
                print(e)
        array.append(number)
    return array

#main metod
if __name__ == "__main__":
    filledArray = Array()
    sumToZero(filledArray)
