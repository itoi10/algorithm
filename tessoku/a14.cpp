#include <algorithm>
#include <iostream>
using namespace std;

int N, K, A[1009], B[1009], C[1009], D[1009];
int AB[1000009], CD[1000009];

int main() {
    cin >> N >> K;

    int *arrs[] = {A, B, C, D};
    for(int i = 0; i < 4; i++) {
        for(int j = 1; j <= N; j++) {
            cin >> arrs[i][j];
        }
    }

    /* 半分全列挙 */
    // A + B の全列挙 O(N^2)
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            AB[(i - 1) * N + j] = A[i] + B[j];
        }
    }

    // C + D の全列挙 O(N^2)
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            CD[(i - 1) * N + j] = C[i] + D[j];
        }
    }
    sort(CD + 1, CD + (N * N) + 1);

    // 二分探索 O(N^2*logN)
    for(int i = 1; i <= N * N; i++) {
        // CDの中にK - AB[i]があるかどうか lower_bound(start, end, target)
        int pos = lower_bound(CD + 1, CD + (N * N) + 1, K - AB[i]) - CD;
        if(pos <= N * N && CD[pos] == K - AB[i]) {
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;
    return 0;
}
