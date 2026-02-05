#include <stdio.h>
#include <stdlib.h>

int binary_search(int* nums, int size, int target) {
    if (nums == NULL || size == 0) return -1;

    int left = 0;
    int right = size - 1;

    // TODO: Viết vòng lặp while.
    // Lưu ý cách tính mid để tránh tràn số (Integer Overflow) nếu left + right quá lớn.
    // mid = left + (right - left) / 2;
    while (left <= right)
    {
        long mid = left + (right - left) / 2;
        if (nums[mid] < target)
        {
            left = mid + 1;
        }

        else if (nums[mid] > target)
        {
            right = mid - 1;
        }

        else{
            return mid;
        }
    }
    
    return -1;
}

int main(void)
{
    printf("--- BAT DAU TEST ---\n");

    // Test 1: Binary Search
    int t1[] = {-1, 0, 3, 5, 9, 12};
    if (binary_search(t1, 6, 9) == 4) printf("[PASS] Bai 1: Found\n");
    else printf("[FAIL] Bai 1: Expected 4, got %d\n", binary_search(t1, 6, 9));

    if (binary_search(t1, 6, 2) == -1) printf("[PASS] Bai 1: Not Found\n");
    else printf("[FAIL] Bai 1: Expected -1, got %d\n", binary_search(t1, 6, 2));
    return 0;
}