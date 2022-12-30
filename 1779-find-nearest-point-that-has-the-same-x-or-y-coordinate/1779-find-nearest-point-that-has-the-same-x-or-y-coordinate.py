class Solution(object):
    def ManhattanDistance(self,list1,list2):
       
        distance = abs(list1[0]-list2[0]) + abs(list1[1] - list2[1])
        return distance
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        my_point=[x,y]
        distanceCheck={}
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                distance= self.ManhattanDistance(points[i],my_point)
                if distance not in distanceCheck.keys():
                    distanceCheck[distance] = i
        print(distanceCheck)
        a=list(distanceCheck.keys())
        a.sort()
      
        if not a:
            return -1
        else:
            return distanceCheck[a[0]]
        