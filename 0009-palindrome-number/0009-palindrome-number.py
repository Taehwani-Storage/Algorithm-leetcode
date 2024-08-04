class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # 음수는 NO palindrome
            return False
        # 정수를 문자열로 변형 후 비교
        x_str = str(x)
        if x_str == x_str[: : -1]:
            return True