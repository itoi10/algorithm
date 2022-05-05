"""
典型 027 https://atcoder.jp/contests/typical90/tasks/typical90_aa
"""

from sys import stdin
input = stdin.readline

N = int(input())
S = [input().rstrip("\n") for _ in range(N)]


# if a in b の計算量はO(n)なので全体でO(N^2)の計算量となりN<=10e5だとTLEになる
# cf. (Pythonistaなら知らないと恥ずかしい計算量のはなし)[https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb]

# registered = []
# for i in range(N):
#     if S[i] not in registered:
#        registered.append(S[i])
#        print(i+1) 


# 辞書を使えば要素の参照が高速に行える
name_dict = {}
for i in range(N):
    if not name_dict.get(S[i]):
        name_dict[S[i]] = 1
        print(i+1)
