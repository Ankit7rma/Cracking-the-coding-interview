# Power Set: Write a method to return all subsets of a set.


# BRUTE
# REcursive 
def power_set_brute_force(s):
    def generate_subsets(index, current, result):
        if index == len(s):
            result.append(current[:])
            return
        # Exclude the current element
        generate_subsets(index + 1, current, result)
        # Include the current element
        current.append(s[index])
        generate_subsets(index + 1, current, result)
        # Backtrack
        current.pop()
    
    result = []
    generate_subsets(0, [], result)
    return result

# Example usage
s = [1, 2, 3]
print(f"Power set (Brute Force): {power_set_brute_force(s)}")

# Iterative 
def power_set_brute_force(s):
    ans =[[]]
    for i in s:
        ans+= [item + [i] for item in ans ]
    return ans 

# Optimised Bit Manipulation 
def power_set_bit_manipulation(s):
    n = len(s)
    result = []
    for i in range(1 << n):  # 2^n possible subsets
        subset = []
        for j in range(n):
            if i & (1 << j):  # Check if the j-th bit is set
                subset.append(s[j])
        result.append(subset)
    return result

# Example usage
s = [1, 2, 3]
print(f"Power set (Bit Manipulation): {power_set_bit_manipulation(s)}")
