import tkinter as tk
import random
from tkinter import messagebox

def move_window(event):
    """Hàm này sẽ di chuyển cửa sổ đến vị trí ngẫu nhiên khi chuột chạm vào"""
    # Lấy kích thước màn hình của nạn nhân
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Kích thước của cửa sổ troll
    window_width = 350
    window_height = 150

    # Tạo tọa độ X, Y ngẫu nhiên mới (đảm bảo không bị lọt ra ngoài màn hình)
    new_x = random.randint(0, screen_width - window_width)
    new_y = random.randint(0, screen_height - window_height)

    # Cập nhật vị trí mới cho cửa sổ
    root.geometry(f'{window_width}x{window_height}+{new_x}+{new_y}')

def on_closing():
    """Hàm này sẽ chạy khi nạn nhân cố gắng bấm nút X để đóng cửa sổ"""
    messagebox.showwarning("Cảnh báo", "Bạn nghĩ tắt nó dễ thế sao? 😜")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Lỗi hệ thống nghiêm trọng!")
root.geometry("350x150")
root.resizable(False, False) # Không cho thay đổi kích thước
root.attributes("-topmost", True) # Luôn ghim trên cùng mọi ứng dụng khác

# Vô hiệu hóa nút X màu đỏ
root.protocol("WM_DELETE_WINDOW", on_closing)

# Thêm dòng chữ dọa nạt nhẹ nhàng
text_content = (
    "CẢNH BÁO BẢO MẬT!\n\n"
    "Hệ thống đang tiến hành xóa toàn bộ dữ liệu ổ C:...\n"
    "Hãy click chuột vào cửa sổ này để HỦY bỏ quá trình!"
)

label = tk.Label(root, text=text_content, font=("Arial", 10, "bold"), fg="red", justify="center")
label.pack(expand=True, fill="both", padx=10, pady=10)

# Quan trọng nhất: Bắt sự kiện '<Enter>' (khi con trỏ chuột bước vào không gian của cửa sổ)
root.bind('<Enter>', move_window)

# Chạy vòng lặp giao diện
root.mainloop()