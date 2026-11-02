
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 0/1 Knapsack using Dynamic Programming
int knapsack(vector<int>& weights, vector<int>& values,
             int capacity, int n) {

    // Create DP table
    vector<vector<int>> dp(n + 1,
                           vector<int>(capacity + 1, 0));

    // Fill DP table
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {

            if (weights[i - 1] <= w) {
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                );
            }
            else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

int main() {
    int n, capacity;

    cout << "Enter number of items: ";
    cin >> n;

    if (n <= 0) {
        cout << "Invalid input";
        return 0;
    }

    vector<int> weights(n), values(n);

    for (int i = 0; i < n; i++) {
        cout << "Enter weight of item " << i + 1 << ": ";
        cin >> weights[i];

        cout << "Enter value of item " << i + 1 << ": ";
        cin >> values[i];

        if (weights[i] <= 0) {
            cout << "Invalid input";
            return 0;
        }
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    if (capacity < 0) {
        cout << "Invalid input";
        return 0;
    }

    cout << "Maximum value: "
         << knapsack(weights, values, capacity, n);

    return 0;
}
