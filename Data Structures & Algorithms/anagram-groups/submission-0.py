class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            hash_map[sortedS].append(s)

        return list(hash_map.values())

    