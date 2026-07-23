class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        n = len(arr)
        hash_map = {ele for ele in arr}
        st = set()

        cnt = 0
        for i in range(n):
            curr_ele = arr[i]
            curr_cnt = 1

            if curr_ele not in st and (curr_ele-1) not in hash_map:
                st.add(curr_ele)

                while (curr_ele+1) in hash_map:
                    curr_cnt += 1
                    curr_ele += 1
                
            cnt = max(cnt, curr_cnt)

        return cnt