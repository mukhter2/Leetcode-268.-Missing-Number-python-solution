class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sz = len(nums)
        actual_sum_of_val=sz*(sz+1)
        actual_sum_of_val/=2
        total=0
        for x in nums:
            total+=x
        res=int(actual_sum_of_val-total)
        return res
        
