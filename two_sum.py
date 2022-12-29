class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1 in nums:
            for num2 in nums[nums.index(num1)+1:]:
                if num1 + num2 == target:
                    num_ind = nums.index(num1)
                    nums[nums.index(num1)] = None
                    return [num_ind,nums.index(num2)]
