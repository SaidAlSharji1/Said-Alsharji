def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
            break
    
    return None  

input_string = "hello"
result = first_non_repeating_char(input_string)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")