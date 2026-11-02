
#include <iostream>
using namespace std;

// Recursive Fibonacci
long long recursiveFib(int n) {
    if (n <= 1)
        return n;

    return recursiveFib(n - 1) + recursiveFib(n - 2);
}

// Non-recursive Fibonacci
long long iterativeFib(int n) {
    if (n <= 1)
        return n;

    long long a = 0, b = 1, c;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return b;
}

int main() {
    int n;

    cout << "Enter the number of terms: ";
    cin >> n;

    if (n < 0) {
        cout << "Invalid input";
        return 0;
    }

    cout << "Fibonacci using Recursion: ";
    for (int i = 0; i < n; i++)
        cout << recursiveFib(i) << " ";

    cout << "\nFibonacci using Iteration: ";
    for (int i = 0; i < n; i++)
        cout << iterativeFib(i) << " ";

    return 0;
}
