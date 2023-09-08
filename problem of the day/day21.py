def min_jumps_to_end(arr):
    n = len(arr)
    if n <= 1:
        return 0  # No jumps needed for an empty array or an array with only one element

    jumps = 0  # Initialize the number of jumps
    max_reach = arr[0]  # Initialize the maximum reachable index
    steps = arr[0]  # Initialize the number of steps you can take in the current jump

    for i in range(1, n):
        if i == n - 1:
            return jumps + 1  # If you have reached the last element, return the jumps + 1

        max_reach = max(max_reach, i + arr[i])  # Update the maximum reachable index

        steps -= 1  # Decrement the number of steps remaining in the current jump

        if steps == 0:
            jumps += 1  # If you have used all the steps, take a jump
            if i >= max_reach:
                return -1  # If you can't reach the next position, return -1
            steps = max_reach - i  # Calculate the number of steps for the next jump

    return -1  # If you can't reach the end, return -1

# Example usage:
arr = [1,3,5,8,9,2,6,7,6,8,9]
result = min_jumps_to_end(arr)
if result != -1:
    print("Minimum number of jumps to reach the end:", result)
else:
    print("It's not possible to reach the end.")