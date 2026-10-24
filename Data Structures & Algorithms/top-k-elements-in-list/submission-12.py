class Solution:
    def topKFrequent(self,nums:List[int],k:int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        buckets =  [[] for i in range(len(nums)+1)]

        for num,freq in count.items():
            buckets[freq].append(num)
        res = []
        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                res.append(j)
            
                if len(res) == k:
                    return res

        return []