from typing import List
#Two elements should have different indices and add up to a specific target number. Return the indices of the two numbers.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target number: "))
solution = Solution()
result = solution.twoSum(nums, target)
if result:
    print(f"Indices of the two numbers that add up to {target} are: {result}")
