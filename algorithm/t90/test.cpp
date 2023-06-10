#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for(int i = 0; (i) < (int)(n); ++(i))

bool m[256];

int findIdx(int n, int l) {
    int cnt = 0;
    REP(i, n) {
        if(m[i] == true) {
            cnt += 1;
            if(cnt == l)
                return i;
        }
    }
    return -1;
}

int main() {
    int N, K, Q, A, L;
    cin >> N >> K >> Q;
    REP(i, K) {
        cin >> A;
        m[A - 1] = 1;
    }
    REP(i, Q) {
        cin >> L;
        int idx = findIdx(N, L);
        if(idx != N - 1 && m[idx + 1] == false) {
            m[idx] = false;
            m[idx + 1] = true;
        }
    }

    bool fst = true;
    REP(i, N) {
        if(m[i] == true) {
            if(fst) {
                cout << i + 1;
                fst = false;
            } else {
                cout << ' ' << i + 1;
            }
        }
    }
    cout << endl;
}
