import random
import math
import time

maxNum = 1000
euclidianCounter = 0

def createPoints(n, dimention):
    # membuat array of points sebanyak n, poin yang dibentuk memiliki dimensi dimention
    points = [[round((random.random()*maxNum),2) for i in range(dimention)] for i in range(n)]
    sortPointsbyX(points)
    return points

def displayPoints(points):
    # menampilkan titik-titik
    print(points)

def euclidian(point1,point2):
    # menghitung jarak antara dua titik
    dimention = len(point1)
    sum=0;
    for i in range(dimention):
        sum+= (point1[i]-point2[i])**2
    return math.sqrt(sum)

def closestPointBrute(points):
    # mencari titik terdekat dengan pendekatan brute force
    if len(points)==2 :
        return points;
    else:
        global euclidianCounter
        min = 9999999999999;
        minPair = [points[0],points[0]];
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                euclidiandis = euclidian(points[i],points[j])
                euclidianCounter+=1
                if (euclidiandis<min):
                    min = euclidiandis
                    minPair = [points[i],points[j]]
        return minPair

def sortPointsbyX(points):
    # mengurutkan array of titik dengan axis x terurut membesar
    points.sort(key=lambda x: x[0])

def getPointsinStrip(points, closestDistance):
    # mengembalikan array of titik yang jarak axis x nya dengan strip sebesar < closestdistance sementara
    strip = []
    mid = points[len(points)//2]
    for i in range(len(points)):
        if (abs(points[i][0]-mid[0])<closestDistance):
            strip.append(points[i])
    return strip

def isClosestPairCandidate(point1,point2, closestDistance):
    # menentukan apakah sepasang titik merupakan kandidat closest pair
    # yakni apabila pada setiap axis jarak point1 dan point 2 < closest distance sementara
    for i in range(len(point1)):
        if (abs(point1[i]-point2[i])>=closestDistance):
            return False;
    return True;

def closestPointsDividenConquer(points):
    # menentukan sepasang titik terdekat dengan pendekatan divide & conquer
    if (len(points)<=3):
        # SOLVE : jika hanya terdapat <=3 titik tidak perlu melakukan divide & conquer
        return closestPointBrute(points)
    else:
        # DIVIDE : membagi titik-titik menjadi dua bagian points1,points2 sama banyak 
        # (jika ganjil len(points1)= len(points2)+1)
        mid = len(points)//2
        points1 = points[:mid]
        points2 = points[mid:]

        # CONQUER : secara rekursif mencari sepasang titik terdekat dengan 
        # algoritma divide & conquer
        closestPair1 = closestPointsDividenConquer(points1)
        closestPair2 = closestPointsDividenConquer(points2)

        # COMBINE
        if (euclidian(closestPair1[0],closestPair1[1])<=euclidian(closestPair2[0],closestPair2[1])):
            closestPair = closestPair1
        else:
            closestPair = closestPair2

        closestDistance = euclidian(closestPair[0],closestPair[1])

        # penanganan kasus apabila sepasang titik terdekat terpisah pada saat DIVIDE
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

