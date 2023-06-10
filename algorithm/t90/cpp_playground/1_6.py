def solve():
    n = 5
    a = [2, 3, 4, 5, 10]

    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # 辺の長さ
                len = a[i] + a[j] + a[k]
                # 一番長い辺の長さ
                ma = max(a[i], max(a[j], a[k]))
                # 他の辺の長さの和
                rest = len - ma

                # 三角形が作れる条件を満たしている
                if ma < rest:
                    # より長ければ更新
                    ans = max(ans, len)

    print(ans)


if __name__ == "__main__":
    solve()
