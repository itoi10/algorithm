"""
典型 016 https://atcoder.jp/contests/typical90/tasks/typical90_p
"""
# 全検索を行うがなるべく不要な計算を避ける
# それでもPythonでは遅そうなのでnumbaを使ってみる

from numba import njit
from sys import stdin
input = stdin.readline

@njit(cache=True)
def main(N: int, A:int, B:int, C:int):
    MAX_COIN = 9999

    rslt = MAX_COIN
    for i in range(MAX_COIN+1):
        # この時点でNを超えていたら計算終了
        s1 = A * i
        if s1 > N:
            break
        for j in range(MAX_COIN+1):
            s2 = s1 + B * j
            # j計算終了
            if s2 > N:
                break
            # Cの枚数は計算で求まる
            if (N - s2) % C == 0:
                k = (N - s2) // C
                # 最も小さい値が答え
                rslt = min(i+j+k, rslt)
    print(rslt)

if __name__ == "__main__":
    N = int(input())
    A, B, C = list(map(int, input().split()))

    main(N, A, B, C)