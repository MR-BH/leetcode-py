# 质数的各种筛法 以及 质因数分解

# 204 count-primes
# 欧拉筛
MX = 5 * 10 ** 6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def countPrimes(self, n: int) -> int:
        return bisect_left(primes, n)

# 线性筛
MX = 5 * 10 ** 6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
    for p in primes:
        if i * p >= MX:
            break
        is_prime[i * p] = False
        if i % p == 0:
            break


class Solution:
    def countPrimes(self, n: int) -> int:
        return bisect_left(primes, n)
    