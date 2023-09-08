class Solution:
    def trap(self, height):
        result = 0
        start = 0
        end = len(height) - 1
        while start < end:
            if height[start] <= height[end]:
                current = height[start]
                while height[start + 1] < current:
                    result += current - height[start + 1]
                    start += 1
                start += 1
            else:
                current = height[end]
                while height[end - 1] < current:
                    result += current - height[end - 1]
                    end -= 1
                end -= 1
        return result
    
# Create an instance of the Solution class
solution = Solution()

# Input data: an array representing the heights of walls
heights = [0,1,0,2,1,0,1,3,2,1,2,1]

# Call the trap function to calculate the trapped water
trapped_water = solution.trap(heights)

# Print the result
print("Trapped water:", trapped_water)
