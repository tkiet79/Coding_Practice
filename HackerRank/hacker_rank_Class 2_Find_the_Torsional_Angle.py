import math
import numpy as np
class Points(object):
    # --- Bước 1: Hoàn thiện __init__ ---
    # Hàm này được gọi khi bạn viết Points(x, y, z)
    # Nó cần "lưu" x, y, z vào đối tượng    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # --- Bước 2: Hoàn thiện __sub__ (Phép trừ vector) ---
    # Hàm này được gọi khi bạn dùng toán tử '-' (ví dụ: b - a)
    # 'self' là đối tượng bên trái (b)
    # 'no' (viết tắt của "another object") là đối tượng bên phải (a)
    # Phép trừ vector (b-a) = (b.x - a.x, b.y - a.y, b.z - a.z)
    # Kết quả của phép trừ là một vector MỚI (một đối tượng Points mới)
    def __sub__(self, no):
        new_x = self.x - no.x
        new_y = self.y - no.y
        new_z = self.z - no.z
        return Points(new_x, new_y, new_z)

    # --- Bước 3: Hoàn thiện dot (Tích vô hướng) ---
    # Hàm này được gọi khi bạn viết x.dot(y)
    # Tích vô hướng (self · no) = (self.x * no.x + self.y * no.y + self.z * no.z)
    # Kết quả là một SỐ (scalar), không phải vector
    # tích vô hướng là lấy x nhân x, y nhân y, z nhân z
    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    # --- Bước 4: Hoàn thiện cross (Tích có hướng) ---
    # Hàm này được gọi khi bạn viết x.cross(y)
    # Tích có hướng (self × no)
    # Kết quả là một vector MỚI (một đối tượng Points mới)
    # cách nhân có hướng là viết 3 giá trị x,y,z của 2 vector đó ra thành 2 hàng ngang và thêm 1 cột của giá trị x của cả 2 vector
    # sau đó, tính giá trị nào thì che giá trị đó lại: vd:
    # A(x1,y1,z1) , B(x2,y2,z2) 
    # x1  y1  z1  x1
    # x2  y2  z2  x2
    # muốn tính giá trị x thì lấy che cột x lại sau đó lấy huyền trừ sắc tức (y1 x z2) - (y2 x z1) 
    # tương tự với các giá trị y và z
    def cross(self, no):
        new_x = (self.y * no.z) - (self.z * no.y)
        new_y = (self.z * no.x) - (self.x * no.z)
        new_z = (self.x * no.y) - (self.y * no.x)
        return Points(new_x, new_y, new_z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))