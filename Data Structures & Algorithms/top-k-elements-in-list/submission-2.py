class Solution:
    def topKFrequent(self, nums:List[int],k:int) -> List[int]:

        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        res = []
        for i , j in count.items():
            res.append((j,i))

        sorted_nums = sorted(res, key = lambda x:x[0], reverse =True)

        return [ j for i,j in sorted_nums[:k]]

