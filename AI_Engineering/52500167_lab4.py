import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

# Biến toàn cục để lưu đề bài 1 dùng cho bài 2
exercises_b1 = []

def bai_1():
    print("--- BÀI 1: TÍNH GIỚI HẠN ---")
    x = sp.symbols('x')
    
    global exercises_b1
    
    exercises_b1 = [
        ('a', sp.Abs(x**2 - x - 7), 3),
        ('b', sp.Abs(x - 1) / (x**2 - 1), 1),
        ('c', sp.exp(1/x), 1), 
        ('d', (x**4 - 16) / (x - 2), 2),
        ('e', (x**3 - x**2 - 5*x - 3) / ((x + 1)**2), -1),
        ('f', (x**2 - 9) / (sp.sqrt(x**2 + 7) - 4), 3),
        ('g', sp.Abs(x) / sp.sin(x), 1),
        ('h', (1 - sp.cos(x)) / (x * sp.sin(x)), 0),
        ('i', (2 * x**2) / (3 - 3*sp.cos(x)), 0),
        ('j', ((3 + x) / (-1 + x))**x, sp.oo),
        ('k', (1 - 2/(3 + x))**x, sp.oo),
        ('l', (1/x)**(1/x), sp.oo),
        ('m', (-x**(sp.Rational(1,3)) + (1+x)**(sp.Rational(1,3))) / (-sp.sqrt(x) + sp.sqrt(1+x)), sp.oo),
        ('n', sp.factorial(x) / x**x, sp.oo) 
    ]

    for label, expr, point in exercises_b1:
        try:
            limit_val = sp.limit(expr, x, point)
            print(f"({label}) Lim x->{point} của biểu thức = {limit_val}")
        except Exception as e:
            print(f"({label}) Không thể tính hoặc lỗi: {e}")
    print("\n")

def bai_2():
    print("--- BÀI 2: VẼ ĐỒ THỊ TỪNG CÂU RIÊNG BIỆT (a -> n) ---")
    
    x_sym = sp.symbols('x')

    for i, (label, expr, point) in enumerate(exercises_b1):
        print(f">> Đang vẽ đồ thị câu ({label})...")
        
        # Tạo figure mới cho mỗi bài toán
        plt.figure(figsize=(8, 6))
        
        # Chuyển đổi hàm sympy sang numpy
        try:
            f_func = sp.lambdify(x_sym, expr, modules=['numpy', 'math'])
        except:
            f_func = None

        # Xác định khoảng vẽ (xung quanh điểm giới hạn)
        is_infinity = (point == sp.oo or point == -sp.oo)
        
        if is_infinity:
            x_vals = np.linspace(1, 50, 500)
            title_point = r"$\infty$"
        else:
            p_val = float(point)
            x_vals = np.linspace(p_val - 2.5, p_val + 2.5, 500)
            title_point = str(point)

        # Tính giới hạn để hiển thị
        try:
            lim_val = sp.limit(expr, x_sym, point)
        except:
            lim_val = sp.nan

        # Tính giá trị y và xử lý lỗi
        y_vals = []
        if f_func:
            for val in x_vals:
                try:
                    if not is_infinity and abs(val - float(point)) < 1e-5:
                        y_vals.append(np.nan)
                        continue
                    
                    res = f_func(val)
                    
                    if isinstance(res, complex):
                        y_vals.append(res.real)
                    elif np.isinf(res) or np.isnan(res) or abs(res) > 100:
                        y_vals.append(np.nan)
                    else:
                        y_vals.append(res)
                except:
                    y_vals.append(np.nan)
        
        # Vẽ đồ thị
        try:
            plt.plot(x_vals, y_vals, label=f'Hàm số câu ({label})', linewidth=2)
            
            # Đánh dấu điểm giới hạn
            if not is_infinity and lim_val.is_real and not sp.zoo == lim_val:
                plt.scatter([float(point)], [float(lim_val)], color='red', s=60, zorder=5)
                plt.text(float(point) + 0.1, float(lim_val) + 0.1, f"L={float(lim_val):.2f}", color='red', fontsize=12, fontweight='bold')
            elif is_infinity and lim_val.is_real:
                plt.axhline(y=float(lim_val), color='r', linestyle='--', alpha=0.7, label=f'Tiệm cận y={float(lim_val):.2f}')

            plt.title(f"Đồ thị bài 1({label}): Lim khi x -> {title_point}", fontsize=14)
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.legend()
            plt.xlabel('x')
            plt.ylabel('f(x)')
            
            # Hiển thị đồ thị ngay lập tức
            plt.show()
            
        except Exception as e:
            print(f"Lỗi vẽ câu {label}: {e}")
            plt.close() # Đóng figure nếu lỗi để tránh rác

    print(">> Đã vẽ xong tất cả đồ thị.\n")

def bai_3():
    print("--- BÀI 3: TÌM GIỚI HẠN VÀ VẼ ĐỒ THỊ ---")
    x = sp.symbols('x')
    
    f1_sym = 1 / (1 + 2**(1/x))
    f2_sym = (x**2 + x) / sp.sqrt(x**3 + x**2)
    
    funcs = [("1", f1_sym), ("2", f2_sym)]

    for label, f in funcs:
        print(f"Hàm số {label}: f(x) = {f}")
        lim_phai = sp.limit(f, x, 0, dir='+')
        lim_trai = sp.limit(f, x, 0, dir='-')
        
        print(f"  Lim x->0+ : {lim_phai}")
        print(f"  Lim x->0- : {lim_trai}")
        
        if lim_phai == lim_trai:
            print(f"  => Lim x->0 : {lim_phai}")
        else:
            print(f"  => Lim x->0 : Không tồn tại")

    print(">> Đang hiển thị đồ thị Bài 3...")
    x_vals = np.linspace(-2, 2, 1000)
    x_vals = x_vals[x_vals != 0]
    
    y1 = []
    for val in x_vals:
        try:
            with np.errstate(over='ignore', divide='ignore'):
                term = 2.0**(1.0/val)
                if np.isinf(term): y1.append(0.0)
                else: y1.append(1.0 / (1.0 + term))
        except: y1.append(np.nan)
    
    x_vals2 = np.linspace(-0.95, 2, 1000)
    x_vals2 = x_vals2[x_vals2 != 0]
    y2 = (x_vals2**2 + x_vals2) / np.sqrt(x_vals2**3 + x_vals2**2)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y1, label='Bài 3.1')
    plt.title('Bài 3.1')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(x_vals2, y2, color='orange', label='Bài 3.2')
    plt.title('Bài 3.2')
    plt.grid(True)
    plt.show()
    print("\n")

def bai_4():
    print("--- BÀI 4: HÀM SIN(1/X) ---")
    x = sp.symbols('x')
    
    print("Tính toán:")
    try:
        lim_phai = sp.limit(sp.sin(1/x), x, 0, dir='+')
        print(f"  1. Lim x->0+ f(x): {lim_phai}")
    except:
        print("  1. Lim x->0+ f(x): Không tồn tại (do dao động)")

    print(f"  2. Lim x->0- f(x): 0")
    print("  3. Lim x->0 f(x): Không tồn tại.")

    print(">> Đang hiển thị đồ thị Bài 4...")
    x_vals = np.linspace(-0.1, 0.1, 2000) 
    x_vals = x_vals[x_vals != 0]
    y_vals = np.array([np.sin(1/v) if v > 0 else 0 for v in x_vals])
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x)$')
    plt.title(r'Bài 4: Dao động của $\sin(1/x)$ gần 0')
    plt.axvline(x=0, color='r', linestyle='--', alpha=0.5)
    plt.grid(True)
    plt.show()
    print("\n")

def check_continuity(func_expr, point_val, defined_val):
    x = sp.symbols('x')
    lim_val = sp.limit(func_expr, x, point_val)
    print(f"  Tại x = {point_val}: f({point_val})={defined_val}, Lim={lim_val}")
    if lim_val == defined_val: print("    => LIÊN TỤC")
    else: print("    => GIÁN ĐOẠN")

def bai_5():
    print("--- BÀI 5: CHỨNG MINH LIÊN TỤC ---")
    x = sp.symbols('x')
    
    f_a = x**2 - 7
    print("(a) f(x) = x^2 - 7, c = 1")
    check_continuity(f_a, 1, f_a.subs(x, 1))

    f_b = sp.sqrt(2*x - 3)
    print("(b) f(x) = sqrt(2x - 3), c = 2")
    check_continuity(f_b, 2, f_b.subs(x, 2))
    print("\n")

def bai_6():
    print("--- BÀI 6: KIỂM TRA ĐIỂM LIÊN TỤC ---")
    x = sp.symbols('x')

    print("(a) Tại x = 0:")
    check_continuity((x**2 - x - 6)/(x - 3), 0, 5)
    
    print("(b) Tại x = 2:")
    check_continuity((x**3 - 8)/(x**2 - 4), 2, 3)
    
    print("    Tại x = -2:")
    try:
        lim_val = sp.limit((x**3 - 8)/(x**2 - 4), x, -2)
        print(f"    Lim x->-2 = {lim_val}, f(-2)=4 => GIÁN ĐOẠN")
    except: print("    Không có giới hạn => GIÁN ĐOẠN")

    print("(c) Tại x = 2:")
    check_continuity((x**2 - x - 2)/(x - 2), 2, 1)

    print("(d) Tại x = 0:")
    try:
        lim_val = sp.limit(1/x**2, x, 0)
        print(f"    Lim x->0 = {lim_val}, f(0)=1 => GIÁN ĐOẠN")
    except: print("    => GIÁN ĐOẠN")
    print("\n")

def bai_7():
    print("--- BÀI 7: TÌM ĐIỂM GIÁN ĐOẠN ---")
    x = sp.symbols('x')
    
    print("1. f(x) = (x^2 - x - 2)/(x - 2)")
    print(f"   Gián đoạn tại x = {sp.solve(x - 2, x)}")

    print("2. f(x) = (x^2 - 2x - 3)/(2x - 6)")
    print(f"   Gián đoạn tại x = {sp.solve(2*x - 6, x)}")
    print("\n")

def bai_8():
    print("--- BÀI 8: KIỂM TRA TÍNH LIÊN TỤC TRÊN ĐOẠN [-1, 1] ---")
    x = sp.symbols('x')
    f = 1 - sp.sqrt(1 - x**2)
    print(f"Hàm số: f(x) = {f}")

    # 1. Kiểm tra giới hạn tại biên trái (-1) từ bên phải
    lim_trai_plus = sp.limit(f, x, -1, dir='+')
    val_trai = f.subs(x, -1)
    print(f"1. Tại x = -1:")
    print(f"   Lim x->-1+ = {lim_trai_plus}")
    print(f"   f(-1)      = {val_trai}")
    check_1 = (lim_trai_plus == val_trai)

    # 2. Kiểm tra giới hạn tại biên phải (1) từ bên trái
    lim_phai_minus = sp.limit(f, x, 1, dir='-')
    val_phai = f.subs(x, 1)
    print(f"2. Tại x = 1:")
    print(f"   Lim x->1-  = {lim_phai_minus}")
    print(f"   f(1)       = {val_phai}")
    check_2 = (lim_phai_minus == val_phai)

    if check_1 and check_2:
        print("=> KẾT LUẬN: Hàm số LIÊN TỤC trên đoạn [-1, 1]")
    else:
        print("=> KẾT LUẬN: Hàm số KHÔNG liên tục trên đoạn [-1, 1]")

    # Vẽ đồ thị minh họa
    print(">> Đang hiển thị đồ thị Bài 8...")
    x_vals = np.linspace(-1, 1, 500)
    y_vals = 1 - np.sqrt(1 - x_vals**2)
    
    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x) = 1 - \sqrt{1-x^2}$')
    plt.scatter([-1, 1], [1, 1], color='red', zorder=5, label='Endpoints')
    
    plt.title('Bài 8: Tính liên tục trên [-1, 1]')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.xlim(-1.5, 1.5)
    plt.ylim(0, 1.5)
    plt.legend()
    plt.show()
    print("\n")

def bai_10():
    print("--- BÀI 10: TÌM L ---")
    x = sp.symbols('x')
    
    limit_a = sp.limit(sp.sin(x)/x, x, 0)
    print(f"(a) Lim x->0 (sin x / x) = {limit_a} => Chọn L = {limit_a}")

    func_b = (x**2 + x - 6)/(x**2 - 4)
    limit_b = sp.limit(func_b, x, 2)
    print(f"(b) Lim x->2 (...) = {limit_b} => Chọn L = {limit_b}")

if __name__ == "__main__":
    bai_1()
    bai_2() 
    bai_3()
    bai_4()
    bai_5()
    bai_6()
    bai_7()
    bai_8() 
    bai_10()