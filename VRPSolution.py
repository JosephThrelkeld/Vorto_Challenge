import math
import sys

class VehicleLoad:
    def __init__(self, lnum, pickupPt, dropoffPt, loadDist, cenPickupDist, dropoffCenDist) -> None:
        self.loadNum = lnum
        self.pickupPoint = pickupPt
        self.dropoffPoint = dropoffPt
        self.loadDistance = loadDist
        self.centerPickupDistance = cenPickupDist
        self.dropoffCenterDistance = dropoffCenDist
def loadProblem(path):
    f = open(path, "r")
    vechicleLoadArr = []
    
    #Skip header line, contains no new information for us
    next(f)
    for line in f:
        currLineItems = line.split()
        currPickupPt = [float(numInStr.replace('(', '').replace(')','')) for numInStr in currLineItems[1].split(',')]
        currDropoffPt = [float(numInStr.replace('(', '').replace(')','')) for numInStr in currLineItems[2].split(',')]
        
        #Caluclating and storing cartesian distance b/n pickup and dropoff points for given load as it is most likely necessary to calculate all of these values anyways
        #This prevents repeating calculations for the cost of some storage
        vechicleLoadArr.append(VehicleLoad(int(currLineItems[0]), currPickupPt, currDropoffPt, calcCartesianDistance(currPickupPt, currDropoffPt), 
                                           calcCartesianDistance([0,0], currPickupPt), calcCartesianDistance(currDropoffPt, [0,0])))
        
    return vechicleLoadArr

def calcCartesianDistance(pt1, pt2):
    return abs(math.sqrt(pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2)))


MAX_MINUTES = 720
#Using greedy approach to fitting drivers to loads, start off with the 
 
 
problemLoads = loadProblem(sys.argv[1])
sortedProbLoads = sorted(problemLoads, key=lambda vl: vl.centerPickupDistance)
while len(sortedProbLoads) > 0:
    currDriveTime = sortedProbLoads[0].loadDistance + sortedProbLoads[0].centerPickupDistance
    currDriverSchedule = [sortedProbLoads.pop(0).loadNum]
    while True:
        closestDist = sys.float_info.max
        closestLoadIDX = -1
        for idx, load in enumerate(sortedProbLoads):
            traverseDistance = calcCartesianDistance(problemLoads[currDriverSchedule[-1] - 1].dropoffPoint, load.pickupPoint)
            if (currDriveTime + traverseDistance + load.loadDistance + load.dropoffCenterDistance) < MAX_MINUTES:
                closestDist = traverseDistance
                closestLoadIDX = idx
                break
        if closestDist == sys.float_info.max:
            break
        currDriveTime += traverseDistance + sortedProbLoads[closestLoadIDX].loadDistance
        currDriverSchedule.append(sortedProbLoads.pop(closestLoadIDX).loadNum)
    print(currDriverSchedule)
    
    
        
    