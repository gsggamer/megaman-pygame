import pygame
from pygame.locals import *
import os
from sys import exit
import index

class Megaman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.walking = False
        self.idle = True
        self.jump = False
        self.shoot = False

        self.x = 120
        self.y = 200
        self.w = 24*3.2
        self.h = 24*3.2

        self.direction = "RIGHT"

        self.vy = 0

        self.mega_images = []

        self.mega_bi_images = []
        self.mega_bi_rev_images = []
        self.mega_bw_images = []
        self.mega_bw_rev_images = []
        self.mega_jump_image = []
        self.mega_jump_rev_image = []
        self.mega_idle_shoot_image = []



        mbuster = index.m_buster_ss.subsurface((0, 0), (35, 25))
        mbuster = pygame.transform.scale(mbuster, (35*4, 25*4))
        self.mega_buster_image = mbuster



        for i in range(3):
            mbi_is = index.mbi_ss.subsurface((i * 21.5, 0), (22, 24))
            mbi_is = pygame.transform.scale(mbi_is, (22*3.2, 24*3.2))
            self.mega_bi_images.append(mbi_is)
        for i in range(3):
            mbw_is = index.mbw_ss.subsurface((i * 24, 0), (24, 24))
            mbw_is = pygame.transform.scale(mbw_is, (24*3.2, 24*3.2))
            self.mega_bw_images.append(mbw_is)
        
        for i in range(3):
            mbw_r_is = index.mbw_rev_ss.subsurface((i * 24, 0), (24, 24))
            mbw_r_is = pygame.transform.scale(mbw_r_is, (24*3.2, 24*3.2))
            self.mega_bw_rev_images.append(mbw_r_is)
        for i in range(3):
            mbi_r_is = index.mbi_rev_ss.subsurface((i * 21.5, 0), (22, 24))
            mbi_r_is = pygame.transform.scale(mbi_r_is, (22*3.2, 24*3.2))
            self.mega_bi_rev_images.append(mbi_r_is)

        for i in range(1):
            mbj_i = index.mbj_ss.subsurface((i * 26, 0), (26, 30))
            mbj_i = pygame.transform.scale(mbj_i, (26*3.2, 30*3.2))
            self.mega_jump_image.append(mbj_i)
        for i in range(1):
            mbj_r_i = index.mbj_rev_ss.subsurface((i * 26, 0), (26, 30))
            mbj_r_i = pygame.transform.scale(mbj_r_i, (26*3.2, 30*3.2))
            self.mega_jump_rev_image.append(mbj_r_i)

        for i in range(1):
            mbis_i = index.mbis_ss.subsurface((i * 31, 0), (31, 24))
            mbis_i = pygame.transform.scale(mbis_i, (31*3.2, 24*3.2))
            self.mega_idle_shoot_image.append(mbis_i)

        



        self.ind = 0

        if self.walking == True and self.idle == False:
            if self.direction == "RIGHT":
                if self.jump == True:
                    self.image = self.mega_jump_image[self.ind]
                else:
                    self.image = self.mega_bw_images[self.ind]
            elif self.direction == "LEFT":
                if self.jump == True:
                    self.image = self.mega_jump_rev_image[self.ind]
                else:
                    self.image = self.mega_bw_rev_images[self.ind]

        elif self.walking == False and self.idle == True:
            if self.direction == "RIGHT":
                if self.jump == True:
                    self.image = self.mega_jump_image[self.ind]
                else:
                    if self.shoot:
                        self.image = self.mega_idle_shoot_image[self.ind]
                    else:
                        self.image = self.mega_bi_images[self.ind]
            elif self.direction == "LEFT":
                if self.jump == True:
                    self.image = self.mega_jump_rev_image[self.ind]
                else:
                    self.image = self.mega_bi_rev_images[self.ind]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.mbrect = self.mega_buster_image.get_rect()
        self.mbrect.topleft = (100, 100)

    def update(self):

        if self.idle and not self.walking:
            self.ind += 0.02
        elif self.walking and not self.idle:
            self.ind += 0.13
            #self.ind += 0.01



        self.vy += index.gravity
        self.y += self.vy
        
        if self.idle or self.walking:
            if self.jump or self.shoot:
                if self.ind >= 1:
                    self.ind = 0
            else:
                if self.ind >= 3:
                    self.ind = 0

        if self.walking == True and self.idle == False:
            if self.direction == "RIGHT":
                if self.jump == True:
                    self.image = self.mega_jump_image[int(self.ind)]
                else:
                    self.image = self.mega_bw_images[int(self.ind)]
            elif self.direction == "LEFT":
                if self.jump == True:
                    self.image = self.mega_jump_rev_image[int(self.ind)]
                else:
                    self.image = self.mega_bw_rev_images[int(self.ind)]

        elif self.walking == False and self.idle == True:
            if self.direction == "RIGHT":
                if self.jump == True:
                    self.image = self.mega_jump_image[int(self.ind)]
                else:
                    if self.shoot:
                        self.image = self.mega_idle_shoot_image[int(self.ind)]
                    else:
                        self.image = self.mega_bi_images[int(self.ind)]
            elif self.direction == "LEFT":
                if self.jump == True:
                    self.image = self.mega_jump_rev_image[int(self.ind)]
                else:
                    self.image = self.mega_bi_rev_images[int(self.ind)]

        self.rect.topleft = (self.x, self.y)
