# 快速幂
def myPow(x: float, n: int) -> float:
    def quickMul(N):
        ans = 1.0
        y = x
        while N > 0:
            if N % 2 == 1:
                ans *= y
            y *= y
            N //= 2
        return ans
    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
            
# 带 MOD 的快速幂
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
