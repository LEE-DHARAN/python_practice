from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        length = len(nums) #5
        for i in range(length): #01234
            if nums[i] == 15:
                print(i)
                break    
            print(f"15 is not in index {i}")

solution = Solution()
solution.twoSum([2,15,11,7,17], 9)


