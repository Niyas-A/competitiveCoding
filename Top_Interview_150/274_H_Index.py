class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        n = len(citations)
        for i in range(n):
            if citations[i]>= n-i:
                return n-i
        return 0
         