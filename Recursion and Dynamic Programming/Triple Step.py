# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time, implement a method to count how many possible ways the child can run up the stairs.


### Brute Force Approach

# To solve this problem using brute force, we can use recursion. The child has three options at every step:
# - Hop 1 step
# - Hop 2 steps
# - Hop 3 steps

# For a given number of steps `n`, we can break down the problem recursively as:
# - The number of ways to reach step `n` is the sum of ways to reach steps `n-1`, `n-2`, and `n-3`.

# The base cases will be:
# - If `n == 0`: There's only one way to stay on the ground (i.e., do nothing).
# - If `n < 0`: No valid way to move, so return 0.

# Here's the brute-force recursive solution:

# ```python
def count_ways_brute(n):
    # Base cases
    if n == 0:
        return 1  # There's one way to stay at the ground (do nothing)
    elif n < 0:
        return 0  # No way to move if negative steps
    
    # Recursive calls for n-1, n-2, and n-3
    return count_ways_brute(n-1) + count_ways_brute(n-2) + count_ways_brute(n-3)

# Example usage
n = 4
print(f"Number of ways (Brute Force) to climb {n} steps: {count_ways_brute(n)}")
# ```

### Optimized Approach (Using Dynamic Programming)

# The brute force approach leads to overlapping subproblems (i.e., recalculating the same steps multiple times). We can optimize this using dynamic programming (memoization or tabulation).

# In this approach, we store the results of the subproblems in an array and reuse them when needed. This reduces the time complexity from exponential to linear.

# #### Dynamic Programming (Top-Down with Memoization):

# ```python
def count_ways_memo(n, memo):
    # Base cases
    if n == 0:
        return 1  # One way to stay at the ground (do nothing)
    elif n < 0:
        return 0  # No way to move if negative steps
    
    # If already computed, return the stored value
    if memo[n] != -1:
        return memo[n]
    
    # Store the result of the recursive calls in the memo array
    memo[n] = count_ways_memo(n-1, memo) + count_ways_memo(n-2, memo) + count_ways_memo(n-3, memo)
    return memo[n]

def count_ways_optimized(n):
    # Create a memo array initialized to -1
    memo = [-1] * (n + 1)
    return count_ways_memo(n, memo)

# Example usage
n = 4
print(f"Number of ways (Optimized) to climb {n} steps: {count_ways_optimized(n)}")
 

# #### Dynamic Programming (Bottom-Up with Tabulation):

# In this version, we build the solution iteratively from the bottom up, filling an array to store results for all possible steps.

 
def count_ways_bottom_up(n):
    if n == 0:
        return 1
    
    # Create a dp array to store the number of ways to reach each step
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # There's one way to stay at the ground (do nothing)
    if n >= 1:
        dp[1] = 1  # One way to reach the 1st step
    if n >= 2:
        dp[2] = 2  # Two ways to reach the 2nd step (1+1 or 2)
    
    # Fill the dp array using the recursive relation
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]

# Example usage
n = 4
print(f"Number of ways (Bottom-Up) to climb {n} steps: {count_ways_bottom_up(n)}")
 

# ### Time Complexity:

# - **Brute Force**: `O(3^n)` because at each step, you are making three recursive calls.
# - **Optimized (Memoization)**: `O(n)` since each subproblem is solved only once.
# - **Optimized (Bottom-Up)**: `O(n)` because we compute each step exactly once.

# ### Space Complexity:

# - **Brute Force**: `O(n)` for the recursive stack depth.
# - **Memoization**: `O(n)` for the recursive stack and memo array.
# - **Bottom-Up**: `O(n)` for the dp array.