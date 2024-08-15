import heapq
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapify(head_workers)
        heapify(tail_workers)
        
        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates 

        for _ in range(k): 
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]: 
                answer += heappop(head_workers)
                if next_head <= next_tail: 
                    heappush(head_workers, costs[next_head])
                    next_head += 1
            else: 
                answer += heappop(tail_workers)
                if next_head <= next_tail:  
                    heappush(tail_workers, costs[next_tail])
                    next_tail -= 1
                    
        return answer
        # cost = 0
        # size = len(costs)
        # count = 0
        # lf = 0
        # rf = 0
        # if size > 2*candidates:
        #         left = costs[:candidates]
        #         right = costs[-candidates:]
        #         heapq.heapify(left)
        #         heapq.heapify(right)
        # while count<k:
        #     if size > 2*candidates:
        #         # l = heapq.heappop(left)
        #         # r = heapq.heappop(right)
        #         l = left[0]
        #         r = right[0]
        #         if l<=r:
        #             # heapq.heappush(right, r)
        #             heapq.heappop(left)
        #             heapq.heappush(left, costs[candidates+lf])
        #             cost += l
        #             lf += 1
        #         else:
        #             # heapq.heappush(left, l)
        #             heapq.heappop(right)
        #             heapq.heappush(right, costs[-candidates-1-rf])
        #             cost += r
        #             rf += 1
        #         count += 1
        #         size -= 1
        #         if size == 2*candidates:
        #             costs = list(left) + list(right) 
        #     else:
        #         heapq.heapify(costs)
        #         cost += heapq.heappop(costs)
        #         count += 1
        # return cost

        