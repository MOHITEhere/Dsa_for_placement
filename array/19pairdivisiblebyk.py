#PAir divisible by k 

# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.

# Example 1:
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

# Example 2:
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).

# Example 3:
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.

def pairdivisiblebyk(arr, k):

    # Step 0: If length is odd → cannot form pairs
    if len(arr) % 2 != 0:
        return False

    freq = {}  # Dictionary to store remainder frequencies

    # Step 1: Count how many numbers give each remainder
    for num in arr:
        rem = num % k                    # Find remainder
        freq[rem] = freq.get(rem, 0) + 1  # Increase count

    # Step 2: Check if valid pairing is possible
    for rem in freq:

        # Case 1: remainder = 0
        # Must pair among themselves → count must be even
        if rem == 0:
            if freq[rem] % 2 != 0:
                return False

        # Case 2: remainder = k/2 (only when k is even)
        # Example: k=6 → rem=3 → 3+3=6
        elif 2 * rem == k:
            if freq[rem] % 2 != 0:
                return False

        # Case 3: general case
        # rem must match with (k - rem)
        else:
            if freq.get(rem) != freq.get(k - rem, 0):
                return False

    return True  # All conditions satisfied

arr = [1,2,3,4,5,6]
k = 7
print(pairdivisiblebyk(arr,k))