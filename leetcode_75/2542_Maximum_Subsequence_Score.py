import heapq
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        lst=list(zip(nums2,nums1))
        lst.sort(key=lambda x:(-x[0],-x[1]))
        flst=[]
        heapq.heapify(flst)
        i=0
        sm=0
        ef=float("infinity")
        prd=float("-infinity")
        while i<k:
            x=lst.pop(0)
            heapq.heappush(flst,x[1])
            ef=min(ef,x[0])
            sm+=x[1]
            i+=1
        prd=max(prd,sm*ef)
        while lst:
            x=heapq.heappop(flst)
            sm-=x
            y=lst.pop(0)
            heapq.heappush(flst,y[1])
            ef=min(ef,y[0])
            sm+=y[1]
            prd=max(prd,sm*ef)
        return prd
        # n2 = sorted(nums2,reverse=True)
        # n1 = [x for _,x in sorted(zip(nums2,nums1), reverse=True)]
        # print(n1)
        # print(n2)
        # max_score = 0
        # for l in range(0,len(nums1)-k+1):
        #     print(n1[l:l+k])
        #     print(n2[l:l+k])
        #     print(sum(n1[l:l+k]))
        #     print(min(n2[l:l+k]))
        #     score = sum(n1[l:l+k])*min(n2[l:l+k])
        #     if score>max_score:
        #         max_score = score
        # return max_score
        # start = 0
        # end = k-1
        # max_score = 0
        # while end<len(nums1):
        #     if start == 0:
        #         sum1 = sum(nums1[start:end+1]) 
        #     else:
        #         sum1 = sum1 + nums1[end] - nums1[start-1]
        #     print(sum1)
        #     print(nums2[start:end+1])
        #     score = min(nums2[start:end+1])*sum1
        #     print(score)
        #     if score > max_score:
        #         max_score = score
        #     end = end+1
        #     start = start+1

        # return max_score

        