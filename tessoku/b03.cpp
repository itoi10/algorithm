#include <iostream>
using namespace std;

int main() {
    int N;
    int A[109];
    bool Answer = false;
    const int targetPrice = 1000;

    cin >> N;
    for(int i = 0; i < N; i++)
        cin >> A[i];

    // ３つの異なる商品の合計金額が1000円になる組み合わせがあるかどうかを全探索
    for(int i = 0; i < N - 2; i++) {
        for(int j = i + 1; j < N - 1; j++) {
            for(int k = j + 1; k < N; k++) {
                if(i != j && j != k && k != i) {
                    if(A[i] + A[j] + A[k] == targetPrice) {
                        Answer = true;
                        break;
                    }
                }
            }
        }
    }

    if(Answer == true) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
