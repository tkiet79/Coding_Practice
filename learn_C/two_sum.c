#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// ==========================================
// BÀI 1: Two Sum
// Lưu ý: Trong C, bài này hơi khoai vì trả về mảng động.
// returnSize phải được gán bằng 2.
// ==========================================
// Hàm so sánh cho số nguyên (Tăng dần)

typedef struct 
{
    int value;
    int originalIndex;
} Element;
int compareElements(const void *a, const void *b) {
    return ((Element*)a)->value - ((Element*)b)->value;
}
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // TODO: Viết code ở đây
    // Gợi ý: Brute force O(N^2) là dễ nhất với C thuần.
    // Nếu muốn O(N log N) thì phải sort rồi dùng 2 pointers (nhưng sẽ mất index gốc).
    *returnSize = 2;
    int* result = (int*)malloc(2 * sizeof(int));

    // BƯỚC 1: Tạo mảng struct và copy dữ liệu
    Element* elements = (Element*)malloc(numsSize * sizeof(Element));
    for (int i = 0; i < numsSize; i++) {
        elements[i].value = nums[i];
        elements[i].originalIndex = i; // Lưu lại index "nhà cũ"
    }

    // BƯỚC 2: Sort cái mảng struct này
    qsort(elements, numsSize, sizeof(Element), compareElements);

    int left = 0;
    int right = numsSize - 1;
    
    while (left < right) 
    {
        int sum = elements[left].value + elements[right].value;
        if (sum == target)
        {
            result[0] = elements[left].originalIndex;
            result[1] = elements[right].originalIndex;
            free(elements);
            return result;
        }
        else if (sum < target) 
        {
            left++;
        } 
        else 
        {
            right--;
        }
    }
    free(elements);
    return NULL;
}

