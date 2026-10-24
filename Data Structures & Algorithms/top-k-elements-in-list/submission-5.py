class Solution:
    def topKFrequent(self,nums:List[int],k:int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] +=1
        sorted_nums = sorted(count.items(), key = lambda x: x[1], reverse = True)
        return [ i for i,j in sorted_nums[:k] ]
