import numpy as np

# --- BẢNG TRA CỨU (Tạo 1 lần) ---
# Dùng để chuyển đổi 'A4', 'B2' v.v. sang tọa độ (hàng, cột)
ROWS = ['4', '3', '2', '1']
COLS = ['A', 'B', 'C', 'D']
LOOKUP_BOARD = np.array([[c + r for c in COLS] for r in ROWS])

# --- CÁC HÀM TÌM NƯỚC ĐI (Bước 2: Chi tiết) ---

def is_valid_target(board, r, c, is_white_turn):
    """
    Hàm trợ giúp kiểm tra 3 quy tắc "trượt" mà chúng ta đã thảo luận.
    Trả về (True, True) nếu có thể ĂN QUÂN ĐỊCH.
    Trả về (True, False) nếu có thể DI CHUYỂN đến (ô trống).
    Trả về (False, False) nếu KHÔNG HỢP LỆ (ngoài bàn cờ hoặc đụng quân nhà).
    """
    # 1. Dừng lại nếu đi ra NGOÀI BÀN CỜ
    if not (0 <= r < 4 and 0 <= c < 4):
        return (False, False) 

    target_piece = board[r, c]
    
    # 2. Nếu là ô trống
    if target_piece == '.':
        return (True, False) 

    # 3. Kiểm tra quân nhà / quân địch
    is_target_white = target_piece.isupper() # 'N' -> True, 'q' -> False

    # 4. Dừng lại nếu đụng QUÂN CÙNG PHE
    if is_white_turn == is_target_white:
        return (False, False) 

    # 5. Có thể ĂN QUÂN ĐỊCH
    return (True, True) 

def get_sliding_moves(board, r, c, is_white_turn, directions):
    """
    Hàm "trượt" cho Xe, Tượng, Hậu.
    """
    all_moves = []
    for dr, dc in directions:
        current_r, current_c = r + dr, c + dc 
        
        while True:
            can_move, can_capture = is_valid_target(board, current_r, current_c, is_white_turn)
            
            if not can_move:
                break # Bị chặn (ra ngoài bàn cờ hoặc đụng quân nhà)
            
            all_moves.append((current_r, current_c))
            
            if can_capture:
                break # Đã ăn quân địch, dừng lại
            
            current_r += dr
            current_c += dc
            
    return all_moves

def get_all_moves_for_player(board, is_white_turn):
    """
    Tạo ra một danh sách TẤT CẢ các nước đi hợp lệ.
    Hàm này trả về các "bộ" (tuple) di chuyển: ((từ_hàng, từ_cột), (tới_hàng, tới_cột))
    Chúng ta cần điều này để "giả lập" nước đi trong hàm 'solve'.
    """
    all_move_tuples = [] # Danh sách các ((from_r, from_c), (to_r, to_c))
    
    knight_deltas = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                       (-1, -2), (-1, 2), (1, -2), (1, 2)]
    rook_deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bishop_deltas = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for r in range(4):
        for c in range(4):
            piece = board[r, c]
            if piece == '.':
                continue

            is_piece_white = piece.isupper()
            
            if is_white_turn == is_piece_white:
                # Đây là quân cờ của chúng ta. Tìm nước đi.
                
                # Hàm trợ giúp để thêm nước đi vào danh sách
                def add_moves_from_targets(targets):
                    for (to_r, to_c) in targets:
                        all_move_tuples.append(((r, c), (to_r, to_c)))

                # 1. Mã (Knight)
                if piece.upper() == 'N':
                    knight_targets = []
                    for dr, dc in knight_deltas:
                        new_r, new_c = r + dr, c + dc
                        can_move, _ = is_valid_target(board, new_r, new_c, is_white_turn)
                        if can_move:
                            knight_targets.append((new_r, new_c))
                    add_moves_from_targets(knight_targets)
                
                # 2. Xe (Rook)
                if piece.upper() == 'R':
                    add_moves_from_targets(get_sliding_moves(board, r, c, is_white_turn, rook_deltas))
                
                # 3. Tượng (Bishop)
                if piece.upper() == 'B':
                    add_moves_from_targets(get_sliding_moves(board, r, c, is_white_turn, bishop_deltas))
                
                # 4. Hậu (Queen)
                if piece.upper() == 'Q':
                    add_moves_from_targets(get_sliding_moves(board, r, c, is_white_turn, rook_deltas + bishop_deltas))
            
    return all_move_tuples

# --- BỘ NÃO MINIMAX (Bước 3: Chi tiết) ---

# Dùng một 'memo' (bộ đệm) để lưu các kết quả đã tính, tăng tốc độ
memo = {}

def solve(board, moves_left, is_white_turn):
    """
    Hàm đệ quy Minimax.
    Trả về True nếu Trắng có thể ÉP thắng, ngược lại False.
    """
    
    # Tạo một 'key' duy nhất cho trạng thái hiện tại để kiểm tra bộ đệm
    # (board.tobytes() là cách nhanh để hash một mảng NumPy)
    state_key = (board.tobytes(), moves_left, is_white_turn)
    if state_key in memo:
        return memo[state_key]

    # --- TRƯỜNG HỢP CƠ SỞ 1: KIỂM TRA THẮNG NGAY LẬP TỨC ---
    # Đây là "Quy tắc 1" của bạn: "Hậu đen nằm trong các ô bên trắng có thể di chuyển"
    
    # 1a. Xác định mục tiêu
    target_queen_piece = 'q' if is_white_turn else 'Q'
    
    # 1b. Tìm vị trí Hậu của đối thủ
    loc = np.where(board == target_queen_piece)
    if len(loc[0]) == 0:
        # Nếu không tìm thấy Hậu đối thủ (họ đã bị ăn ở lượt TRƯỚC)
        # -> Người chơi hiện tại KHÔNG thể thắng (vì họ đã thắng rồi)
        # -> Người chơi trước (đối thủ) đã thắng.
        result = not is_white_turn # True nếu Đen thắng, False nếu Trắng thắng
        memo[state_key] = result
        return result # Trả về kết quả của lượt TRƯỚC

    queen_pos = (loc[0][0], loc[1][0])
    
    # 1c. Kiểm tra xem người chơi hiện tại có thể ăn Hậu không
    # (Hàm này chỉ cần danh sách các ô có thể đến)
    all_target_squares = set(m[1] for m in get_all_moves_for_player(board, is_white_turn))
    
    if queen_pos in all_target_squares:
        # Người chơi hiện tại có thể ăn Hậu -> Thắng!
        memo[state_key] = True # (Trắng thắng)
        return True # (Trắng thắng)

    # --- TRƯỜNG HỢP CƠ SỞ 2: HẾT NƯỚC ĐI ---
    # Đây là quy tắc "Trắng thua" nếu hết nước đi mà chưa thắng
    if moves_left == 0:
        memo[state_key] = False # Trắng không ép thắng được
        return False

    # --- BƯỚC ĐỆ QUY (MINIMAX) ---
    
    # Lấy tất cả các nước đi ((from), (to)) để giả lập
    all_moves = get_all_moves_for_player(board, is_white_turn)

    if is_white_turn:
        # --- Lượt của Trắng (Maximizer) ---
        # Trắng chỉ cần tìm ÍT NHẤT MỘT nước đi dẫn đến thắng.
        for (from_r, from_c), (to_r, to_c) in all_moves:
            # "Thử" nước đi trên một bàn cờ mới
            new_board = board.copy()
            new_board[to_r, to_c] = new_board[from_r, from_c]
            new_board[from_r, from_c] = '.'
            
            # Gọi đệ quy cho lượt của Đen
            if solve(new_board, moves_left - 1, False) == True:
                # Nếu Trắng tìm thấy MỘT đường thắng, dừng lại và trả về True
                memo[state_key] = True
                return True
        
        # Nếu lặp qua tất cả các nước đi mà không tìm thấy đường thắng
        memo[state_key] = False
        return False
        
    else:
        # --- Lượt của Đen (Minimizer) ---
        # Đen chỉ cần tìm ÍT NHẤT MỘT nước đi để CHẶN Trắng thắng.
        for (from_r, from_c), (to_r, to_c) in all_moves:
            # "Thử" nước đi
            new_board = board.copy()
            new_board[to_r, to_c] = new_board[from_r, from_c]
            new_board[from_r, from_c] = '.'
            
            # Gọi đệ quy cho lượt của Trắng
            if solve(new_board, moves_left - 1, True) == False:
                # Nếu Đen tìm thấy MỘT đường phòng thủ (làm Trắng thua)
                # -> Đen sẽ chọn nước này, và kết quả của nhánh này là False
                memo[state_key] = False
                return False
                
        # Nếu Đen đã thử tất cả các nước đi mà vẫn bị Trắng ép thắng
        memo[state_key] = True
        return True

# === HÀM CHÍNH (Bước 1: Đã hoàn thành) ===
def simplifiedChessEngine(whites, blacks, m):
    # 1. Xóa bộ đệm (memo) cho mỗi ván cờ mới
    global memo
    memo = {}
    
    # 2. Tạo bàn cờ trạng thái (game_state) trống
    game_state = np.full((4, 4), '.') 
    
    # 3. Đặt quân Trắng
    for piece_info in whites:
        name = piece_info[0] 
        coord_str = piece_info[1] + piece_info[2]
        loc = np.where(LOOKUP_BOARD == coord_str)
        r, c = loc[0][0], loc[1][0]
        game_state[r, c] = name 
        
    # 4. Đặt quân Đen
    for piece_info in blacks:
        name = piece_info[0] 
        coord_str = piece_info[1] + piece_info[2]
        loc = np.where(LOOKUP_BOARD == coord_str)
        r, c = loc[0][0], loc[1][0]
        game_state[r, c] = name.lower() 
        
    # 5. Bắt đầu thuật toán Minimax!
    # Lượt đầu tiên (moves_left = m) luôn là của Trắng (is_white_turn = True)
    if solve(game_state, m, True):
        return "YES"
    else:
        return "NO"