"""
典型 026 https://atcoder.jp/contests/typical90/tasks/typical90_z
"""


import sys
from sys import stdin

input = stdin.readline

sys.setrecursionlimit(10**6)
# 再起回数が1000を超えるとランタイムエラーとなるので上限変更
# また再起処理を使う場合はPyPyよりPythonの方が速い
# cf. (AtCoderでPythonが再帰に弱い問題をどうにかしたい)[https://aotamasaki.hatenablog.com/entry/cython_recursion]

N = int(input())
graph = [[] for _ in range(N)]
dist = [None] * N

# 隣接リスト作成
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 深さ優先探索により各点をTrue or Falseに塗り分け
def dfs(idx, bool):
    dist[idx] = bool
    for i in graph[idx]:
        # 未探索？
        if dist[i] == None:
            # 次の点に反対の色を設定して探索
            dfs(i, not bool)


# 色分け
dfs(0, 0)

# 塗り分けたうちTrueかFalse多い方を選択
half_N = N // 2
bool = False
if dist.count(True) >= half_N:
    bool = True

# N/2個頂点を出力
cnt = 0
for i in range(N):
    if dist[i] == bool:
        print(i + 1)
        cnt += 1
    if cnt == half_N:
        break
