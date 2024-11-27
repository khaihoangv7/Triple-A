import pygame

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simply Wizard')
pygame.display.set_icon(pygame.image.load('sword.png'))

# Tải hình ảnh nhân vật
player = pygame.image.load("assets/player/wizardred1.png").convert_alpha()
player_movement = player.get_rect()  # Lấy kích thước và tọa độ của nhân vật
player_movement.topleft = (100, 400)  # Đặt nhân vật ở vị trí ban đầu

# Tốc độ di chuyển và trọng lực
speed = 5
gravity = 0.8
jump_strength = -15

# Biến trạng thái
velocity_y = 0  # Vận tốc dọc (trọng lực và nhảy)
on_ground = True  # Kiểm tra xem nhân vật có đang đứng trên mặt đất không

# Camera
camera_x = 0  # Tọa độ x của camera

# Tải nhạc nền
pygame.mixer.init()
pygame.mixer.music.load('assets/music/nhacnen.mp3')
pygame.mixer.music.play(-1)

# Màu nền
GREEN = (200, 250, 200)

# Đồng hồ FPS
clock = pygame.time.Clock()

# Bản đồ (dạng nền đơn giản)
ground_y = 500  # Vị trí mặt đất

# Vòng lặp game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lấy trạng thái phím bấm (ấn giữ phím)
    keys = pygame.key.get_pressed()
    dx = 0  # Chuyển động ngang

    # Kiểm tra các phím di chuyển
    if keys[pygame.K_a]:  # Di chuyển trái
        dx = -speed
    if keys[pygame.K_d]:  # Di chuyển phải
        dx = speed
    if keys[pygame.K_w] and on_ground:  # Nhảy
        velocity_y = jump_strength
        on_ground = False

    # Áp dụng trọng lực
    velocity_y += gravity
    player_movement.y += velocity_y

    # Kiểm tra va chạm với mặt đất
    if player_movement.y + player_movement.height >= ground_y:
        player_movement.y = ground_y - player_movement.height
        velocity_y = 0
        on_ground = True

    # Cập nhật vị trí ngang của nhân vật
    player_movement.x += dx

    # Camera theo dõi nhân vật
    camera_x = player_movement.x - WIDTH // 2
    camera_x = max(0, camera_x)  # Không cho camera lùi quá đầu map

    # Vẽ màn hình
    screen.fill(GREEN)  # Làm sạch màn hình
    # Vẽ mặt đất (dịch chuyển theo camera)
    pygame.draw.rect(screen, (139, 69, 19), (0 - camera_x, ground_y, 2000, HEIGHT - ground_y))  # Bản đồ dài 2000px
    # Vẽ nhân vật
    screen.blit(player, (player_movement.x - camera_x, player_movement.y))  # Dịch chuyển nhân vật theo camera

    pygame.display.flip()  # Cập nhật màn hình

    clock.tick(60)  # Đặt FPS (60 frame mỗi giây)

pygame.quit()
