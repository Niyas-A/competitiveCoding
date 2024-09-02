class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        count = 1
        for point in points[1:]:
            if point[0]>end:
                end = point[1]
                count +=1
        return count

        