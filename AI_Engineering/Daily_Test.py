class Value:
    """
    Class Value: Bọc một con số bình thường lại để theo dõi 'gia phả' của nó.
    """
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0 # Đạo hàm (lúc đầu khởi tạo luôn bằng 0)
        
        # LƯU TRỮ GIA PHẢ
        self._prev = set(_children) # Tập hợp các Node cha đẻ ra nó
        self._op = _op              # Phép toán nào đã đẻ ra nó (+, *, v.v.)
        self.label = label          # Tên của Node (để dễ in ra xem)

    def __repr__(self):
        # Hàm này giúp khi print(a) nó in ra đẹp đẽ hơn
        return f"Value(data={self.data})"

    # ==========================================
    # KHU VỰC CỦA EM: GHI NHẬN PHÉP TOÁN
    # ==========================================
    def __add__(self, other):
        """
        Được gọi khi em dùng dấu cộng: a + b
        self chính là a, other chính là b.
        """
        # Khởi tạo một đối tượng Value() MỚI mang giá trị tổng.
        # Truyền luôn data, tập hợp cha mẹ (self, other) và phép '+' vào hàm __init__
        out = Value(self.data + other.data, (self, other), '+')
        return out

    def __mul__(self, other):
        """
        Được gọi khi em dùng dấu nhân: a * b
        """
        # Làm tương tự như hàm __add__, nhưng đây là phép NHÂN
        out = Value(self.data * other.data, (self, other), '*') # CODE VÀO ĐÂY
        return out

def main():
    # TEST XÂY DỰNG ĐỒ THỊ TÍNH TOÁN
    print("--- TEST ĐỒ THỊ TÍNH TOÁN ---")
    
    a = Value(2.0, label='a')
    b = Value(-3.0, label='b')
    c = Value(10.0, label='c')
    
    # Thực hiện phép tính: d = a * b + c
    # Python sẽ tự động gọi a.__mul__(b), sau đó lấy kết quả gọi tiếp __add__(c)
    e = a * b
    e.label = 'e'
    d = e + c
    d.label = 'd'
    
    print(f"Kết quả của d: {d.data} (Mong đợi: 4.0)")
    
    # Kiểm tra gia phả của d
    print(f"\nGia phả của d:")
    print(f"- d được tạo ra bởi phép toán: '{d._op}'")
    print(f"- Cha mẹ trực tiếp của d là: {d._prev}")

if __name__ == "__main__":
    main()