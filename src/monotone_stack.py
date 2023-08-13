# 单调栈 + 贡献法
# sum-of-subarray-minimums
MOD = 10 ** 9 + 7
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n # left[i]  为 <  arr[i] 左侧最近元素下标
        right = [n] * n # right[i] 为 <=   arr[i] 右侧最近元素下标
        st = []
        for i, x in enumerate(arr):
            while st and arr[st[-1]] >= x:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)
        ans = 0
        for i, x in enumerate(arr):
            total = (i - left[i]) * (right[i] - i) 
            ans = (ans + total * x) % MOD
        return ans

MOD = 10 ** 9 + 7
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(-1)
        st = [-1]
        ans = 0
        for r, x in enumerate(arr):
            while len(st) > 1 and arr[st[-1]] >= x:
                i = st.pop()
                ans += arr[i] * (r - i) * (i - st[-1])
            st.append(r)
        return ans % MOD

