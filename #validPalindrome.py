'''


Problem 4: Valid Palindrome

Given a string s, return True if it's a palindrome — reading the same forwards and backwards — considering only alphanumeric characters and ignoring case.
Example: s = "A man, a plan, a canal: Panama" → True
Example: s = "race a car" → False

peep


'''

def is_pal(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        

        left += 1
        right -= 1 

def main():
    s= "peep"
    is_pal(s)

print(main())