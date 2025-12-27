import numpy
element = np.array(list(map(float,input().split())))
x = float(input())
print(numpy.polyval(element, x))

print(numpy.roots([1, 0, -1])) # Bạn đưa cho nó một danh sách các hệ số, nó sẽ giải phương trình và trả về các nghiệm.
# có nghĩa là 1x^2 + 0x - 1 = 0. Nó sẽ giải phương trình x^2 - 1 = 0 và tìm ra nghiệm là [-1. 1.].

print(numpy.poly([-1, 1, 1, 10])) # Bạn đưa cho nó một danh sách các nghiệm, nó sẽ xây dựng đa thức và trả về các hệ số.
# Nó sẽ tính (x+1)(x-1)(x-1)(x-10) và cho bạn các hệ số của đa thức x^4 - 11x^3 + 9x^2 + 11x - 10, tức là [ 1 -11 9 11 -10].

print(numpy.polyval([1, -2, 0, 2], 4)) # Tính giá trị (evaluate) của đa thức tại một điểm x cụ thể.
# nghĩa là 1x^3 - 2x^2 + 0x + 2 tại x = 4.Kết quả là: 1(4)^3 - 2(4)^2 + 0(4) + 2 = 64 - 32 + 2 = 34.

print(numpy.polyder([1, 1, 1, 1])) # Lấy đạo hàm (derivative) của đa thức.
# Lấy đạo hàm của 1x^3 + 1x^2 + 1x + 1. Kết quả là 3x^2 + 2x + 1, nên nó trả về các hệ số mới là [3, 2, 1].

print(numpy.polyint([1, 1, 1])) # Lấy tích phân (integral) hay nguyên hàm (antiderivative) của đa thức.
#  Lấy tích phân của 1x^2 + 1x + 1. Kết quả là (1/3)x^3 + (1/2)x^2 + 1x + C. NumPy sẽ trả về [0.333..., 0.5, 1, 0]. (Nó tự động cho hằng số tích phân C bằng 0).

print(numpy.polyfit([0,1,-1,2,-2], [0,1,1,4,4], 2)) 
# Yêu cầu tìm một đa thức bậc 2 (dạng ax^2+bx+c) khớp nhất với các điểm (0,0), (1,1), (-1,1), (2,4), (v.v...). 
# Nhìn vào các điểm này, ta có thể thấy chúng gần như nằm hoàn hảo trên đường y = 1x^2 + 0x + 0. Vì vậy, hàm này trả về các hệ số [1, 0, 0] (số cuối cùng là một số rất nhỏ, coi như 0).

#polyadd, polysub, polymul, polydiv. Đây là các hàm cơ bản để cộng, trừ, nhân, chia hai đa thức với nhau.
