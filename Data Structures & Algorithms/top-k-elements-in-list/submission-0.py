class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = defaultdict(int)
        # for i in nums:
        #     res[i] += 1
        # sorted_nums = sorted(res.items(),key=lambda x:x[1],reverse=True)
        # print(sorted_nums)
        # return [nums for nums, freq in sorted_nums[:2]]

        return [ nums for nums, freq in Counter(nums).most_common(k)]