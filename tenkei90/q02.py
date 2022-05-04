"""
典型 002 https://atcoder.jp/contests/typical90/tasks/typical90_b
"""

# cf. [Python de アルゴリズム（bit全探索）] (https://qiita.com/gogotealove/items/11f9e83218926211083a)
# N = 20くらいならbit全検索で間に合う
# 2^20 = 1048576 ≒ 10e6 (1sあたり10e7くらいがpythonの目安
N = int(input())
results = []

# 全パターン探索
# 例えば ((())) なら 2進数で 111000 とし, 000000 ~ 111111 を全探索
for bit in range(2 ** N):
    cnt = 0
    rslt = ""

    # 正しいカッコ列の判定条件
    #  1.左から探索したとき ( は常に ) の以上の数
    #  2.N個探索し終わったあとに ( と ) が同じ数

    # 左からカッコ列を探索
    for i in range(N):
        # シフトしていき ( か )か判定
        if (bit >> i) & 1:
            rslt += "("
            cnt += 1
        else:
            rslt += ")"
            cnt -= 1
            # 条件1に合わないので終了
            if cnt < 0:
                break
    # OK
    if cnt == 0:
        results.append(rslt)

if len(results) > 0:
    results.sort()
    print("\n".join(results))
