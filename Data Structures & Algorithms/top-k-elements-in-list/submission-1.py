class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for i in nums:
            res[i] += 1

        arr = []

        for i,j in res.items():
            arr.append([j,i])
        
        arr.sort()

        res1 = []

        while len(res1) < k:

            res1.append(arr.pop()[1]) 

        return res1

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         arr = []
#         for num, cnt in count.items():
#             arr.append([cnt, num])
#         arr.sort()

#         res = []
#         while len(res) < k:
#             res.append(arr.pop()[1])
#         return res