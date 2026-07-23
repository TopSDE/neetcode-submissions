class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        n = len(arr)
        hash_set = set()

        cnt = 0
        for i in range(n):
            curr_ele = arr[i]
            curr_cnt = 1

            if (curr_ele-1) not in hash_set:

                while (curr_ele+1) in arr:
                    curr_cnt += 1
                    curr_ele += 1
                    hash_set.add(curr_ele)
                
            cnt = max(cnt, curr_cnt)

        return cnt