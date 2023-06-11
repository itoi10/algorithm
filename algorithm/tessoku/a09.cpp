#include <iostream>
using namespace std;

int H, W, N;
int A[100009], B[100009], C[100009], D[100009];
int X[1509][1509], Z[1509][1509];

int main() {
    cin >> H >> W >> N;
    for(int i = 1; i <= N; i++)
        cin >> A[i] >> B[i] >> C[i] >> D[i];

    // 増減
    for(int i = 1; i <= N; i++) {
        X[A[i]][B[i]] += 1;
        X[A[i]][D[i] + 1] -= 1;
        X[C[i] + 1][B[i]] -= 1;
        X[C[i] + 1][D[i] + 1] += 1;
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

    for(int i = 1; i <= H; i++) {
        for(int j = 1; j <= W; j++) {
            if(j != 1)
                cout << " ";
            cout << Z[i][j];
        }
        cout << endl;
    }

    return 0;
}
