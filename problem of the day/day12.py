def alternate_positive_negative(arr):
    positive_nums = [num for num in arr if num >= 0]
    negative_nums = [num for num in arr if num < 0]
    print(positive_nums)
    print(negative_nums)
    alternating_arr = []
    num_pos = len(positive_nums)
    num_neg = len(negative_nums)
    
    min_len = min(num_pos, num_neg)
    

        
    
    for i  in range(num_pos):
        for j in negative_nums:
            if positive_nums[i] >= 0:
                positive_nums.insert(i+1,j)
                i+=2
                

    
    return positive_nums

input_arr = [9, 4 ,-2, -1, 5, 0,-5,-3,2]
alternating_result = alternate_positive_negative(input_arr)
print(alternating_result)