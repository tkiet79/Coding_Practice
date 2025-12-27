arr = [1, 2, 0, 4, 3, 0, 5, 0]
n = len(arr)
pos = 0 

for i in range(n):
    if arr[i] != 0:
        # Nếu gặp số khác 0, ta đưa nó về vị trí pos
        # Bằng cách hoán đổi arr[i] và arr[pos]
        arr[pos], arr[i] = arr[i], arr[pos]
        
        # Sau khi đặt xong, ta nhích pos lên để chờ số khác 0 tiếp theo
        pos += 1

print(arr)