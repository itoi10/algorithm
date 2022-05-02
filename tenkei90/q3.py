"""
典型 003 https://atcoder.jp/contests/typical90/tasks/typical90_c
"""
# 木に存在する2つノード間の最大距離を木の直径と言う
# DFS(深さ優先探索) or BFS(幅優先探索)を2回行い直径の端点を求めれば良い
# cf. (木の直径を求めるアルゴリズム)[https://algo-logic.info/tree-diameter/]


from typing import List, Tuple
from collections import deque
# pop操作計算量  list O(n), deque O(1)
# cf. (Python: deque vs. list)[https://dev.to/v_it_aly/python-deque-vs-listwh-25i9]


def bfs(tree: List[List[int]], start: int) -> Tuple[int, int]:
    """ 幅優先探索を行い,最も深い点の番号と深さを返す　"""

    # キューに探索開始点追加
    que = deque()
    que.append(start)

    # 各点の深さ
    dist = [-1] * len(tree)
    dist[start] = 0

    # 最も深い点の番号
    deepest_idx = 0

    while que:
        # キューから点取得
        pos = que.popleft()
        # 接続点を順番にチェック
        for to in tree[pos]:
            
            # 未訪問の点?
            if dist[to] == -1:
                # 深さを設定してキューに追加
                dist[to] = dist[pos] + 1
                que.append(to)

                # 最も深い点更新
                if dist[to] > dist[deepest_idx]:
                    deepest_idx = to

    # 最も深い点の番号, 深さ
    return deepest_idx, dist[deepest_idx]

if __name__ == "__main__":
    N = int(input())

    # n番目の要素に点nから接続している点のリストを格納
    TREE: List[List[int]] = [[] for _ in range(N)]
    for _ in range(N-1):
        A, B = map(lambda x: x-1, map(int, input().split()))
        TREE[A].append(B) # 点Aiの接続リストにBi追加
        TREE[B].append(A) # 点Biの接続リストにAi追加
    
    # BFS 1回目. とりあえず0番目から開始
    idx, _ = bfs(TREE, 0)

    # BSF 2回目. 1回目で取得した点から開始すれば木の直径が求められる
    _, val = bfs(TREE, idx)
    
    rslt = val + 1
    print(rslt)
