def find_distinct_sums(nums):
    distinct_sums = []
    n = len(nums)
    
    for i in range(1 << n):
        subset_sum = 0
        subset = []
        
        for j in range(n):
            if i & (1 << j):
                subset_sum += nums[j]
                subset.append(nums[j])
        
        if subset_sum not in distinct_sums:
            distinct_sums.append(subset_sum)
            print(f"Subset {subset} has sum: {subset_sum}")
    
    return distinct_sums

nums = [1, 2]
distinct_sums = find_distinct_sums(nums)
print("Distinct sums:", distinct_sums)