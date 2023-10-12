import pygame

# Pygameの初期化
pygame.init()

# 画面の設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Square Button Example")

# ボタンの設定
button_color = (0, 255, 0)  # ボタンの背景色（緑）
button_width = 100
button_height = 100
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2

# クリック回数の初期化
click_count = 0

# ボタンに表示するテキスト
button_text = "click count: "

# ボタンを描画する関数
def draw_button(count):
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    draw_text(str(count), (button_x+30, button_y+15), 100, (255, 255, 255))

# テキストを描画する関数
def draw_text(text, position, font_size=36, text_color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, position)

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                # マウスクリックがボタン上にあるかをチェック
                mouse_x, mouse_y = event.pos
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    # ボタンがクリックされた場合、クリック回数を増加させる
                    click_count += 1

    # 画面をクリア
    screen.fill((255, 255, 255))  # 白で塗りつぶし

    # ボタンを描画
    draw_button(click_count)

    # クリック回数を表示
    draw_text(f"クリック回数: {click_count}", (20, 20))

    pygame.display.flip()

# Pygameの終了
pygame.quit()
