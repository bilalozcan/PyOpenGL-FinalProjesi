import random

import pygame

from RectangularPrism import *
def getDog(camera,dog,human,game):
    dog.hareket =True
    rand = random.randint(0, 1)
    if(dog.hiz>6):
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('assets/sounds/dog1.mp3'))
    if dog.hiz >= 13 and dog.hiz < 14.1 and game.end != True:
        game.end = True
    elif (human.carpismaSayisi > 100):
        dog.hiz += 0.5
    elif (human.carpismaSayisi > 80):
        dog.hiz += 0.1
    elif (human.carpismaSayisi > 50):
        dog.hiz += 0.05
    elif (human.carpismaSayisi > 20):
        dog.hiz += 0.005
    elif(human.carpismaSayisi == 0):
        dog.hiz = 4

    glPushMatrix()
    glTranslatef(0, 1, 0)
    glTranslatef(camera.xPos + dog.hiz * camera.directionX, 0, (camera.zPos) + dog.hiz * camera.directionZ)
    glRotatef(-57.5 * (camera.angleY), 0, 1, 0)
    DogKosmaDurum(dog)
    drawDog(dog)
    glPopMatrix()

def DogKosmaDurum(dog):
    if(dog.hareket == True):
        if (dog.durum == 0):
            dog.sagBacakAngle += dog.hiz/2
            dog.solBacakAngle -= dog.hiz/2
            dog.kuyruk +=dog.hiz
            if (dog.sagBacakAngle > 40):
                dog.durum = 1
        elif (dog.durum == 1):
            dog.sagBacakAngle -= dog.hiz/2
            dog.solBacakAngle += dog.hiz/2
            dog.kuyruk -= dog.hiz
            if (dog.sagBacakAngle < -40):
                dog.durum = 0
    else :
        dog.kuyruk = 0
        dog.sagBacakAngle = 0
        dog.solBacakAngle = 0

def drawDog(dog):
    # GÖVDE
    glPushMatrix()
    glColor3f(0.37, 0.18, 0)
    RectangularPrism(0.312, 0.312, 1)
    glPopMatrix()

    # KAFA
    glPushMatrix()
    glTranslatef(0, 0, -0.4)
    glColor3f(0.20, 0.188, 0)
    RectangularPrism(0.4, 0.4, 0.4)
    glPopMatrix()

    # SAĞ KULAK
    glPushMatrix()
    glTranslatef(0.2, 0.4, -0.9)
    glColor3f(0, 0.45, 0)
    RectangularPrism(0.1, 0.1, 0.03)
    glPopMatrix()

    # SOL KULAK
    glPushMatrix()
    glTranslatef(-0.2, 0.4, -0.9)
    glColor3f(0, 0.45, 0)
    RectangularPrism(0.1, 0.1, 0.03)
    glPopMatrix()

    # SAĞ GÖZ
    glPushMatrix()
    glTranslatef(0.15, 0.18, -1)
    glColor3f(0, 0, 0)
    RectangularPrism(0.05, 0.05, 0.03)
    glPopMatrix()

    # SOL GÖZ
    glPushMatrix()
    glTranslatef(-0.15, 0.18, -1)
    glColor3f(0, 0, 0)
    RectangularPrism(0.05, 0.05, 0.03)
    glPopMatrix()

    # BURUN
    glPushMatrix()
    glTranslatef(0, -0.15, -1.08)
    glColor3f(0.77, 0.77, 0.77)
    RectangularPrism(0.165, 0.165, 0.165)
    glPopMatrix()

    # AĞIZ
    glPushMatrix()
    glTranslatef(0, -0.2, -1.25)
    glColor3f(0.7, 0, 0)
    RectangularPrism(0.12, 0.05, 0.03)
    glPopMatrix()

    # SOL ÖN AYAK
    glPushMatrix()
    glTranslatef(-0.18, -0.7, -0.4)
    glRotatef(dog.solBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SAĞ ÖN AYAK
    glPushMatrix()
    glTranslatef(0.18, -0.7, -0.4)
    glRotatef(dog.sagBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SOL ARKA AYAK
    glPushMatrix()
    glTranslatef(-0.18, -0.7, 0.8)
    glRotatef(dog.sagBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # SAĞ ARKA AYAK
    glPushMatrix()
    glTranslatef(0.18, -0.7, 0.8)
    glRotatef(dog.solBacakAngle, 1, 0, 0)
    glColor3f(0.5, 0, 0)
    RectangularPrism(0.12, 0.47, 0.12)
    glPopMatrix()

    # KUYRUK
    glRotatef(dog.kuyruk, 0, 0, 1)
    glPushMatrix()
    glTranslatef(0.045, -0.25, 1.3)
    glRotatef(45,1,0,0)
    glColor3f(0, 0, 0.3)
    RectangularPrism(0.12, 0.12, 0.6)
    glPopMatrix()

