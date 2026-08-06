# : Maximum Length Chain of Pairs
# You are given n pairs of numbers, where each pair is represented as:
# (a, b) such that a < b
# 👉 A pair (c, d) can follow (a, b) only if:
# b < c
# 🎯 Goal

# 👉 Find the maximum length chain that can be formed using these pairs.
# ⚡ Constraint
# Each pair can be used at most once
# Chain must satisfy:
# end of previous < start of next
# 🧾 Example

# Input:
# pairs = [(5,24), (15,25), (27,40), (50,60)]

# Step 1: Sort by second element (end time)
# (5,24), (15,25), (27,40), (50,60)
# Step 2: Build chain greedily
# Pick (5,24) ✅
# Skip (15,25) ❌ (15 < 24 → overlap)
# Pick (27,40) ✅
# Pick (50,60) ✅
# ✅ Output:
# Maximum chain length = 3
# ✔️ Chain formed:
# (5,24) → (27,40) → (50,60)

#same like maximum activity

class Pairs:
    def max_len_chain(self,chain,n):
        chain.sort(key=lambda x:x[1])

        length=1
        end_time=chain[0][1]

        for i in range(1,n):
            if chain[i][0]>end_time:
                length+=1
                end_time=chain[i][1]

        return length



n=int(input())
chain=[]
for _ in range(n):
    a=int(input())
    b=int(input())
    chain.append((a,b))

ans=Pairs()
result=ans.max_len_chain(chain,n)
print(result)

