# ==========================================
# PHẦN 1: IMPORT CÁC THƯ VIỆN CẦN THIẾT
# ==========================================
import torch          # Công cụ cốt lõi để tính toán Tensor và làm Deep Learning
import torch.nn as nn # Module chứa các khối xây dựng mạng nơ-ron (Linear, Embedding...)
import math           # Dùng để tính các phép toán như Logarit cơ số e (cho Positional Encoding)

# ==========================================
# PHẦN 2: LỚP POSITIONAL ENCODING (MÃ HÓA VỊ TRÍ)
# Mục đích: Giúp Transformer biết từ nào đứng trước, từ nào đứng sau 
# (vì nó đọc tất cả các từ cùng một lúc chứ không đọc từ trái sang phải).
# ==========================================
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        
        # 1. Tạo sẵn một ma trận toàn số 0.
        # - Số hàng là max_len (chiều dài tối đa của câu)
        # - Số cột là d_model (kích thước vector của mỗi từ)
        pe = torch.zeros(max_len, d_model)
        
        # 2. Tạo một cột số đếm từ 0 đến max_len - 1 (đại diện cho vị trí thứ 1, 2, 3... trong câu)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        
        # 3. Tính toán "bước sóng" bằng công thức toán học. 
        # Nhờ bước sóng khác nhau, các vector vị trí sẽ không bao giờ bị trùng lặp.
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        
        # 4. Áp dụng hàm Sin cho các cột chẵn (0, 2, 4...)
        pe[:, 0::2] = torch.sin(position * div_term) 
        # 5. Áp dụng hàm Cos cho các cột lẻ (1, 3, 5...)
        pe[:, 1::2] = torch.cos(position * div_term) 
        
        # 6. Lưu ma trận pe vào bộ nhớ của mô hình dưới dạng "buffer".
        # Dùng buffer thay vì Parameter vì ta KHÔNG MUỐN các số Sin/Cos này bị thay đổi khi huấn luyện.
        # unsqueeze(0) là để thêm chiều Batch vào đầu thành (1, max_len, d_model)
        self.register_buffer('pe', pe.unsqueeze(0))

    def forward(self, x):
        # Cắt lấy ma trận pe vừa vặn với độ dài thực tế của câu x đang xét (x.size(1))
        # Sau đó cộng thẳng vào x. Xong bước này, x chứa cả ngữ nghĩa lẫn vị trí!
        return x + self.pe[:, :x.size(1)]

# ==========================================
# PHẦN 3: LỚP GPT MODEL (TRÁI TIM CỦA HỆ THỐNG)
# ==========================================
class GPTModel(nn.Module):
    def __init__(self, vocab_size, d_model, num_heads, num_layers, dropout=0.1, max_len=100):
        super().__init__()
        
        # Lưu lại độ dài câu dài nhất mà mô hình này chịu đựng được
        self.max_len = max_len 
        
        # Cuốn "từ điển" biến ID (số nguyên) thành một vector (số thực)
        self.token_embedding = nn.Embedding(vocab_size, d_model)
        
        # Bộ mã hóa vị trí đã định nghĩa ở trên
        self.pos_encoding = PositionalEncoding(d_model, max_len)
        
        # Cơ chế "nhắm mắt ngẫu nhiên" bỏ qua một số thông tin để chống học vẹt (Overfitting)
        self.dropout = nn.Dropout(dropout)
        
        # Tạo ra một danh sách chứa `num_layers` khối Transformer
        self.blocks = nn.ModuleList([
            # Khối não bộ chính! Chứa cơ chế Self-Attention để các từ chú ý lẫn nhau.
            nn.TransformerEncoderLayer(
                d_model=d_model, 
                nhead=num_heads, 
                dim_feedforward=d_model*4, 
                batch_first=True, # Nghĩa là chiều Batch đứng đầu (Batch, Seq, Feature)
                norm_first=True   # Chuẩn hóa trước để quá trình train ổn định hơn
            ) for _ in range(num_layers)
        ])
        
        # Lớp chuẩn hóa cuối cùng, giúp dữ liệu ổn định trước khi đưa ra dự đoán
        self.ln_f = nn.LayerNorm(d_model)
        
        # Biến vector đặc trưng (d_model) quay ngược trở lại thành điểm số của toàn bộ từ vựng (vocab_size)
        self.head = nn.Linear(d_model, vocab_size)

    # --- LUỒNG ĐI DỮ LIỆU KHI HUẤN LUYỆN (TRAINING) ---
    def forward(self, idx):
        # Lấy độ dài hiện tại của câu
        sz = idx.size(1) 
        device = idx.device
        
        # Quá trình: Nhúng từ -> Cộng vị trí -> Dropout
        x = self.token_embedding(idx) 
        x = self.pos_encoding(x)
        x = self.dropout(x)
        
        # --- TẠO CAUSAL MASK (MẶT NẠ TIÊN TRI) ---
        # 1. Tạo một ma trận tam giác dưới toàn số 1.
        # Những số 1 này đại diện cho quá khứ và hiện tại (vùng an toàn, được phép nhìn)
        mask_ones = torch.tril(torch.ones(sz, sz, device=device))
        
        # 2. Đổ giá trị âm vô cùng (-inf) vào những vùng tương lai (chỗ có số 0)
        # Điều này bắt mô hình phải tự đoán chữ tiếp theo thay vì "nhìn trộm" đáp án phía sau.
        mask = torch.zeros(sz, sz, device=device)
        mask = mask.masked_fill(mask_ones == 0, float('-inf'))
        
        # Cho dữ liệu chạy qua từng khối Transformer, nhớ truyền cái 'mask' bịt mắt vào
        for block in self.blocks:
            x = block(x, src_mask=mask)
        
        # Đi qua chuẩn hóa và lớp Linear để xuất ra điểm số dự báo (Logits)
        x = self.ln_f(x)
        logits = self.head(x)
        return logits

    # ==========================================
    # PHẦN 4: VÒNG LẶP SINH VĂN BẢN (AUTOREGRESSIVE / INFERENCE)
    # Nhiệm vụ: Giúp mô hình "Tự nói chuyện", đẻ ra chữ mới liên tục
    # ==========================================
    @torch.no_grad() # Lệnh "bùa chú" bảo PyTorch: Đừng theo dõi đạo hàm nữa, ta chỉ đang dự đoán thôi (chạy nhanh, ít tốn RAM)
    def generate(self, idx, max_new_tokens):
        # idx là câu mồi ban đầu: shape (batch_size, seq_len)
        
        # Lặp bao nhiêu lần thì đẻ ra bấy nhiêu từ mới
        for _ in range(max_new_tokens):
            
            # 1. CROP CONTEXT (Cắt gọt ngữ cảnh)
            # Nếu câu văn mồi dài quá bộ nhớ (ví dụ > max_len), ta chặt bỏ đoạn đầu đi
            idx_cond = idx[:, -self.max_len:]
            
            # 2. Đưa đoạn chữ đó vào mô hình (gọi hàm forward ở trên) để lấy điểm số
            logits = self(idx_cond)
            
            # 3. CHỈ LẤY ĐIỂM SỐ CỦA TỪ CUỐI CÙNG
            # Dù mô hình nhả ra điểm số của cả câu, ta chỉ quan tâm đến vị trí cuối cùng vì đang tìm chữ tiếp theo
            # Logits shape: (Batch, Seq, Vocab) -> Lấy Seq cuối: (Batch, Vocab)
            logits_last_step = logits[:, -1, :] 
            
            # 4. Chuyển điểm số thành xác suất Softmax (từ 0% đến 100%)
            probs = torch.softmax(logits_last_step, dim=-1)
            
            # 5. GREEDY SEARCH (Chọn từ ngon nhất)
            # Lấy ID của từ có xác suất cao nhất. 
            idx_next = torch.argmax(probs, dim=-1, keepdim=True) # shape: (batch_size, 1)
            
            # 6. NỐI ĐUÔI (AUTOREGRESSIVE)
        # Dán từ mới đẻ ra vào đuôi câu mồi ban đầu, tạo thành một câu mới dài hơn cho vòng lặp sau!
        idx = torch.cat((idx, idx_next), dim=1)
    
        return idx

# ==========================================
# PHẦN 5: CHẠY THỬ NGHIỆM VỚI DỮ LIỆU THỰC TẾ
# ==========================================
def main():
    print("🚀 BẮT ĐẦU QUÁ TRÌNH SINH VĂN BẢN CÓ Ý NGHĨA...")
    
    # 1. TẠO NGƯỜI PHIÊN DỊCH (TOKENIZER)
    # Lấy một câu tiếng Việt làm vốn từ vựng sơ khai
    data_mau = "Xin chào thầy Gemini, hôm nay trò học AI rất vui!"
    chars = sorted(list(set(data_mau))) # Lấy danh sách các ký tự duy nhất
    vocab_size = len(chars)
    
    # Tạo từ điển dịch ngược/xuôi
    stoi = { ch:i for i,ch in enumerate(chars) } # Dịch Chữ -> Số (String to Integer)
    itos = { i:ch for i,ch in enumerate(chars) } # Dịch Số -> Chữ (Integer to String)
    
    encode = lambda s: [stoi[c] for c in s if c in stoi] # Hàm biến câu văn thành mảng ID
    decode = lambda l: ''.join([itos[i] for i in l])     # Hàm biến mảng ID thành câu văn
    
    # 2. KHỞI TẠO MÔ HÌNH
    d_model = 64 
    num_heads = 4
    num_layers = 4 
    model = GPTModel(vocab_size, d_model, num_heads, num_layers)
    
    model.eval() # Bật chế độ dự đoán (Inference mode)
    
    # 3. ĐƯA CÂU MỒI THỰC TẾ VÀO
    cau_moi = "Xin chào"
    print(f"\n📝 1. Câu mồi ban đầu (Chữ): '{cau_moi}'")
    
    # Mã hóa câu mồi
    input_ids = encode(cau_moi)
    start_context = torch.LongTensor([input_ids]) 
    print(f"🔢 2. Máy tính nhìn thấy (ID): {start_context[0].tolist()}")
    
    # 4. CHO GPT TỰ NÓI
    # Yêu cầu mô hình đẻ thêm 20 ký tự nữa
    generated_ids = model.generate(start_context, max_new_tokens=20)
    
    # Dịch số ngược lại thành chữ để con người đọc
    output_text = decode(generated_ids[0].tolist())
    print(f"✨ 3. Kết quả mô hình sinh ra: '{output_text}'")
    
    print("\n(💡 LỜI NHẮN TỪ THẦY: Trò đọc kết quả thấy nó nói nhảm (gibberish) đúng không? Đừng hoảng!)")
    print("Bởi vì các ma trận (Embedding, Linear...) trong mô hình hiện tại đều là SỐ NGẪU NHIÊN.")
    print("Mô hình của chúng ta giống như một em bé sơ sinh, có đầy đủ não bộ (Transformer) nhưng chưa được đi học (Train).")

if __name__ == "__main__":
    main()