# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Occurrence:

    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find_first(nums, target):
            low, high = 0, len(nums) - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1  # Keep searching left for earlier occurrence
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return first

        def find_last(nums, target):
            low, high = 0, len(nums) - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1  # Keep searching right for later occurrence
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return last

        return [find_first(nums, target), find_last(nums, target)]


nums = list(map(int, input().split()))
target = int(input())

ans = Occurrence()
print(ans.searchRange(nums, target))