class Solution:
    def romanToInt(self, s: str) -> int:
        map_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        answer = 0
        for i in range(len(s)):
            if i < len(s) - 1 and map_roman[s[i]] < map_roman[s[i + 1]]:
                answer -= map_roman[s[i]]
            else:
                answer += map_roman[s[i]]
        return answer
