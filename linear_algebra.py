"""numpy plt"""

import numpy as np
import matplotlib.pyplot as plt


def f1():
    # ベクトル定義
    v1 = np.array([10, 20, 30])
    v2 = np.array([5, 10, 15])

    print(f"{v1 = }")
    print(f"{v2 = }")

    # 演算
    print(f"{v1 + v2 = }")
    print(f"{v1 - v2 = }")
    print(f"{v1 * v2 = }")
    print(f"{v1 / v2 = }")

    k = 3
    print(f"{k = }")
    print(f"{k * v1 = }")

    # 内積
    print(f"{np.dot(v1, v2) = }")


def f2():
    # 描画領域全体
    fig = plt.figure(figsize=(5, 5), facecolor="lightgray")
    # 1つのプロット領域
    ax = fig.add_subplot()

    # 格子
    ax.grid()
    # 軸ラベル
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    # 範囲
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    # x,y軸
    ax.axhline(0)
    ax.axvline(0)

    # 二次元ベクトル
    v1 = np.array([10, 20])
    v2 = np.array([5, -10])
    # ベクトル描画
    ax.quiver(0, 0, v1[0], v1[1], angles="xy", scale_units="xy", scale=1, color="red")
    ax.quiver(v1[0], v1[1], v2[0], v2[1], angles="xy", scale_units="xy", scale=1, color="blue")
    plt.title(f"{v1} + {v2} = {v1+v2}")

    plt.show()


def sin_wave():
    # 正弦波
    x = np.linspace(0, 2 * np.pi)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    # f1()
    f2()
