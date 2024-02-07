import numpy as np
import math
import sys

class VehicleLoad:
    def __init__(self, lnum, pickupPt, dropoffPt, cartDist) -> None:
        self.loadNum = lnum
        self.pickupPoint = pickupPt
        self.dropoffPoint = dropoffPt
        self.cartesianDistance = cartDist

def loadProblem(path):
    f = open(path, "r")
    vechicleLoadArr = []
    
    #Skip header line, contains no new information for us
    next(f)
    for line in f:
        currLineItems = line.split()
        currPickupPt = np.array([float(numInStr.replace('(', '').replace(')','')) for numInStr in currLineItems[1].split(',')])
        currDropoffPt = np.array([float(numInStr.replace('(', '').replace(')','')) for numInStr in currLineItems[2].split(',')])
        
        #Caluclating and storing cartesian distance b/n pickup and dropoff points for given load as it is always necessary to calculate this
        #and this saves us from calculating this value multiple times during problem solving algorithm  
        vechicleLoadArr.append(VehicleLoad(currLineItems[0], currPickupPt, currDropoffPt, calcCartesianDistance(currPickupPt, currDropoffPt)))
        
    return vechicleLoadArr

def calcCartesianDistance(pt1, pt2):
    return abs(math.sqrt(pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2)))



for vehLoad in loadProblem(sys.argv[1]):
    print(str(vehLoad.loadNum) + " " + str(vehLoad.pickupPoint[0]) + " " + str(vehLoad.pickupPoint[1]) + " " + 
          str(vehLoad.dropoffPoint[0]) + " " + str(vehLoad.dropoffPoint[1]) + " " + str(vehLoad.cartesianDistance))