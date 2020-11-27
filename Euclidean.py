
import math
import sys
class EuclideanDistance:
  pointA=0
  pointB=0

  def __init__(self,pointA,pointB):
    """
       define Constructor
       Operation:To initialize Data Members And Instantiate Object
      """
    self.pointA=pointA
    self.pointB=pointB

  def Distancecalculation(self):
    """ Definition of  Method
       Operation:To calculate Euclidean Distastance from origin
       return Type:Does not return any value
    """
    distance = math.sqrt(self.pointA * self.pointA + self.pointB * self.pointB)
    print("Euclidean Distastance from",self.pointA, self.pointB,"is= ",distance)

if __name__ == '__main__':
  pointAValue=int(input('enter x value'))
  pointBValue=int(input('enter Y value'))
  object=EuclideanDistance(pointAValue,pointBValue)
  object.calculateDistance()
