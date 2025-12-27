def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Sau mỗi vòng lặp, phần tử lớn nhất sẽ "nổi" xuống cuối
        # nên ta trừ đi i để không phải kiểm tra lại
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                # Hoán đổi vị trí (Swap) cực nhanh trong Python
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr