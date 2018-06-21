import keyboard

from pyglet import window
from pyglet.gl import *

from time import sleep


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)    #sets background color to black
    global q                            #creates global variable q
    q = gluNewQuadric();                #creates a ref to which all objcets must be bound
    glEnable(GL_DEPTH_TEST)             #enables depth comparison and updates the depth buffer
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)   #activates gl polygon mode


def resize(width, height):              #makes sure you are able to see the planets
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)         #specifies projection as the current matrix
    glLoadIdentity()                    #replaces current matrix with the identity matrix
    gluPerspective(zoom, 1 * width / height, 0.1, 100.0)    #the perspective from which you start watching
    glMatrixMode(GL_MODELVIEW)          #specify modelviuw is the current matrix


def sphere(speed,distance,c1,c2,c3,corners,lines, diameter):    #speed = times a year it makes a full cycle
    distance /= 100                                             #scaling distance and diameter for better vieuwing options
    diameter /= 100                                             #1 year = 10 secs
    glRotatef((speed * t) % 360, 0, 1, 0)                       #rotates the matrix so the planet actually has an orbit
    glTranslatef(distance, 0, 0)                                #translates the planet from the sun/planet by the distance it has from the sun/planet
    glColor3f(c1, c2, c3)                                       #gives the planet a color
    gluSphere(q, diameter, corners, lines)                      #creates the planet with the corrisponding size


def mydisplay():
    global t
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(eyeX, eyeY, eyeZ,  # eye
              0.0, 0.0, 0.0,  # center
              0.0, 1, 0.0)  # up

    sphere(0,0,1,1,0,20,12,25)          #Sun ordia 1319


    glPushMatrix()
    sphere(1/0.2,146,1,0.8,0,18,12,5)       #Mercury
    #sphere(1,0.3,1,1,1,12,20,0.1)
    glPopMatrix()

    glPushMatrix()
    sphere(1/0.6,207,1,0,0.5,18,12,12)  #Venus
    glPopMatrix()
#speed,distance,c1,c2,c3,corners,lines, diameter
    glPushMatrix()
    sphere(1,247,0,0.5,1,18,12,13)      #Earth
    sphere(12,25,0.8,0.8,0.8,18,12,3)   #Moon
    glPopMatrix()

    glPushMatrix()
    sphere(1/1.9, 305, 1, 0, 0, 18, 12, 7)  # Mars
    sphere(289, 23, 0.8,0.8,0.8, 18, 12, 3) #Deimos
    sphere(1168, 6, 0.8,0.8,0.8, 18, 12, 3) #Phobos
    glPopMatrix()

    glPushMatrix()
    sphere(1/11.9, 441, 1, 1, 0.5, 18, 12, 20)  # Jupiter ordis741  ordia142
    glPopMatrix()

    glPushMatrix()
    sphere(1/29.5, 550, 0, 0, 0.5, 18, 12, 19)  # Saturn ordis1350
    glPopMatrix()

    glPushMatrix()
    sphere(1/84, 650, 0.5, 1, 0.5, 18, 12, 15)  # Uranus ordis2750
    glPopMatrix()

    glPushMatrix()
    sphere(1/164.8, 750, 0.8, 0, 0.5, 18, 12, 15)  # Neptune ordis4450
    glPopMatrix()


def keyHandle(eyeX, eyeY, eyeZ):
    if keyboard.is_pressed('a'):
        if eyeZ >= 0 and eyeX >= 0:
            eyeX += 0.1
            eyeZ -= 0.1
        elif eyeZ >= 0 and eyeX < 0:
            eyeX += 0.1
            eyeZ += 0.1
        elif eyeZ < 0 and eyeX >= 0:
            eyeZ -= 0.1
            eyeX -= 0.1
        elif eyeZ < 0 and eyeX < 0:
                eyeZ += 0.1
                eyeX -= 0.1
    if keyboard.is_pressed('d'):
        if eyeZ >= 0 and eyeX >= 0:
            eyeX -= 0.1
            eyeZ += 0.1
        elif eyeZ >= 0 and eyeX < 0:
            eyeX -= 0.1
            eyeZ -= 0.1
        elif eyeZ < 0 and eyeX >= 0:
            eyeZ += 0.1
            eyeX += 0.1
        elif eyeZ < 0 and eyeX < 0:
            eyeZ -= 0.1
            eyeX += 0.1
    if keyboard.is_pressed('w'):
        eyeY += 0.1
    if keyboard.is_pressed('s'):
        eyeY -= 0.1
    if keyboard.is_pressed('q'):
        if eyeZ < 0:
            eyeZ += 0.1
        else:
            eyeZ -= 0.1
        if eyeX < 0:
            eyeX += 0.1
        else:
            eyeX -= 0.1
        if eyeY < 0:
            eyeY += 0.1
        else:
            eyeY -= 0.1
        print (eyeX,eyeZ)
    if keyboard.is_pressed('e'):
        if eyeZ >= 0 and eyeX >= 0:
            eyeX += 0.1
            eyeZ += 0.1
        elif eyeZ >= 0 and eyeX < 0:
            eyeX -= 0.1
            eyeZ += 0.1
        elif eyeZ < 0 and eyeX >= 0:
            eyeZ -= 0.1
            eyeX += 0.1
        elif eyeZ < 0 and eyeX < 0:
            eyeZ -= 0.1
            eyeX -= 0.1
    return eyeX,eyeY,eyeZ


def main():
    win = window.Window()
    global zoom
    zoom = 135
    win.on_resize = resize
    init()

    global t
    t = 0.0
    speed = 0.6
    global eyeX
    eyeX = 0.0
    global eyeY
    eyeY = -2.0
    global eyeZ
    eyeZ = -4.0
    global vieuwCircle
    vieuwCircle = 2

    while not win.has_exit:
        eyeX, eyeY, eyeZ = keyHandle(eyeX, eyeY, eyeZ)
        win.on_resize = resize
        win.dispatch_events()
        mydisplay()
        win.flip()
        t += speed
        sleep(0.01)


if __name__ == "__main__":
    main()