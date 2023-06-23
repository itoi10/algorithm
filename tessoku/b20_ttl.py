# 編集距離
# XXX これはTTLになる
import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


# lru_cacheは関数の結果をキャッシュするデコレータ
@lru_cache(maxsize=8192)
def ld(s, t):

    # どちらかが空文字列になったら、残りの文字列の分だけコストがかかる
    if not s:
        return len(t)
    if not t:
        return len(s)

    # 両方の先頭の文字が同じならコストはかからない
    # 2文字目以降のコストを求める
    if s[0] == t[0]:
        return ld(s[1:], t[1:])

    # Sの先頭削除
    l1 = ld(s, t[1:])

    # Tの先頭削除
    l2 = ld(s[1:], t)

    # SとTの先頭を置換
    l3 = ld(s[1:], t[1:])

    # 今行った操作コスト + 残りの文字列コストで最小のものを返す
    return 1 + min(l1, l2, l3)


S = input()
T = input()
print(ld(S, T))
