import pygame
import os
from pygame.locals import *
from sys import exit
import mega_data
import index

bg_color = (190, 200, 255)

root = os.path.dirname(__file__)
sprites_dir = os.path.join(root, 'sprites')
sounds_dir = os.path.join(root, 'sounds')



width = 1080
height = 720



pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(f"Joystick novo reconhecido: {joystick.get_name()}")

main_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Megaman")

axis_motion = [0, 0]



mbi_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-basic-idle.png')).convert_alpha()
mbw_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-basic-walk.png')).convert_alpha()
mbj_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-basic-jump.png')).convert_alpha()
mbis_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-idle-shoot.png')).convert_alpha()
mbi_rev_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-basic-idle-reverse.png')).convert_alpha()
mbw_rev_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-basic-walk-reverse.png')).convert_alpha()
mbj_rev_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-basic-jump-reverse.png')).convert_alpha()
mbis_rev_ss = pygame.image.load(os.path.join(sprites_dir, 'mega-idle-shoot-reverse.png')).convert_alpha()

m_buster_s = pygame.image.load(os.path.join(sprites_dir, 'mega-buster.png')).convert_alpha()



ice_man_stage_song = pygame.mixer.music.load(os.path.join(sounds_dir, "ice-man-gg-cut.mp3"))
pygame.mixer.music.play(999)


all_shots = []



gravity = 0.2
shoot_sign = False
shoot_ind = 0
mega_y_limit = height - 150


        

        

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
m_data = mega_data.Megaman()
all_sprites.add(m_data)





while True:

    clock.tick(60)
    main_screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == JOYBUTTONDOWN:
            print(event.button)
            if event.button == 10:
                pygame.quit()
                exit()
            
            if event.button == 2:
                if m_data.y > mega_y_limit:
                    m_data.jump = True
                    m_data.vy -= 8.5
                else:
                    print("COLIDIU COM LIMITE")

            if event.button == 3:
                if m_data.direction == "RIGHT":
                    m_data.shoot = True
                    shoot_sign = True
                    shoot_ind = 0
                    b_data = mega_data.Megabuster()
                    all_shots.append(b_data)
                    for i in range(len(all_shots)):
                        all_bullets.add(all_shots[i])
                        
                elif m_data.direction == "LEFT":
                    m_data.shoot = True
                    shoot_sign = True
                    shoot_ind = 0
                    b_data = mega_data.Megabuster()
                    all_shots.append(b_data)
                    all_bullets.add(b_data)
                    #all_sprites.add(b_data)

                #print(all_shots)
                

        if event.type == JOYAXISMOTION:
            axis_motion[event.axis] = event.value
            if abs(axis_motion[0]) > 0.4:
                axis_motion[event.axis] = event.value
            elif abs(axis_motion[0]) < 0.4:
                axis_motion[0] = 0

    

    all_sprites.draw(main_screen)
    all_sprites.update()
    all_bullets.draw(main_screen)
    all_bullets.update()
    m_data.x += axis_motion[0] * 3.9


    for i in all_shots:
        if i.x + i.w <= 50:
            all_bullets.remove(i)
            #all_sprites.remove(i)
    



    if shoot_sign:
        shoot_ind += 0.1
        if shoot_ind >= 5:
            m_data.shoot = False
            shoot_ind = 0
            shoot_sign = False
    else:
        shoot_ind = 0



    if axis_motion[0] == 0:
        m_data.walking = False
        m_data.idle = True
    else:
        m_data.walking = True
        m_data.idle = False

    if axis_motion[0] > 0.4:
        m_data.direction = "RIGHT"
    elif axis_motion[0] < -0.4:
        m_data.direction = "LEFT"
    

    if m_data.x < 0:
        m_data.x = 0
    elif m_data.x + m_data.w > width:
        m_data.x = width - m_data.w

    if m_data.y < 0:
        m_data.y = 0
    elif m_data.y + m_data.h > height:
        m_data.y = height - m_data.h
        m_data.vy = 0
        m_data.jump = False

    if m_data.y + m_data.h < height - 1:
        m_data.jump = True
    else:
        m_data.jump = False
    
    


    pygame.display.flip()
    pygame.display.update()