def findp(word):
    return word == word[::-1]

def findlp(sentence):
    words = sentence.split()
    longest_palindrome = ""
    
    for word in words:
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                subword = word[i:j]
                if findp(subword) and len(subword) > len(longest_palindrome):
                    longest_palindrome = subword
                    
    return longest_palindrome

sentence = input("Enter your sentence: ")
longest_palindrome = findlp(sentence)
if longest_palindrome:
    print(f"The longest palindrome word is: {longest_palindrome}")
else:
    print("No palindrome word found in the sentence.")