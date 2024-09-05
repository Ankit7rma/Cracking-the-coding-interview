# MagicIndex:AmagicindexinanarrayA[0...n-1]isdefinedtobeanindexsuchthatA[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?


# Brute Force Approach with Recursion
def find_magic_index_brute_force_recursive(arr, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == index:
        return index
    return find_magic_index_brute_force_recursive(arr, index + 1)

# Optimized Approach with Recursion
def find_magic_index_optimized_recursive(arr, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == mid:
        return mid
    
    if arr[mid] > mid:
        return find_magic_index_optimized_recursive(arr, left, mid - 1)
    else:
        return find_magic_index_optimized_recursive(arr, mid + 1, right)

# Wrapper function for optimized approach
def find_magic_index_optimized(arr):
    return find_magic_index_optimized_recursive(arr, 0, len(arr) - 1)

# Example usage
arr = [-10, -5, 2, 3, 7]
print(f"Magic index (Brute Force Recursive): {find_magic_index_brute_force_recursive(arr)}")
print(f"Magic index (Optimized Recursive): {find_magic_index_optimized(arr)}")



# Non Distinct Values 
# Optimized Approach for Non-Distinct Values
def find_magic_index_non_distinct(arr):
    def binary_search(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == mid:
            return mid
        
        # To handle duplicates, we need to search both sides
        # Search left side
        left_index = min(mid - 1, arr[mid])
        left_result = binary_search(left, left_index)
        if left_result != -1:
            return left_result
        
        # Search right side
        right_index = max(mid + 1, arr[mid])
        return binary_search(right_index, right)

    return binary_search(0, len(arr) - 1)

# Example usage
arr = [-10, -5, 1, 2, 2, 3, 7]
print(f"Magic index (Non-Distinct Values): {find_magic_index_non_distinct(arr)}")
