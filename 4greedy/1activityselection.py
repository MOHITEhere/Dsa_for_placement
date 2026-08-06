# Problem: Activity Selection (Greedy)
# You are given n activities with their start times and end times.
# 👉 Your task is to select the maximum number of activities such that:

# No two activities overlap
# A person can do only one activity at a time
# 🎯 Goal
# 👉 Select the maximum number of non-overlapping activities


# 🧾 Example
# Input:
# start = [1, 3, 0, 5, 8, 5]
# end   = [2, 4, 6, 7, 9, 9]

# 🔍 Activities (start, end)
# (1,2), (3,4), (0,6), (5,7), (8,9), (5,9)
# ✅ Output:
# Maximum activities = 4


class Activity:

    def activity_selection(self,start,end):
        n=len(start)
        meetings=sorted(zip(start,end), key=lambda x:x[1])

        end_time=meetings[0][1]
        count=1

        for i in range(1,n):
            if end_time<=meetings[i][0]:
                count+=1
                end_time=meetings[i][1]

        return count


start=list(map(int,input().split()))
end=list(map(int,input().split()))
ans=Activity()
result=ans.activity_selection(start,end)
print(result)