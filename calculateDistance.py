import math

points = [(1, 2), (20, 15), (34, 6), (9, 8)]  #example points
distances = []  #list to store the distances

def euclideanDistance(pointA, pointB):
    (x1, y1) = pointA
    (x2, y2) = pointB

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

for i in range(len(points)):
    for l in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[l])
        distances.append(distance)

minDistance = min(distances)  #find the minimum distance inside the list

print("Minimum mesafe: ", minDistance)