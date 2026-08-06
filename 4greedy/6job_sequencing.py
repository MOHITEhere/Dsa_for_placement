# Problem: Job Sequencing with Deadlines

# You are given n jobs, where each job has:
# a deadline
# a profit
# Each job takes exactly 1 unit of time.

# 👉 You can schedule only one job at a time
# 🎯 Goal
# 👉 Maximize the total profit by scheduling jobs such that:

# Each job is completed before its deadline
# No two jobs overlap
# 🧾 Example
# Input:
# Jobs = [(id, deadline, profit)]
# J1 = (1, 2, 100)
# J2 = (2, 1, 19)
# J3 = (3, 2, 27)
# J4 = (4, 1, 25)
# J5 = (5, 3, 15)

# Step 2: Schedule jobs
# J1 → slot 2 ✅
# J3 → slot 1 ✅
# J4 → no slot ❌
# J2 → no slot ❌
# J5 → slot 3 ✅
# ✅ Output:
# Number of jobs = 3
# Maximum profit = 142
class Sequencing:
    def job_sequencing(self,n,jobs):
        jobs.sort(key=lambda x:x[2],reverse=True)

        max_deadline=max(job[1] for job in jobs)

        slots=[-1]*max_deadline

        total=0
        count=0

        for job in jobs:
            profit=job[2]
            deadline=job[1]

            for i in range(deadline,0,-1):
                if slots[i]==-1:
                    count+=1
                    total+=profit
                    slots[i]=profit

        return count,total

n=int(input())
deadline=list(map(int,input().split()))
profit=list(map(int,input().split()))
jobs=[]
for i in range(n):
    jobs.append((i,deadline[i],profit[i]))

ans=Sequencing()
result=ans.job_sequencing(jobs)
print(result)