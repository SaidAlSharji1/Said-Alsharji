def find_leader_numbers(nums):
    n = len(nums)
    max_right = nums[n - 1]
    leaders = [max_right]

    for i in range(n - 2, -1, -1):
        
        print(nums[i])
        if nums[i] >= max_right:
            leaders.append(nums[i])
            max_right = nums[i]

    leaders.reverse()
    return leaders

# Example usage
input_list = [16, 17, 4, 3, 5, 2]
leader_numbers = find_leader_numbers(input_list)
print("Leader numbers:", leader_numbers)