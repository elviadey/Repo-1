import math

def Closest_Pair(Px,Py):
    if len(Px) <= 3:
        return BruteForceClosestPair(Px)

    mid = len(Px) // 2
    Lx = Px[:mid]
    Rx = Px[mid:]
    median = Px[mid]
    Ly,Ry = [], []
    for point in Py:
        if point[0] < int(median[0]):
            Ly.append(point)
        else:
            Ry.append(point)

    dl = Closest_Pair(Lx,Ly)
    dr = Closest_Pair(Rx,Ry)
    d = min(dl,dr)
    x_bar = Lx[-1][0]
    Sy = []
    for y in Py:
        if x_bar - d[0] < y[0] < x_bar + d[0]:
            Sy.append(y)
    
    Best_pair = (0,0)
    for i in range(len(Sy) - 1):
        for j in range(i+1, min(i + 7, len(Sy))):
            Pm = Sy[i]
            Qm = Sy[j]
            dm = Distance(Pm,Qm)
            if dm < d[0]:
                d = (dm,Pm,Qm)
    return d
    
def mergesortX(Array):
    if len(Array) == 1:
        return Array
    mid_point = len(Array) // 2
    left_part = Array[:mid_point]
    right_part = Array[mid_point:]

    left_sorted = mergesortX(left_part)
    right_sorted = mergesortX(right_part)
    i = j = 0
    C = []

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i][0] <= right_sorted[j][0]:
            C.append(left_sorted[i])
            i += 1
        elif right_sorted[j][0] < left_sorted[i][0]:
            C.append(right_sorted[j])
            j += 1
    while i < len(left_sorted) and j == len(right_sorted):
        C.append(left_sorted[i])
        i += 1
    while j < len(right_sorted) and i == len(left_sorted):
        C.append(right_sorted[j])
        j += 1
    return C

def mergesortY(Array):
    if len(Array) == 1:
        return Array
    mid_point = len(Array) // 2
    left_part = Array[:mid_point]
    right_part = Array[mid_point:]

    left_sorted = mergesortY(left_part)
    right_sorted = mergesortY(right_part)
    
    i = j = 0
    C = []

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i][1] <= right_sorted[j][1]:
            C.append(left_sorted[i])
            i += 1
        elif right_sorted[j][1] < left_sorted[i][1]:
            C.append(right_sorted[j])
            j += 1
    while i < len(left_sorted) and j == len(right_sorted):
        C.append(left_sorted[i])
        i += 1
    while j < len(right_sorted) and i == len(left_sorted):
        C.append(right_sorted[j])
        j += 1
    return C



def Distance(P1,P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)

def BruteForceClosestPair(Array):
    size = len(Array)
    minimum_distance = Distance(Array[0],Array[1])
    Target_Pair = (Array[0],Array[1])
    if size == 2:
        return Distance(Array[0],Array[1]),Array[0],Array[1]
    for i in range(0,size):
        for j in range(i+1,size):
            distance = Distance(Array[i],Array[j])
            if distance < minimum_distance:
                minimum_distance = distance
                Target_Pair = (Array[i],Array[j])
    return minimum_distance,Target_Pair

def main(P):

    Px = mergesortX(P)
    Py = mergesortY(P) 
    p, k = Closest_Pair(Px,Py)
    print("The pair of closest points are :",p)
    print("The distance between the points are :",k,"units")

#Specifying the set of points in a plane 
P = [(1, 30), (41, 51), (40, 50), (5, 1),(1,2), (12, 10), (8, 4)]
main(P)