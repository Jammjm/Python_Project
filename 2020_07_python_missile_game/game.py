import pygame
from random import *

pygame.init() # 반드시 해야하는 초기화

#화면 설정
display_width = 480
display_height = 640
display_size = [display_width, display_height]
display = pygame.display.set_mode(display_size)


#게임타이틀
pygame.display.set_caption("미사일피하기!") #게임이름

#게임 폰트
display_font = pygame.font.Font(None , 30)

#게임 이미지 불러오기
background = pygame.image.load("D:\\1학업\\사회복무_법인공인인증서\\Python Workspace\\Python_Project\\Python_Project\\2020_07_python_missile_game\\background.png")

user = pygame.image.load("D:\\1학업\\사회복무_법인공인인증서\\Python Workspace\\Python_Project\\Python_Project\\2020_07_python_missile_game\\user.png").convert()
user_size = user.get_rect().size
user_width = user_size[0]
user_height = user_size[1]

enemy = pygame.image.load("D:\\1학업\\사회복무_법인공인인증서\\Python Workspace\\Python_Project\\Python_Project\\2020_07_python_missile_game\\enemy.png").convert()
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]



user_X_pos = display_width/2 - user_width/2

enemies = [[randint(0, display_width - enemy_width), 0 , 5]]
#enemy_X_pos = 0
#enemy_Y_pos = 0

# 1000ms 마다 enemy 생성
enemy_new_time = 1000

# enemy_refreshed_index 와 이벤트 while 내 elapsed_time의 차이가 enemy_new_time이 되면 new enemy 생성
enemy_refreshed_index = 0

#게임스코어
game_score = 0

#게임 이벤트 루프
clock = pygame.time.Clock()

user_move_left = False
user_move_right = False
user_move_speed = 7

enemy_move_speed_start = 5
enemy_move_speed = 5

start_time = pygame.time.get_ticks()

game_run = True
while game_run:

    clock.tick(60)
    
    for event in pygame.event.get(): #이벤트가 계속 발생하는동안
        if event.type == pygame.QUIT:
            game_run = False
          
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                user_move_right = True
                #print("RIGHT PRESS")
                

            if event.key == pygame.K_LEFT:
                user_move_left =True
                #print("LEFT PRESS")

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                user_move_right = False
                #print("RIGHT UP")
                
            if event.key == pygame.K_LEFT:
                user_move_left = False
               # print("LEFT UP")
    
    # user 움직임 처리
    if user_move_left:
        user_X_pos -= user_move_speed
    if user_move_right:
        user_X_pos += user_move_speed


    #충돌처리를 위한 rect정보
    #반드시 left와 top정보 입력해야함
    user_rect = user.get_rect()
    user_rect.left = user_X_pos
    user_rect.top = display_height - user_height

    # enemy 요소들을 가져와서 요소들 움직임 및 충돌처리
    for idx, enemy_element in enumerate(enemies):
       
       #enemy 요소 Y_pos 변경
        enemy_element[1] += enemy_element[2]
            
        #지면에 닿은경우 요소 삭제    
        if enemy_element[1] > display_height:
          # print(str(idx) + "enemy dead")
            del enemies[idx]
            game_score += 1

        #충돌처리
        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_element[0]
        enemy_rect.top = enemy_element[1]

        # 충돌했을때
        if enemy_rect.colliderect(user_rect):
            #print("your score: "+ str(game_score))
            game_run = False
        
    
    #user가 화면밖으로 나가지 않도록 처리
    if user_X_pos < 0:
        user_X_pos = 0
    elif user_X_pos > display_width - user_width:
        user_X_pos = display_width - user_width
    
    #display 백그라운드 표시
    display.blit(background,(0,0))
    #user enemy 표시
    display.blit(user,(user_X_pos, display_height - user_height))
    for enemy_element in enemies:
        display.blit(enemy,(enemy_element[0],enemy_element[1]))
    # 시간 점수 표시
    score_to_display = display_font.render(("score: "+ str(game_score)) , True, (255,255,255))
    display.blit(score_to_display , (5,5))

    #경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_time)
    #print(str(int(elapsed_time/1000)))
    
 #난이도 조절
    enemy_new_time -= 0.3
    if enemy_new_time <= 250:
        enemy_new_time = 250
    enemy_move_speed += 0.002
    if enemy_move_speed >= 15:
        enemy_move_speed = 15

    # 새로운 enemy 추가
    if elapsed_time - enemy_refreshed_index > enemy_new_time:
        enemy_random_speed = uniform(float(enemy_move_speed_start), enemy_move_speed)
        enemies.append([randint(0, display_width - enemy_width), 0, enemy_random_speed]) 
        enemy_refreshed_index = elapsed_time
        
       
        
    
    #화면 그리기
    pygame.display.update()

#게임 종료
pygame.quit()
