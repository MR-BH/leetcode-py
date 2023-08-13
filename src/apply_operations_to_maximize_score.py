# 7023
# 这道题涵盖了 快速幂、质因数分解、乘法原理、单调栈 + 贡献法 等知识点
# 属于不可多得的优秀练习题、面试题

MOD = 10 ** 9 + 7
# 预处理质数分数
MX = 10 ** 5 + 1
omega = [0] * MX
for i in range(2, MX):
    if omega[i] == 0: # omega[i] = 0 代表 i 为质数
        for j in range(i, MX, i):
            omega[j] += 1 # i 是 j 的一个质因子

def myPow(x: int, n: int, mod: int) -> float:
    def quickMul(N):
        ans = 1
        y = x
        while N > 0:
            if N % 2 == 1:
                ans = ans * y % mod
            y = y * y % mod
            N //= 2
        return ans
    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
    
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n # 质数分数 >= omega[nums[i]] 的左侧最近元素的下标
        right = [n] * n # 质数分数 >  omega[nums[i]] 的右侧最近元素的下标
        st = []         # 单调栈 (递减) 
        for i, x in enumerate(nums):
            while st and omega[nums[st[-1]]] < omega[x]:
                right[st.pop()] = i
            if st: left[i] = st[-1]
            st.append(i)
        
        ans = 1
        for i, x, l, r in sorted(zip(range(n), nums, left, right), key=lambda z: -z[1]):
            total = (i - l) * (r - i)
            if total >= k:
                ans = ans * myPow(x, k, MOD) % MOD
                break 
            ans = ans * myPow(x, total, MOD) % MOD
            k -= total

        return ans     

