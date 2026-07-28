class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1

        while l < r:
            if not s[l].isalnum():
                l += 1
            
            if not s[r].isalnum():
                r -= 1
            
            if s[l].isalnum() and s[r].isalnum():
                if s[l].isdigit() and s[r].isdigit():
                    if s[l] == s[r]:
                        l += 1
                        r -= 1

                    else:
                        return False

                else:
                    if s[l].lower() == s[r].lower():
                        l += 1
                        r -= 1

                    else:
                        return False

        return True