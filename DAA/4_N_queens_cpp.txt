
#include <iostream>
#include <vector>
using namespace std;

int N;

// Check whether a queen can be placed safely
bool isSafe(vector<vector<int>>& board, int row, int col) {

    // Check left side of the row
    for (int j = 0; j < col; j++) {
        if (board[row][j])
            return false;
    }

    // Check upper-left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j])
            return false;
    }

    // Check lower-left diagonal
    for (int i = row, j = col; i < N && j >= 0; i++, j--) {
        if (board[i][j])
            return false;
    }

    return true;
}

// Solve N-Queens using Backtracking
bool solveNQueens(vector<vector<int>>& board, int col) {

    // All queens placed
    if (col >= N)
        return true;

    // Try each row in current column
    for (int i = 0; i < N; i++) {

        if (isSafe(board, i, col)) {

            board[i][col] = 1;

            if (solveNQueens(board, col + 1))
                return true;

            // Backtrack
            board[i][col] = 0;
        }
    }

    return false;
}

int main() {
    cout << "Enter number of queens: ";
    cin >> N;

    if (N < 1) {
        cout << "Invalid input";
        return 0;
    }

    vector<vector<int>> board(N, vector<int>(N, 0));

    // Place first queen in first row and first column
    board[0][0] = 1;

    if (solveNQueens(board, 1)) {

        cout << "\nSolution:\n";

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                cout << board[i][j] << " ";
            cout << endl;
        }
    }
    else {
        cout << "No solution exists";
    }

    return 0;
}
