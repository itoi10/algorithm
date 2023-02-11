#include <cstdio>

// 配列表示
void trace(int A[], int N) {
    for(int i = 0; i < N; i++) {
        if(i > 0) {
            printf(" ");
        }
        printf("%d", A[i]);
    }
    printf("\n");
}

// 挿入ソート
void insertionSort(int A[], int N) {

    for(int i = 1; i < N; i++) {

        // 未ソート部分の先頭を取り出す
        int v = A[i];

        int j = i - 1;

        // vより大きい要素を右にずらす
        while(j >= 0 && A[j] > v) {
            A[j + 1] = A[j];
            j -= 1;
        }

        A[j + 1] = v;

        // ソートされていく過程を表示
        trace(A, N);
    }
}

int main() {
    int N, i, j;
    int A[100];

    // input
    scanf("%d", &N);
    for(i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    // 表示
    trace(A, N);
    // 挿入ソート
    insertionSort(A, N);

    return 0;
}
