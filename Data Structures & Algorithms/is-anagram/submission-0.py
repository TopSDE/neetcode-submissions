class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}

        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        for ch in t:
            hash_map[ch] = hash_map.get(ch, 0) - 1

        for val in hash_map.values():
            if val != 0:
                return False

        return True