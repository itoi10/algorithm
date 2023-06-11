#include <iostream>
using namespace std;

int N;
const int SIZE = 1500;
int A[100009], B[100009], C[100009], D[100009];
int Z[SIZE + 9][SIZE + 9];

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++)
        cin >> A[i] >> B[i] >> C[i] >> D[i];

    // 増減
    for(int i = 1; i <= N; i++) {
        Z[A[i]][B[i]] += 1;
        Z[A[i]][D[i]] -= 1;
        Z[C[i]][B[i]] -= 1;
        Z[C[i]][D[i]] += 1;
    }

    // 横の累積和
    for(int i = 0; i <= SIZE; i++) {
        for(int j = 1; j <= SIZE; j++) {
            Z[i][j] = Z[i][j - 1] + Z[i][j];
        }
    }

    // 縦の累積和
    for(int i = 1; i <= SIZE; i++) {
        for(int j = 0; j <= SIZE; j++) {
            Z[i][j] = Z[i - 1][j] + Z[i][j];
        }
    }

    int ans = 0;
    for(int i = 0; i <= SIZE; i++) {
        for(int j = 0; j <= SIZE; j++) {
            if(Z[i][j] >= 1)
                ans += 1;
        }
    }

    cout << ans << endl;

    return 0;
}
