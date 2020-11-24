"""
* author - ${USER}
* date - ${11/23/2020}
* time - ${3:30 pm}
* package - ${PACKAGE_NAME}
* Title - Replace of Username by using User Input
"""



import random
class FlipCoin2 :
    def __init__(self):
        self.FlipCoinNumber = 0
        self.Head = 0
        self.Tail =0
        self.headspercent = 0
        self.tailspercent = 0

    def NumberOfTimeFlipCoin(self):  # Coin flip Method
            self.FlipCoinNumber = random.randint(1, 2)
            x=input('enter number times coin flipped')
            for x in range(self.FlipCoinNumber) :
                self.HeadTail = random.randint(0,1)
                if self.HeadTail == 0 :
                    print('head wins')
                    self.Head = self.Head+1
                else :
                    print('tail wins')
                    self.Tail=self.Tail+1
    def CalculatePercentage(self):
        headspercent = self.Head / 10.0
        tailspercent = 100.0 - self.headspercent
        print("Heads percent: " + str(self.headspercent))
        print("Tails percent: " + str(self.tailspercent))

if __name__ == '__main__':
        try:
            object = FlipCoin2()
            object.CalculatePercentage()
        except:
            print('Exception Occured')
