"""
典型 033 https://atcoder.jp/contests/typical90/tasks/typical90_ag
"""

H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
else:
    # 2つ置きに配置していった数
    print(((H + 1) // 2) * ((W + 1) // 2))
