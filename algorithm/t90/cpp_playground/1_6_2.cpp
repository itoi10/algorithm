#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
    // input
    int L = 10;
    int n = 3;
    int x[] = {2, 6, 7};

    // 最小時間
    int minTime = 0;
    for(int i = 0; i < n; i++) {
        //                     端からの距離の小さい方
        minTime = max(minTime, min(x[i], L - x[i]));
    }

    // 最大時間
    int maxTime = 0;
    for(int i = 0; i < n; i++) {
        //                     端からの距離の大きい方
        maxTime = max(maxTime, max(x[i], L - x[i]));
    }

    printf("min:%d max:%d\n", minTime, maxTime);
}
