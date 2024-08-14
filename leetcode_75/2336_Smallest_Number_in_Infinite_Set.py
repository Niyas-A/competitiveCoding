import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.Set = set(range(1,1001))
        # print(Set)

    def popSmallest(self):
        """
        :rtype: int
        """
        li = list(self.Set)
        heapq.heapify(li)
        popped = heapq.heappop(li)
        self.Set = set(li)
        return popped   
        
    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.Set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)