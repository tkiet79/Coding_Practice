import pygame
import random
import math

# --- Cấu hình ban đầu ---
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hiệu ứng Pháo Hoa Liên Tục - Python")
CLOCK = pygame.time.Clock()

# Màu sắc
BLACK = (0, 0, 0)

# Lớp đại diện cho một hạt pháo hoa (Particle)
class Particle:
    def __init__(self, x, y, color, is_rocket=False):
        self.x = x
        self.y = y
        self.color = color
        self.is_rocket = is_rocket
        self.radius = 2 if not is_rocket else 4
        self.lifetime = 0  # Thời gian sống (đếm ngược để biến mất)

        if self.is_rocket:
            # Nếu là tên lửa: Bay thẳng lên
            self.vel_x = random.randint(-1, 1)  # Lệch trái phải một chút cho tự nhiên
            self.vel_y = random.randint(-15, -10) # Tốc độ bay lên
        else:
            # Nếu là hạt nổ: Bay tung tóe theo hình tròn
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 6)
            self.vel_x = math.cos(angle) * speed
            self.vel_y = math.sin(angle) * speed
            self.lifetime = 255  # Độ sáng (alpha) ban đầu

    def move(self):
        # Cập nhật vị trí
        self.x += self.vel_x
        self.y += self.vel_y

        if self.is_rocket:
            # Tên lửa chịu ít trọng lực hơn
            self.vel_y += 0.2
        else:
            # Hạt nổ chịu trọng lực (rơi xuống) và sức cản không khí (bay chậm lại)
            self.vel_y += 0.15 # Trọng lực
            self.vel_x *= 0.95 # Sức cản không khí ngang
            self.vel_y *= 0.95 # Sức cản không khí dọc
            self.lifetime -= 5 # Mờ dần nhanh hơn

    def draw(self, surface):
        if self.is_rocket:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        else:
            # Vẽ hạt nổ với hiệu ứng mờ dần (cần Surface phụ để chỉnh alpha)
            if self.lifetime > 0:
                # Tạo một bề mặt nhỏ trong suốt để vẽ hạt
                s = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
                r, g, b = self.color
                # Vẽ hình tròn lên bề mặt nhỏ đó với độ trong suốt (lifetime)
                pygame.draw.circle(s, (r, g, b, int(self.lifetime)), (self.radius, self.radius), self.radius)
                surface.blit(s, (int(self.x) - self.radius, int(self.y) - self.radius))

# --- Hàm tạo màu ngẫu nhiên rực rỡ ---
def random_color():
    # Chọn màu sáng (tránh màu quá tối)
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# --- Vòng lặp chính ---
def main():
    particles = [] # Chứa tất cả các hạt (cả tên lửa và hạt nổ)
    
    running = True
    while running:
        # 1. Tạo hiệu ứng mờ đuôi (Ghost Trail)
        # Thay vì xóa đen hoàn toàn (fill BLACK), ta phủ một lớp đen mờ lên
        # giúp tạo vệt đuôi đẹp mắt cho pháo hoa.
        fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        fade_surface.fill((0, 0, 0, 30)) # Số 30 là độ trong suốt (càng nhỏ đuôi càng dài)
        SCREEN.blit(fade_surface, (0, 0))

        # 2. Xử lý sự kiện tắt cửa sổ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 3. Tự động bắn pháo hoa ngẫu nhiên
        # Tỉ lệ 1/30 mỗi khung hình sẽ bắn một quả mới
        if random.randint(1, 30) == 1:
            start_x = random.randint(100, WIDTH - 100)
            particles.append(Particle(start_x, HEIGHT, random_color(), is_rocket=True))

        # 4. Cập nhật trạng thái các hạt
        for p in particles[:]: # Duyệt copy của list để có thể xóa phần tử
            p.move()
            p.draw(SCREEN)

            # Xử lý Logic nổ
            if p.is_rocket:
                # Nếu tên lửa bay chậm lại (đạt đỉnh) -> Nổ
                if p.vel_y >= -1: 
                    particles.remove(p)
                    # Tạo 50 hạt con nổ ra từ vị trí đó
                    for _ in range(50):
                        particles.append(Particle(p.x, p.y, p.color, is_rocket=False))
            else:
                # Nếu hạt nổ tắt hẳn -> Xóa
                if p.lifetime <= 0:
                    particles.remove(p)

        pygame.display.flip()
        CLOCK.tick(60) # Giới hạn 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()