# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.


#  Let's explore both brute force and optimized approaches to solve the problem of finding the number of unique paths in a grid with obstacles.

# ### Brute Force Approach

# The brute force approach involves exploring all possible paths using recursion. However, this approach is highly inefficient for larger grids due to its exponential time complexity. The recursive function will explore all possible ways to move down and right, but it does not handle obstacles efficiently.

# Here is the brute force approach using recursion:

 
def unique_paths_brute(grid):
    def count_paths(x, y):
        # Base case: reached the bottom-right corner
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return 1
        
        # If out of bounds or obstacle encountered
        if x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 1:
            return 0
        
        # Move right and down
        return count_paths(x + 1, y) + count_paths(x, y + 1)
    
    # Starting point
    return count_paths(0, 0)

# Example usage
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(f"Number of unique paths (Brute Force): {unique_paths_brute(grid)}")
 
### Optimized Approach

# The optimized approach uses dynamic programming to efficiently compute the number of unique paths while considering obstacles. We use a 2D DP table where each cell `dp[i][j]` represents the number of unique paths to reach that cell.

# Here's how you can implement this approach:

#### Dynamic Programming (Tabulation)
 
def unique_paths_optimized(grid):
    m, n = len(grid), len(grid[0])
    
    # If the start or end cell is an obstacle, return 0
    if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        return 0
    
    # Create a 2D dp array
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting cell
    dp[0][0] = 1
    
    # Fill the first row
    for j in range(1, n):
        if grid[0][j] == 0 and dp[0][j-1] == 1:
            dp[0][j] = 1
    
    # Fill the first column
    for i in range(1, m):
        if grid[i][0] == 0 and dp[i-1][0] == 1:
            dp[i][0] = 1
    
    # Fill the rest of the dp array
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Example usage
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(f"Number of unique paths (Optimized): {unique_paths_optimized(grid)}")
 

### Explanation

# 1. **Brute Force Approach**:
#    - **Recursion**: Uses a recursive function to explore all possible paths by moving right or down.
#    - **Time Complexity**: `O(2^(m+n))` due to the exponential number of possible paths.
#    - **Space Complexity**: `O(m+n)` for the recursion stack.

# 2. **Optimized Approach**:
#    - **Dynamic Programming**: Uses a 2D array `dp` to store the number of ways to reach each cell. Handles obstacles by setting the corresponding `dp` cell to `0` if an obstacle is present.
#    - **Time Complexity**: `O(m * n)` where `m` is the number of rows and `n` is the number of columns.
#    - **Space Complexity**: `O(m * n)` for the `dp` table.

# The optimized approach is significantly more efficient and feasible for larger grids compared to the brute force method.