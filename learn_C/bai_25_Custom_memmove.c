#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ==========================================
// BÀI 25: Custom memmove (Level 2+)
// ==========================================
// Yêu cầu: Copy `n` bytes từ địa chỉ `src` sang `dest`.
// 
// THÁCH THỨC:
// - Vùng nhớ `src` và `dest` có thể BỊ CHỒNG LÊN NHAU (Overlapping).
// - Nếu dest > src: Copy từ đuôi về đầu để tránh ghi đè dữ liệu chưa copy.
// - Nếu dest < src: Copy từ đầu về đuôi.
// - Đây là cách hoạt động thực sự của hàm chuẩn `memmove`.
void *my_memmove(void *dest, const void *src, size_t n) {
    char *d = (char *)dest;
    const char *s = (const char *)src;
    if (d == s) return;
    if (d < s) 
    {
        for (size_t i = 0; i < n ; i++) 
        {
            d[i] = s[i];
        }
            
    }
    if (d > s)
    {
        for (size_t i = n; i > 0; i--)
        {
            d[i-1] = s[i-1];
        }
    }
    return dest;
}