# MagicIndex:AmagicindexinanarrayA[0...n-1]isdefinedtobeanindexsuchthatA[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?


# Brute Force Approach
def find_magic_index_brute_force(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

# Optimized Approach
def find_magic_index_optimized(arr):
    def binary_search(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == mid:
            return mid
        
        if arr[mid] > mid:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)
    
    return binary_search(0, len(arr) - 1)

# Example usage
arr = [-10, -5, 2, 3, 7]
print(f"Magic index (Brute Force): {find_magic_index_brute_force(arr)}")
print(f"Magic index (Optimized): {find_magic_index_optimized(arr)}")

