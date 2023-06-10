#include <cstdio>
#include <queue>
#include <stack>
using namespace std;

const int MAX_N = 1000;

/*
再帰関数(基本)
*/

// 階乗を求める関数
int fact(int n) {
    if(n == 0) {
        return 1;
    }
    return n * fact(n - 1);
}

// フィボナッチ数列(メモ化なし)
int fib(int n) {
    if(n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

// フィボナッチ数列(メモ化あり)
int memo[MAX_N];
int fib_with_memo(int n) {
    if(n <= 1) {
        return n;
    }
    if(memo[n] != 0) {
        return memo[n];
    }
    memo[n] = fib_with_memo(n - 1) + fib_with_memo(n - 2);
    return memo[n];
}

/*
スタック・キュー（基本）
*/

void stack_test() {
    stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);

    printf("%d\n", s.top());
    s.pop();
    printf("%d\n", s.top());
    s.pop();
    printf("%d\n", s.top());
    s.pop();
}

void queue_test() {
    queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);

    printf("%d\n", q.front());
    q.pop();
    printf("%d\n", q.front());
    q.pop();
    printf("%d\n", q.front());
    q.pop();
}

int main() {
    queue_test();
    return 0;
}
