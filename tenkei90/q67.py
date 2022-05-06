"""
典型 067 https://atcoder.jp/contests/typical90/tasks/typical90_bo
"""

import numpy as np

N, K = map(int, input().split())

num = N
for _ in range(K):
    num = int(str(np.base_repr(int(str(num), base=8), base=9)).replace("8", "5"))

print(num)
