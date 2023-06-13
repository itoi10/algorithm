#include <iostream>
using namespace std;

int N, X, A[100009];

// 二分探索 O(logN)
int search(int x) {
    int L = 1, R = N;
    while(L <= R) {
        int M = (L + R) / 2;
        if(A[M] == x) {
            return M;
        } else if(A[M] < x) {
            L = M + 1;
        } else {
            R = M - 1;
        }
    }
}

int search2(int x) {
    // lower_bound: 標準ライブラリ, Pythonだとbisectが使える
    int pos = lower_bound(A + 1, A + N + 1, x) - A;
    if(pos <= N && A[pos] == x) {
        return pos;
    } else {
        return -1;
    }
}

int main() {
    cin >> N >> X;
    for(int i = 1; i <= N; i++)
        cin >> A[i];

    int ans = search(X);

    cout << ans << endl;
    return 0;
}
