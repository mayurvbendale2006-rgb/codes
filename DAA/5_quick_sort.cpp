
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

// Partition function
int partition(vector<int>& a, int low, int high) {
    int pivot = a[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }

    swap(a[i + 1], a[high]);
    return i + 1;
}

// Deterministic Quicksort
void deterministicQuickSort(vector<int>& a, int low, int high) {
    if (low < high) {
        int p = partition(a, low, high);

        deterministicQuickSort(a, low, p - 1);
        deterministicQuickSort(a, p + 1, high);
    }
}

// Randomized Quicksort
int randomizedPartition(vector<int>& a, int low, int high) {
    int randomIndex = low + rand() % (high - low + 1);

    swap(a[randomIndex], a[high]);

    return partition(a, low, high);
}

void randomizedQuickSort(vector<int>& a, int low, int high) {
    if (low < high) {
        int p = randomizedPartition(a, low, high);

        randomizedQuickSort(a, low, p - 1);
        randomizedQuickSort(a, p + 1, high);
    }
}

// Display array
void display(vector<int>& a) {
    for (int x : a)
        cout << x << " ";
    cout << endl;
}

int main() {
    int n;

    cout << "Enter number of elements: ";
    cin >> n;

    if (n <= 0) {
        cout << "Invalid input";
        return 0;
    }

    vector<int> a(n), b;

    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++)
        cin >> a[i];

    b = a;

    deterministicQuickSort(a, 0, n - 1);

    srand(time(0));
    randomizedQuickSort(b, 0, n - 1);

    cout << "\nDeterministic Quicksort: ";
    display(a);

    cout << "Randomized Quicksort: ";
    display(b);

    return 0;
}
