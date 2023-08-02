# 线段树 以及 Lazy 线段树
class SegmentTree:
   def __init__(self, nums: int):
      n = len(nums)
      self.nums = nums 
      self.min = [0] * (4 * n)
      self.sum = [0] * (4 * n)
      self.lazy = [0] * (4 * n)
      self.n = n
      self.build(1, 1, n)

   def maintain(self, o: int):
      self.min[o] = self.min[2 * o] if self.min[2 * o] < self.min[2 * o + 1] else self.min[2 * o + 1]
      self.sum[o] = self.sum[2 * o] + self.sum[2 * o + 1]

   def do(self, o: int, l: int, r: int, val: int):
      self.lazy[o] += val
      self.sum[o] += (r - l + 1) * val
      self.min[0] += val
   
   def build(self, o: int, l: int, r: int):
      if l == r:
         self.min[o] = self.nums[l]
         self.sum[o] = self.nums[l]
         return
      m = (l + r) // 2
      self.build(2 * o, l, m)
      self.build(2 * o + 1, m + 1, r)
      self.maintain(o)

   # lazy update, 常用于区间更新
   def update(self, o: int, l: int, r: int, L: int, R: int, val):
      if L <= l and r <= R:
         self.do(o, l, r, val)
         return
      m = (l + r) // 2
      if self.lazy[o]:
         self.do(o * 2, l, m, self.lazy[o])
         self.do(o * 2 + 1, m + 1, r, self.lazy[o])
         self.lazy[o] = 0
      if L <= m:
         self.update(o * 2, l, m, L, R, val)
      if m < R:
         self.update(o * 2 + 1, m + 1, r, L, R, val)
      self.maintain(o)
      
   def query(self, o: int, l: int, r: int, L: int, R: int):
      if L <= l and r <= R:
         return (self.min[o], self.sum[o])
      m = (l + r) // 2
      mn, s = inf, 0
      if L <= m:
         x, y = self.query(2 * o, l, m, L, R)
         mn = x if x < mn else mn
         s += y
      if m < R:
         x, y = self.query(2 * o + 1, m + 1, r, L, R)
         mn = x if x < mn else mn
         s += y
      return (mn, s)
