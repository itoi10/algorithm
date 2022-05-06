"""
典型 020 https://atcoder.jp/contests/typical90/tasks/typical90_t
"""
# 問題文 log2(a) < b*log2(c)ですか?

# from math import log2
A, B, C = list(map(int, input().split()))

# 浮動小数点で計算すると誤差が出てしまう
# r1 = log2(A)
# r2 = B * log2(C)

# 整数で計算することで誤差を防げる
# log2(a) < b*log2(c)
# log2(a) < log2(c^b)   cf. (対数計算の基本)[https://w3e.kanazawa-it.ac.jp/math/category/sisuu-taisuu/henkan-tex.cgi?target=/math/category/sisuu-taisuu/taisuu-no-keisan.html]
# a < c^b  (底>1のとき)  cf. (大小比較) [https://w3e.kanazawa-it.ac.jp/math/category/other/henkan-tex.cgi?target=/math/category/other/dai-syou-hikaku.html#4]

if A < C ** B:
    print("Yes")
else:
    print("No")
