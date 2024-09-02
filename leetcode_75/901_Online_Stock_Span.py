class StockSpanner(object):

    def __init__(self):
        self.stack = []
        # self.count = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        if len(self.stack) == 0:
            self.stack.append([price,res])
            return res
        else:
            # print(self.stack)
            while len(self.stack) != 0 and price >= self.stack[-1][0]:
                stackPr, stackSpn = self.stack.pop()
                res += stackSpn
            self.stack.append([price,res])
            return res


        # self.count += 1
        # while self.stack and price > self.stack[-1][0]:
        #     self.stack.pop()
        # if self.stack != []:
        #     print(self.stack)
        #     res = self.count - self.stack[-1][1]
        # else:
        #     res = 1 
        # self.stack.append([price,self.count])
        # print(self.stack)
        # return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)