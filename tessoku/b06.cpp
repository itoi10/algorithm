#include <iostream>
using namespace std;

int N, A[100009], win[100009], lose[100009];
int Q, L[100009], R[100009];

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++)
        cin >> A[i];
    cin >> Q;
    for(int i = 1; i <= Q; i++)
        cin >> L[i] >> R[i];

    // 累積和
    win[0] = 0;
    lose[0] = 0;
    for(int i = 1; i <= N; i++) {
        win[i] = win[i - 1];
        lose[i] = lose[i - 1];
        if(A[i] == 1)
            win[i] += 1;
        else
            lose[i] += 1;
    }

    for(int i = 1; i <= Q; i++) {
        int w = win[R[i]] - win[L[i] - 1];
        int l = lose[R[i]] - lose[L[i] - 1];
        if(w > l)
            cout << "win" << endl;
        else if(w < l)
            cout << "lose" << endl;
        else
            cout << "draw" << endl;
    }
}
