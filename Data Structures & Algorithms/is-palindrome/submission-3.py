class Solution:
    def isPalindrome(self, s: str) -> bool:

        ct = "".join(char for char in s if char.isalnum()).lower()
        
        reversed_ct = ct[::-1]

        print(reversed_ct)

        if ct == reversed_ct:
            return True
        else: 
            return False
        