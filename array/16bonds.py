class Bound:

    def upper_bound(self, arr: list[int], target: int) -> int:
        """Finds smallest index where arr[index] > target."""
        low, high = 0, len(arr)

        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= target: #jaha equal nahi waha equal hain 
                low = mid + 1
            else:
                high = mid

        return low

    def lower_bound(self, arr: list[int], target: int) -> int:
        """Finds smallest index where arr[index] >= target."""
        low, high = 0, len(arr)

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target: #jaha equal hain waha equal nahi hian 
                low = mid + 1
            else:
                high = mid

        return low



arr = list(map(int, input().split()))
target = int(input())

ans = Bound()
print("Upper Bound index:", ans.upper_bound(arr, target))
print("Lower Bound index:", ans.lower_bound(arr, target))