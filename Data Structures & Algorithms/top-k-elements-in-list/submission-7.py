class Solution:
    def topKFrequent(self,nums:List[int],k:int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        return heapq.nlargest(k,count, key = count.get)
