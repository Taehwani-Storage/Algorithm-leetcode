class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0] # 기준이 되는 단어의 앞머리 2글자
        # 두 번째 단어부터 리스트 마지막까지 반복
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0: # 현재 단어 접두사 시작 X
                prefix = prefix[0: len(prefix) - 1] # 접두사 한 글자씩 저장
                # 접두사가 없는 경우
                if prefix == "":
                    return ""
        return prefix
    