"""
典型 001 https://atcoder.jp/contests/typical90/tasks/typical90_a
python q1.py < inputs/q1.txt
"""
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def solve(M: int) -> bool:
    """Lを長さM以上のピースに分解できるか判定"""
    # 分割回数
    cnt = 0
    # 前回区切った位置
    pre = 0

    for i in range(N):
        # 区切りの左右がどちらも長さM以上なら分割可能
        if (A[i] - pre >= M) and (L - A[i] >= M):
            cnt += 1
            pre = A[i]

    # K回で分割可能
    if cnt >= K:
        return True
    return False


# 解を二分法で求める
# cf. [二分探索アルゴリズムを一般化 〜 めぐる式二分探索法のススメ 〜](https://qiita.com/drken/items/97e37dd6143e33a64c8c)
left = -1
right = L + 1

while right - left > 1:
    # 中間値
    mid = int(left + (right - left) / 2)
    # 中間値で分割可能?
    if solve(mid):
        # 右に範囲を狭める
        left = mid
    else:
        # 左に範囲を狭める
        right = mid

# 解
print(left)
