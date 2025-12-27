#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):


# Tạo 3 danh sách rỗng
        small = []
        mid = []
        big = []

        for x in arr:
            if x < a:
                small.append(x)      # Nhóm nhỏ
            elif x > b:
                big.append(x)        # Nhóm lớn
            else:
                mid.append(x)        # Nhóm giữa (a <= x <= b)

# Gộp lại theo thứ tự: Nhỏ -> Giữa -> Lớn
# arr[:] để cập nhật trực tiếp vào list gốc (nếu cần)
        arr[:] = small + mid + big

        

	    
	        
	        
	       