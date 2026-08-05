#2 sum problem 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Sum:

    def two_sum(self,arr,target):

        hashmap={}

        for i in range(len(arr)):
            complement=target-i

            if complement in hashmap:
                return hashmap[complement],i 

            hashmap[arr[i]]=i

        return -1
# Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10 
# Output: true
# Explanation: The triplets [1, 3, 6] and [1, 2, 7] both sum to 10. 

    def three_sum(self,arr,target):
        n=len(arr)
        arr.sort()

        for i in range(n-2):
            left=i+1
            right=n-1

            while left<right:
                total=arr[i]+arr[left]+arr[right]

                if total==target:
                    return True 

                elif total>target:
                    high-=1

                elif total<target:
                    low-=1

        return False 



nums=list(map(int,input().split()))
target=int(input())
ans=Sum()
result=ans.two_sum(nums,target)
print(result)


'''3 SUM LEETCODE'''
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n=len(nums)
        nums.sort()

        x=[]

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue 

        left=i+1
        right=n-1

        while left<right:
            total=nums[i]+nums[left]+nums[right]

            if total==0:
                x.append[[nums[i],nums[left],nums[right]]]

                while left<right and nums[left]==nums[left-1]:
                    left+=1

                while left<right and nums[right]==nums[right+1]:
                    right-=1

            elif total<0:
                left+=1

            else:
                right-=1

        return x



nums=list(map(int,input().split()))
ans=Solution()
result=ans.three_sum(nums)
print(result)