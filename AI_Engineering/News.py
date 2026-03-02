import urllib.request
import xml.etree.ElementTree as ET

import os
from dotenv import load_dotenv

# === THÊM THƯ VIỆN AI ===
# Cài đặt bằng lệnh: pip install google-generativeai python-dotenv
import google.generativeai as genai

# ==========================================
# GIAI ĐOẠN 1: KỸ SƯ DỮ LIỆU (DATA ENGINEERING)
# Thu thập và Lọc tin tức theo chủ đề (Chiến tranh & Chính trị)
# ==========================================

def lay_tin_tuc_chien_tranh_chinh_tri(so_luong=5):
    """
    Hàm này quét qua các chuyên mục thời sự/thế giới và dùng
    bộ lọc từ khóa để chỉ lấy các tin về chiến tranh, chính trị.
    """
    print("Đang quét máy chủ VNExpress để tìm tin Chiến tranh & Chính trị...")
    
    # Sử dụng RSS của mục Thế giới và Thời sự để tối ưu tỷ lệ tìm thấy
    urls_nguon = [
        'https://vnexpress.net/rss/the-gioi.rss',
        'https://vnexpress.net/rss/thoi-su.rss'
    ]
    
    # BỘ LỌC TỪ KHÓA (Kỹ thuật lọc text cơ bản)
    tu_khoa = [
        'chiến tranh', 'chính trị', 'quân sự', 'xung đột', 'tổng thống', 
        'thủ tướng', 'bầu cử', 'ngoại giao', 'tên lửa', 'quân đội', 
        'lãnh đạo', 'nga', 'ukraine', 'israel', 'hamas', 'nato','Iran'
    ]
    
    danh_sach_tin = []
    
    # Duyệt qua từng đường link RSS
    for url in urls_nguon:
        # Nếu đã lấy đủ số lượng tin yêu cầu thì dừng lại
        if len(danh_sach_tin) >= so_luong:
            break
            
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            xml_data = response.read().decode('utf-8')
            root = ET.fromstring(xml_data)
            
            # Quét từng bài báo trong luồng dữ liệu
            for item in root.findall('./channel/item'):
                if len(danh_sach_tin) >= so_luong:
                    break
                    
                tieu_de = item.find('title').text
                link = item.find('link').text
                thoi_gian = item.find('pubDate').text
                tom_tat_tho = item.find('description').text
                tom_tat = tom_tat_tho.split('</br>')[-1].strip() if '</br>' in tom_tat_tho else tom_tat_tho
                
                # --- THUẬT TOÁN LỌC (FILTERING) ---
                # Nối tiêu đề và tóm tắt lại, chuyển thành chữ thường để dễ so sánh
                text_kiem_tra = (tieu_de + " " + tom_tat).lower()
                
                # Kiểm tra xem có bất kỳ từ khóa nào xuất hiện trong bài báo không
                co_lien_quan = any(tk in text_kiem_tra for tk in tu_khoa)
                
                if co_lien_quan:
                    bai_bao = {
                        "Tieu_de": tieu_de,
                        "Tom_tat": tom_tat,
                        "Thoi_gian": thoi_gian,
                        "Link": link
                    }
                    
                    # Kiểm tra trùng lặp (phòng trường hợp 1 bài báo có ở cả 2 mục)
                    if not any(t['Link'] == link for t in danh_sach_tin):
                        danh_sach_tin.append(bai_bao)
                        
        except Exception as e:
            print(f"Lỗi kết nối tại {url}: {e}")
            
    return danh_sach_tin

# ==========================================
# CHẠY THỬ CHƯƠNG TRÌNH
# ==========================================
if __name__ == "__main__":
    print("==================================================")
    print("AI NEWS FETCHER (CHỦ ĐỀ: CHIẾN TRANH & CHÍNH TRỊ)")
    print("==================================================\n")
    
    # Yêu cầu hệ thống tìm 3 bài báo đúng chủ đề
    tin_nong = lay_tin_tuc_chien_tranh_chinh_tri(so_luong=3)
    
    if len(tin_nong) > 0:
        for i, tin in enumerate(tin_nong):
            print(f"📰 TIN SỐ {i+1}: {tin['Tieu_de']}")
            print(f"🕒 Thời gian: {tin['Thoi_gian']}")
            print(f"📝 Tóm tắt: {tin['Tom_tat'][:100]}...")
            print(f"🔗 Link đọc tiếp: {tin['Link']}")
            print("-" * 50)
    else:
        print("Hiện tại không tìm thấy bản tin nào khớp với chủ đề này.")
        
    # ==========================================
    # GIAI ĐOẠN 2: AI AGENT (REASONING & ACTING)
    # Kết nối với Google Gemini API để phân tích chuyên sâu
    # ==========================================
    def phan_tich_chuyen_sau_gemini(danh_sach_tin):
        # 1. Lấy API Key từ biến môi trường (File .env) ẩn
        load_dotenv() # Tải các thông tin bảo mật từ file .env vào hệ thống
        API_KEY = os.getenv("GEMINI_API_KEY")
        
        if not API_KEY:
            print("\n⚠️ CẢNH BÁO: Không tìm thấy Gemini API Key trong hệ thống.")
            print("Để bảo mật khi đưa code lên GitHub, hãy làm theo các bước sau:")
            print("1. Tạo một file tên là '.env' nằm cùng chỗ với file code này.")
            print("2. Viết dòng sau vào file .env: GEMINI_API_KEY=mã_key_thật_của_bạn")
            print("3. Mở terminal và gõ lệnh: pip install python-dotenv")
            return

        print("\n🤖 Đang gửi dữ liệu cho AI (Gemini) phân tích. Vui lòng đợi trong giây lát...")
        
        # Cấu hình API
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # 2. Kỹ nghệ Câu lệnh (Prompt Engineering) - Ép AI đóng vai chuyên gia
        prompt = "Hãy đóng vai một chuyên gia phân tích địa chính trị và tình báo.\n"
        prompt += "Tôi sẽ cung cấp cho bạn một số bản tin nóng nhất vừa được cào từ báo về. Hãy đọc và thực hiện 2 yêu cầu:\n"
        prompt += "1. Viết một Báo cáo Tình hình tóm tắt tổng quan những sự kiện đang diễn ra trong 3-4 câu.\n"
        prompt += "2. Đánh giá Mức độ căng thẳng toàn cầu (Thấp / Trung bình / Cao / Rất Cao) và giải thích ngắn gọn lý do.\n\n"
        prompt += "--- DỮ LIỆU TIN TỨC MỚI NHẤT ---\n"
        
        # Tự động nhồi các tin tức cào được vào Prompt
        for i, tin in enumerate(danh_sach_tin):
            prompt += f"Bản tin {i+1}:\n- Tiêu đề: {tin['Tieu_de']}\n- Tóm tắt: {tin['Tom_tat']}\n\n"
            
        # 3. Gọi AI suy luận
        try:
            response = model.generate_content(prompt)
            print("\n==================================================")
            print("🧠 BÁO CÁO PHÂN TÍCH TỪ AI (CHUYÊN GIA ĐỊA CHÍNH TRỊ)")
            print("==================================================")
            print(response.text)
        except Exception as e:
            print(f"\n❌ Có lỗi xảy ra khi gọi API: {e}")

    # Gọi hàm phân tích ngay sau khi in xong tin tức
    if len(tin_nong) > 0:
        phan_tich_chuyen_sau_gemini(tin_nong)