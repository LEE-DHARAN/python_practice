from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums) #0
 
        for i in range(n):
            complement = target - nums[i] #0
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i #[2,0]
 
        return []  # No solution found
    
        
solution = Solution()
result = solution.twoSum([2, 15, 11, 17,7], 9)
print(result)