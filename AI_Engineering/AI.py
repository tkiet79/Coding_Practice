import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# =====================================================================
# BẢN THIẾT KẾ MẠNG NƠ-RON 3 LỚP BẰNG PYTORCH
# =====================================================================
class PyTorchMNIST(nn.Module):
    def __init__(self):
        super(PyTorchMNIST, self).__init__() 
        self.fc1 = nn.Linear(in_features=784, out_features=128)
        self.fc2 = nn.Linear(in_features=128, out_features=64)
        self.fc3 = nn.Linear(in_features=64, out_features=10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)       
        x = self.relu(x)      
        x = self.fc2(x)       
        x = self.relu(x)      
        x = self.fc3(x)       
        return x

# =====================================================================
# HÀM HUẤN LUYỆN VỚI DỮ LIỆU ẢNH THẬT (REAL MNIST)
# =====================================================================
def train_real_mnist():
    print("--- DẠY AI NHẬN DIỆN CHỮ SỐ (DỮ LIỆU THẬT) ---")
    
    # 1. TẢI DỮ LIỆU TỪ INTERNET
    # Lệnh Transform này giúp biến bức ảnh thành Ma trận (Tensor) cho máy tính hiểu
    transform = transforms.Compose([transforms.ToTensor()]) 
    
    print("Đang tải dữ liệu MNIST (Vài chục MB)...")
    # Tải 60.000 ảnh để học
    train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    # Tải 10.000 ảnh để thi (test)
    test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    
    # DataLoader: Chia 60.000 ảnh thành từng lô (mỗi lô 64 ảnh)
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)
    
    # 2. KHỞI TẠO MÔ HÌNH VÀ CÔNG CỤ TỐI ƯU
    model = PyTorchMNIST()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    
    # 3. VÒNG LẶP TRAINING
    epochs = 5 # Chạy 5 vòng qua toàn bộ 60.000 bức ảnh
    print(f"\nBắt đầu Training {epochs} vòng...")
    
    for epoch in range(epochs):
        total_loss = 0
        
        # Vòng lặp lấy từng lô 64 bức ảnh ra để học
        for images, labels in train_loader:
            # Duỗi thẳng ảnh hình vuông 28x28 thành vector 784
            images = images.view(-1, 28*28)
            
            # --- 5 BƯỚC THẦN THÁNH ---
            optimizer.zero_grad()           # Xóa rác đạo hàm
            outputs = model(images)         # Lan truyền xuôi
            loss = criterion(outputs, labels)# Tính Loss
            loss.backward()                 # Tính đạo hàm cực nhanh (Backprop)
            optimizer.step()                # Cập nhật não bộ
            
            total_loss += loss.item()
            
        # In ra trung bình Loss của cả Epoch
        print(f"Epoch [{epoch+1}/{epochs}] | Loss trung bình: {total_loss/len(train_loader):.4f}")
        
    # 4. ĐÁNH GIÁ ĐỘ CHÍNH XÁC SAU KHI HỌC (TESTING PHASE)
    print("\n--- ĐÁNH GIÁ TRÊN 10.000 BỨC ẢNH MỚI TINH ---")
    correct = 0
    total = 0
    
    # Khi đi thi, ta không cần cập nhật não bộ nữa, tắt tính năng đạo hàm cho máy chạy nhanh
    with torch.no_grad(): 
        for images, labels in test_loader:
            images = images.view(-1, 28*28)
            outputs = model(images)
            
            # Lấy ra chữ số có xác suất cao nhất trong 10 cổng (0-9)
            _, predicted = torch.max(outputs.data, 1) 
            
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
    accuracy = 100 * correct / total
    print(f"✅ Độ chính xác của AI bạn vừa tạo ra là: {accuracy:.2f}%")
    print("🎉 CHÚC MỪNG BẠN CHÍNH THỨC HOÀN THÀNH MỘT PIPELINE AI HOÀN CHỈNH!")

if __name__ == "__main__":
    train_real_mnist()