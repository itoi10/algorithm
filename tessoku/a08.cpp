#include <iostream>
using namespace std;

int H, W, Q;
int X[1509][1509], Z[1509][1509];
int A[100009], B[100009], C[100009], D[100009];

int main() {
    cin >> H >> W;
    for(int i = 1; i <= H; i++) {
        for(int j = 1; j <= W; j++) {
            cin >> X[i][j];
        }
    }
    cin >> Q;
    for(int i = 1; i <= Q; i++) {
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    }

    // Z初期化
    for(int i = 1; i <= H; i++) {
        for(int j = 1; j <= W; j++) {
            Z[i][j] = 0;
        }
    }

    // 横の累積和
    for(int i = 1; i <= H; i++) {
        for(int j = 1; j <= W; j++) {
            Z[i][j] = Z[i][j - 1] + X[i][j];
        }
    }

    // 縦の累積和
    for(int i = 1; i <= H; i++) {
        for(int j = 1; j <= W; j++) {
            Z[i][j] = Z[i - 1][j] + Z[i][j];
        }
    }

    for(int i = 1; i <= Q; i++) {
        int all = Z[C[i]][D[i]];
        int left = Z[C[i]][B[i] - 1];
        int up = Z[A[i] - 1][D[i]];
        int upleft = Z[A[i] - 1][B[i] - 1];
        cout << all - left - up + upleft << endl;
    }
}
