import random
import math
import time

maxNum = 1000
euclidianCounter = 0

def createPoints(n, dimention):
    points = [[random.random()*maxNum for i in range(dimention)] for i in range(n)]
    sortPointsbyX(points)
    print(points)
    return points

def displayPoints(points):
    print(points)

def euclidian(point1,point2):
    dimention = len(point1)
    sum=0;
    for i in range(dimention):
        sum+= (point1[i]-point2[i])**2
    return math.sqrt(sum)

def closestPointBrute(points):
    if len(points)==2 :
        return points;
    else:
        global euclidianCounter
        min = 9999999999999;
        minPair = [points[0],points[0]];
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                euclidianCounter+=1
                if (euclidian(points[i],points[j])<min):
                    min = euclidian(points[i],points[j])
                    minPair = [points[i],points[j]]
        return minPair

def sortPointsbyX(points):
    points.sort(key=lambda x: x[0])

def getPointsinStrip(points, closestDistance):
    strip = []
    mid = points[len(points)//2]
    for i in range(len(points)):
        if (abs(points[i][0]-mid[0])<closestDistance):
            strip.append(points[i])
    return strip

def isClosestPairCandidate(points1,points2, closestDistance):
    for i in range(len(points1)):
        if (abs(points1[i]-points2[i])>=closestDistance):
            return False;
    return True;

def closestPointsDividenConquer(points):
    if (len(points)<=3):
        return closestPointBrute(points)
    else:
        mid = len(points)//2
        points1 = points[:mid]
        points2 = points[mid:]
        closestPair1 = closestPointsDividenConquer(points1)
        closestPair2 = closestPointsDividenConquer(points2)

        if (euclidian(closestPair1[0],closestPair1[1])<=euclidian(closestPair2[0],closestPair2[1])):
            closestPair = closestPair1
        else:
            closestPair = closestPair2

        closestDistance = euclidian(closestPair[0],closestPair[1])

        strip = getPointsinStrip(points,closestDistance)

        global euclidianCounter
        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                if (isClosestPairCandidate(strip[i],strip[j],closestDistance)):
                    euclidianCounter+=1
                    if (euclidian(strip[i],strip[j])<closestDistance):
                        closestPair = [strip[i],strip[j]]
                        closestDistance = euclidian(strip[i],strip[j])
        return closestPair


if __name__ == "__main__":
    n = int(input("n = "))
    dimention = int(input("dimention = "))
    points = createPoints(n,dimention)
    displayPoints(points)
    # print(euclidian(points[0],points[1]))
    
    sa = time.time()
    closestPairBrute = closestPointBrute(points)
    fa = time.time()
    print("closest pair by brute = ", closestPairBrute)
    print(euclidian(closestPairBrute[0],closestPairBrute[1]))
    print("brute time = ", (fa-sa)*1000)
    print("ecludian = ", euclidianCounter)
    
    euclidianCounter = 0
    sb = time.time()
    closestPair = closestPointsDividenConquer(points)
    fb = time.time()
    print("closest pair by dividenconq = ",closestPair)
    print(euclidian(closestPair[0],closestPair[1]))
    print("divide n conquer time = ",(fb-sb)*1000)
    print("ecludian = ", euclidianCounter)

