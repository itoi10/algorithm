#include <iostream>
using namespace std;

int N, Q;
const int HW = 1509;
int MAP[HW][HW], SUM[HW][HW];
int A[100009], B[100009], C[100009], D[100009];

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++) {
        int x, y;
        cin >> x >> y;
        MAP[x][y] += 1;
    }
    cin >> Q;
    for(int i = 1; i <= Q; i++) {
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    }

    // 横の累積和
    for(int i = 1; i < HW; i++) {
        for(int j = 1; j < HW; j++) {
            SUM[i][j] = SUM[i][j - 1] + MAP[i][j];
        }
    }

    // 縦の累積和
    for(int i = 1; i < HW; i++) {
        for(int j = 1; j < HW; j++) {
            SUM[i][j] = SUM[i - 1][j] + SUM[i][j];
        }
    }

    // // MAP表示
    // const int dispSize = 10;
    // for(int i = 1; i < dispSize; i++) {
    //     for(int j = 1; j < dispSize; j++) {
    //         cout << MAP[j][i] << " ";
    //     }
    //     cout << endl;
    // }
    // cout << endl;
    // // SUM表示
    // for(int i = 1; i < dispSize; i++) {
    //     for(int j = 1; j < dispSize; j++) {
    //         cout << SUM[j][i] << " ";
    //     }
    //     cout << endl;
    // }

    for(int i = 1; i <= Q; i++) {
        int all = SUM[C[i]][D[i]];
        int left = SUM[C[i]][B[i] - 1];
        int up = SUM[A[i] - 1][D[i]];
        int upleft = SUM[A[i] - 1][B[i] - 1];
        cout << all - left - up + upleft << endl;
    }
}
