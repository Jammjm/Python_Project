import pygame

###############################################################
pygame.init()  # 반드시 해야하는 초기화

#화면 설정
display_width = 480
display_height = 640
display_size = [display_width, display_height]
display = pygame.display.set_mode(display_size)

#게임타이틀
pygame.display.set_caption("미사일 피하기")  # 게임이름

#FPS
clock = pygame.time.Clock()
###############################################################

#1. 사용자 게임 초기화 (배경, 이미지, 좌표, 폰트)


game_run = True
while game_run:
    clock.tick(60)

    # 2. 게임 이벤트 처리 (키보드 마우스 등등)
    for event in pygame.event.get():  # 이벤트가 계속 발생하는동안
        if event.type == pygame.QUIT:
            game_run = False

    # 3.캐릭터 움직임 처리

    # 4. 충돌처리를 위한 rect정보

    # 5. 화면에 그리기 blit

    #화면 그리기
    pygame.display.update()

#게임 종료
pygame.quit()
