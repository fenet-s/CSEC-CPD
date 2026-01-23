class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1arr = [0] * 26
        for ch in s1:
            s1arr[ord(ch) - ord('a')] += 1

        for i in range(len(s2) - len(s1) + 1):
            s2arr = [0] * 26

            for j in range(len(s1)):
                s2arr[ord(s2[i + j]) - ord('a')] += 1

            if self.matches(s1arr, s2arr):
                return True

        return False

    def matches(self, s1arr, s2arr) -> bool:
        for i in range(26):
            if s1arr[i] != s2arr[i]:
                return False
        return True
