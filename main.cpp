#include <iostream>
#include <bits/stdc++.h>
using namespace std;




void selectionSort(int arr[], int n)
{
    int i, j, min_idx;

    // One by one move boundary of
    // unsorted subarray
    for (i = 0; i < n - 1; i++) {
      ///0 to the last element in array forloop
        // Find the minimum element in
        // unsorted array
        min_idx = i; /// mid is the first element
        for (j = i + 1; j < n; j++) {
                ///second element to the end
            if (arr[j] < arr[min_idx])
            /// if the element on the right is smaller
            ///than the element on the left
                min_idx = j;
           /// then the index on the right becomes the new min index
        }

        // Swap the found minimum element
        // with the first element
        if (min_idx != i) ///min_indx isn't
            swap(arr[min_idx], arr[i]);
    }
}

// Function to print an array
void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++) {
        cout << arr[i] << " ";
        cout << endl;
    }
}

// Driver program
int main()
{
    int arr[] = { 64, 25, 12, 22, 11 };
    int n = sizeof(arr) / sizeof(arr[0]);

    // Function Call
    selectionSort(arr, n);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}
