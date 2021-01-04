from OpenGL.GLU import *
import OpenGL.GLUT as glut
from Box import *
from Human import *
from Dog import *
import math as m
from MapTexture import *
import pygame
windowX = 1920
windowY = 1080
stopTime = 2.0
boxCordinate = []
boxList = []
def init():
    global boxCordinate
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/background-sounds.mp3'))
    pygame.mixer.Channel(0).set_volume(0.04)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/walk-human.mp3'))
    pygame.mixer.Channel(1).set_volume(0.8)
    pygame.mixer.Channel(1).stop()
    pygame.mixer.Channel(4).play(pygame.mixer.Sound('assets/sounds/dog1.mp3'))
    pygame.mixer.Channel(4).set_volume(0.8)
    pygame.mixer.Channel(4).stop()
    for i in range(0,6):
        boxCordinate.append([random.randint(-300,300),random.randint(-300,300)])
class PlusBox():
    hide = False
    plusBoxCordinateX = random.randint(-300,300)
    plusBoxCordinateY = random.randint(-300, 300)
    x1 = 0
    x2 =0
    z1 =0
    z2 =0
    def NewCordinate(self):
        self.plusBoxCordinateX = random.randint(-100, 100)
        self.plusBoxCordinateY = random.randint(-100, 100)
class Tus():
    keyW = False
    keyA = False
    keyD = False
class Human():
    sagBacakAngle = 0
    solBacakAngle = 0
    durum = 0
    humanSpace = 0
    humanSpaceControl = False
    angleY = 0.05
    topxPos = 0.0
    topzPos = 1.0
    directionX = 0.0
    directionZ = -1.0
    hareket = False
    engelVar = False
    carpismaSayisi =0


class Dog():
    sagBacakAngle = 0
    solBacakAngle = 0
    kuyruk = 0
    durum = 0
    hiz = 6.0
    hareket = False

class Camera():
    angleY = 0.05
    directionX = 0.0
    directionZ = -1.0
    directionXmouse = 0.0
    directionZmouse = 0.0
    directionYmouse = 0.0
    directionY = 0
    xPos = 0.0
    zPos = -5.0
    yPos = 8.0
    zoom = 0.2
    mouse_x = 0
    mouse_y = 0
    mouse_left = 1

plusBox = PlusBox()
tus = Tus()
camera = Camera()
human = Human()
dog = Dog()
MAIN_MENU_SCREEN = 0
GAME_SCREEN = 1
PAUSE_MENU_SCREEN = 2
CurrentScreen = MAIN_MENU_SCREEN
def changeScreen():
    global CurrentScreen
    if CurrentScreen == MAIN_MENU_SCREEN:
        return MainMenu()
    elif CurrentScreen == GAME_SCREEN:
        return display()
    elif CurrentScreen == PAUSE_MENU_SCREEN:
        return PauseMenu()

def MainMenu():
    print("Main Menu")
    pygame.mixer.Channel(0).pause()
    #glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(-5,-5,0)
    glActiveTexture(GL_TEXTURE0)
    LoadTextures("assets/main-menu.png")
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex2f(0.0, 0.0)
    glTexCoord2f(0.0, 0.0), glVertex2f(0.0, 10.0)
    glTexCoord2f(1.0, 0.0), glVertex2f(10.0,10.0)
    glTexCoord2f(1.0, 1.0), glVertex2f(10.0, 0.0)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glutSwapBuffers()

def PauseMenu():
    print("Pause Menu")
    pygame.mixer.Channel(0).pause()
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glDepthFunc(GL_LESS)
    #glEnable(GL_DEPTH_TEST)
    #glMatrixMode(GL_MODELVIEW)
    #glShadeModel(GL_SMOOTH)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5, 5, -5, 5)
    #glMatrixMode(GL_MODELVIEW)

    glPushMatrix()
    glTranslatef(-5, -5, 0)
    glActiveTexture(GL_TEXTURE0)
    LoadTextures("assets/pause-menu.png")
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0), glVertex2f(0.0, 0.0)
    glTexCoord2f(0.0, 0.0), glVertex2f(0.0, 10.0)
    glTexCoord2f(1.0, 0.0), glVertex2f(10.0, 10.0)
    glTexCoord2f(1.0, 1.0), glVertex2f(10.0, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0,1,0)
    glTranslatef(1,-3,0)
    textWrite("BİLALLL")
    glPopMatrix()


    glutSwapBuffers()

def textWrite(string):
    glRasterPos3f(0, 0, 0)
    for i in string:
        glutBitmapCharacter(glut.GLUT_BITMAP_9_BY_15, ord(i))

def display():
    global camera,dog,human,boxCordinate, boxList,plusBox
    pygame.mixer.Channel(0).unpause()
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 8.0 / 4.0, 1, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera.xPos, camera.yPos, camera.zPos, camera.xPos + camera.directionX + camera.directionXmouse,
              camera.yPos - camera.zoom + camera.directionY-0.18 + camera.directionYmouse,
              camera.zPos + camera.directionZ + camera.directionZmouse, 0, 1, 0)
    mapTexture(300, 100, 300)
    getDog(camera,dog,human)
    keyControl()
    plusBox.x1, plusBox.x2, plusBox.z1, plusBox.z2 = getBox(2, 2, 2, plusBox.plusBoxCordinateX, 1,
                                                            plusBox.plusBoxCordinateY, 1, 0, 0)
    if plusBox.hide==False:
        plusBox.hide = True
        plusBox.NewCordinate()
    for i in range(0,6):
        boxList.append(getBox(5,5,5,boxCordinate[i][0],2.5,boxCordinate[i][1],0,1,0))
    getHuman(camera, human, boxList,plusBox)
    glutSwapBuffers()

def keyControl():
    global camera,human,tus
    if(human.engelVar == False):
        if tus.keyW == True:
            if pygame.mixer.Channel(1).get_busy():
                pass
            else:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/walk-human.mp3'))
            camera.xPos += camera.directionX
            camera.zPos += camera.directionZ
            camera.yPos += camera.directionY
        elif(tus.keyA):
            human.angleY -= 0.1
        elif(tus.keyD):
            human.angleY +=0.1
def keyUp(*args):
    global  tus
    if args[0] == b"a":
        tus.keyA = False
    elif args[0] == b"d":
        tus.keyD = False
    elif args[0] == b"w":
        pygame.mixer.Channel(1).stop()
        if (human.engelVar == True):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/sounds/carpma.mp3'))
        human.hareket = False
        tus.keyW = False
    elif args[0] == b" ":
        pass

    glutPostRedisplay()

def keyPressed(*args):
    global camera, human,tus,CurrentScreen
    if args[0] == b'\r':
        CurrentScreen = GAME_SCREEN
    elif args[0] == b"p":
        CurrentScreen = PAUSE_MENU_SCREEN

    if args[0] == b"\x1b":
        glutDestroyWindow(b"Followww")
    if args[0] == b"a":
        tus.keyA =True
    elif args[0] == b"d":
        tus.keyD = True
    elif args[0] == b"w":
        human.hareket = True
        tus.keyW = True
    elif args[0] == b"s":
        human.engelVar = False
        camera.xPos -= camera.directionX
        camera.zPos -= camera.directionZ
        camera.yPos -= camera.directionY

    elif args[0] == b" ":
        if (human.humanSpace == 0):
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('assets/sounds/jump.mp3'))
            human.humanSpaceControl = True

    glutPostRedisplay()

def mouse(button, state, x, y):
    global camera
    if GLUT_LEFT_BUTTON == 0:
        if GLUT_DOWN == 0:
            camera.mouse_left = 1
        if GLUT_UP == 0:
            camera.mouse_left = 0


def mouseMotion(x, y):
    global camera,human
    if(human.engelVar == False):
        if (camera.mouse_x == 0):
            camera.mouse_x = x
            if (x > windowX / 2):
                camera.angleY += 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
            else:
                camera.angleY -= 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
        if (x > 1800):
            camera.mouse_x = x
            camera.angleY += 0.1
            camera.directionX = m.sin(camera.angleY)
            camera.directionZ = -m.cos(camera.angleY)
        if (x < 100):
            camera.mouse_x = x
            camera.angleY -= 0.1
            camera.directionX = m.sin(camera.angleY)
            camera.directionZ = -m.cos(camera.angleY)
        else:
            if (x > camera.mouse_x):
                camera.angleY += 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
            else:
                camera.angleY -= 0.03
                camera.directionX = m.sin(camera.angleY)
                camera.directionZ = -m.cos(camera.angleY)
            camera.mouse_x = x


def MouseWheel(*args):
    global camera
    if args[1] == -1:
        if (camera.yPos > 3):
            camera.yPos -= 0.1
    elif args[1] == 1:
        if (camera.yPos < 9):
            camera.yPos += 0.1
    else:
        pass
    print(camera.yPos)
    glutPostRedisplay()

def main():
    init()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(windowX, windowY)
    glutInitWindowPosition(0, 0)
    glutIdleFunc(changeScreen)
    glutCreateWindow(b"Followw")
    glutDisplayFunc(changeScreen)
    glutIdleFunc(changeScreen)
    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyUp)
    glutMouseWheelFunc(MouseWheel)
    glutMouseFunc(mouse)
    glutPassiveMotionFunc(mouseMotion)
    glutMainLoop()
    glEnable(GL_DEPTH_TEST)

main()
