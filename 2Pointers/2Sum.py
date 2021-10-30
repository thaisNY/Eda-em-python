#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

#brutual force aproach with 2 loops
#Time complexity o(n²)
#class Solution:
#   def twoSum(self, nums: List[int], target: int) -> List[int]:
#       for i in range(len(nums)):
#           for j in range(i + 1, len(nums)):
#               if nums[i] + nums[j] == target:
#                   return [i,j]
# Aproach with 2 pointers Time: o(n)

def twoSum(nums, target):
        lef  = 0
        rig = len(nums) - 1
        while lef < rig:
            curr = nums[lef] + nums[rig] 
            if curr < target:
                lef += 1
            elif curr > target:
                rig -= 1
            else:
                return [lef, rig]
        return [-1, -1]

#Testes case

nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [2, 3, 4]
target2 = 6
nums3 = [1, 3, 5, 7]
target3 = 100
print(towSum(nums1, target1))
print(towSum(nums2, target2))
print(towSum(nums3, target3))