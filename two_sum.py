'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1 in nums:
            for num2 in nums[nums.index(num1)+1:]:
                if num1 + num2 == target:
                    num_ind = nums.index(num1)
                    nums[nums.index(num1)] = None
                    return [num_ind,nums.index(num2)]
'''

class Solution:
    def twoSum(self, nums, target):
        for n in range(0,len(nums)):
          if n + 1 > len(nums)-1:
              break
          if n == n + 1:
            if n + 2 > len(nums)-1:
                  break 
            if nums[n] + nums[n+2] == target:
                print([n,n+2]) 
          else:
            if nums[n] + nums[n+1] == target:
              print([n,n+1])
              
leet = Solution()
print(leet.twoSum([2,5,11],10))         