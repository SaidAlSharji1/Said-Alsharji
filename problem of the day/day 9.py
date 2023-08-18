def find_substrings_with_equal_case(s):
    substrings = []
    n = len(s)

    for i in range(n):
        lower_count = 0
        upper_count = 0

        for j in range(i, n):
            if s[j].islower():
                lower_count += 1
            else:
                upper_count += 1

            if lower_count == upper_count:
                substrings.append(s[i:j + 1])
    print("The number of the substring is : ",len(substrings))
    return substrings

# Test the function
word = "WomensDAY"
substrings = find_substrings_with_equal_case(word)
print("Substrings with equal lowercase and uppercase letters:", substrings)

