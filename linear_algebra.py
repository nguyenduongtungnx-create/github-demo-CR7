import matplotlib.pyplot as plt
import numpy as np

# 1. Tọa độ gốc của Jennifer (trong thế giới của cô ấy)
v_jen = np.array([3, 4])

# 2. Ma trận cơ sở A (Cách chúng ta nhìn hệ thước đo của Jennifer)
A = np.array([[2, -1],
              [1,  1]])

# 3. Tọa độ thực tế theo góc nhìn của chúng ta
v_our = A @ v_jen  # Kết quả sẽ là [2, 7]

# Tạo khung hình với 2 đồ thị nằm ngang
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# ==========================================
# ĐỒ THỊ 1: GÓC NHÌN TỪ THẾ GIỚI CỦA JENNIFER
# ==========================================
ax1.set_title("1. Thế giới của Jennifer\n(Tọa độ ban đầu [3, 4])", fontsize=14)
ax1.grid(True, linestyle='--', color='gray', alpha=0.5)
ax1.axhline(0, color='black', linewidth=1)
ax1.axvline(0, color='black', linewidth=1)
ax1.set_xlim(-1, 5)
ax1.set_ylim(-1, 6)
ax1.set_aspect('equal')

# Trong mắt cô ấy, vector cơ sở của mình là lưới vuông chuẩn [1,0] và [0,1]
ax1.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='green', label='Bước ngang nội bộ (1, 0)')
ax1.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='red', label='Bước dọc nội bộ (0, 1)')

# Đường đi đến tọa độ ban đầu [3, 4]
ax1.plot([0, 3], [0, 0], color='green', linestyle=':', linewidth=2)
ax1.plot([3, 3], [0, 4], color='red', linestyle=':', linewidth=2)
ax1.scatter(v_jen[0], v_jen[1], color='blue', s=100, zorder=5)
ax1.text(v_jen[0] - 0.5, v_jen[1] + 0.3, "v = [3, 4]", color='blue', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')

# ==========================================
# ĐỒ THỊ 2: GÓC NHÌN TỪ THẾ GIỚI CỦA CHÚNG TA
# ==========================================
ax2.set_title("2. Thế giới của Chúng ta\n(Tọa độ đã quy đổi [2, 7])", fontsize=14)
ax2.grid(True, linestyle=':', color='gray', alpha=0.5)
ax2.axhline(0, color='black', linewidth=1)
ax2.axvline(0, color='black', linewidth=1)
ax2.set_xlim(-3, 8)
ax2.set_ylim(-1, 9)
ax2.set_aspect('equal')

# Lấy 2 vector cơ sở của Jennifer từ ma trận A
u1 = A[:, 0]  # [2, 1]
u2 = A[:, 1]  # [-1, 1]

ax2.quiver(0, 0, u1[0], u1[1], angles='xy', scale_units='xy', scale=1, color='green', label='Vector u1 = [2, 1]')
ax2.quiver(0, 0, u2[0], u2[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector u2 = [-1, 1]')

# Đường đi 3 bước u1 và 4 bước u2
ax2.plot([0, 3*u1[0]], [0, 3*u1[1]], color='green', linestyle=':', linewidth=2)
ax2.plot([3*u1[0], v_our[0]], [3*u1[1], v_our[1]], color='red', linestyle=':', linewidth=2)
ax2.scatter(v_our[0], v_our[1], color='purple', s=100, zorder=5)
ax2.text(v_our[0] - 0.5, v_our[1] + 0.3, "v' = [2, 7]", color='purple', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()