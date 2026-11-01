class Solution:
    def productExceptSelf(self,nums:List[int]) -> List[int]:

        prod, zero_count = 1,0
        n = len(nums)

        for i in nums:
            if i:
                prod *= i
            else:
                zero_count +=1

            if zero_count > 1:
                return [0] * n

        print (prod,zero_count)
        res = []
        for i in range(len(nums)):
            if zero_count:
                if nums[i] ==0:
                    res.append(prod)
                else:
                    res.append(0)

            if not zero_count:
                res.append(prod//nums[i])

        return res