# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements 
# to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., 
# [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

# Input: arr[] = [1, 2, 3, 4, 5, 2]
# Output: [5 2]
# Explanation: 5 is greater than all the elements to its right i.e., [2], 
# therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader
class Leader:
    def leader_in_array(self,arr):
        n=len(arr)
        max_element=arr[-1]
        output=[max_element]

        for i in range(n-2,-1,-1):
            if arr[i]>max_element:
                max_element=arr[i]
                output.append(max-max_element)

        return output[::-1]


arr=list(map(int,input().split()))
ans=Leader()
result=ans.leader_in_array(arr)
print(result)
