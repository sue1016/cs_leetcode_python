class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        x_reverse = list(reversed(x))
        if x == x_reverse:
            return True
        else:
            return False

