import pygame


pygame.init() # запускаем pygame

win = pygame.display.set_mode((500, 500)) # создаем окно и задаем ему размеры в px

pygame.display.set_caption("Pygame start") # даем окну название

# задаем координаты нашему объекту
x = 50
y = 50
# задаем размеры нашего объекта
width = 40
height = 37
# задаем скорость передвижения нашего объекта
speed = 5

# создаем прыжок
isJump = False
jumpCount = 5

# загружаем изображения

walkRight = [pygame.image.load('png/walk_right_1.png'), pygame.image.load('png/walk_right_2.png'),
             pygame.image.load('png/walk_right_3.png'), pygame.image.load('png/walk_right_4.png'),
             pygame.image.load('png/walk_right_5.png'), pygame.image.load('png/walk_right_6.png')]



walkLeft = [pygame.image.load('png/walk_left_1.png'), pygame.image.load('png/walk_left_2.png'),
            pygame.image.load('png/walk_left_3.png'), pygame.image.load('png/walk_left_4.png'),
            pygame.image.load('png/walk_left_5.png'), pygame.image.load('png/walk_left_6.png')]


playerStand = pygame.image.load('png/idle (1).png')

# двигается ли он? и в какую сторону
left = False
right = False
animCount = 0

def drawWindow():
    global animCount

    win.fill((255, 255, 255))  # а тут в конце мы просто делаем фон

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount//5], (x,y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))


    # если у нас есть кастомный фон, то
    # win.blit(bg, (0,0 )), где bg - это наш фон, а (0,0) место откуда начать рисовать

    pygame.display.update()  # обновляет окно


run = True # переменная которая обозначает должна ли программа сейчас работать
while run:
    pygame.time.delay(30) # через какой промежуток времени цикл повторяется: чем меньше => тем лучше


    # все события в pygame находятся в одном массиве
    # и чтобы задействовать их, нам нужно постоянно перебирать массив
    # и искать нужное нам действие(мог понять неправильно)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # если пользователь закрывает окно программы
            run = False # то мы говорим, что дальше выполнять цикл не надо

    # учим наш квадрат двигатся
    keys = pygame.key.get_pressed() # получаем кнопки, которые были нажаты
    # как я понял тут мы проверяем есть ли в списке нужная
    # кнопка, и если есть, то двигаем квадрат
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    # при добавлении границ важно понимать, что отсчет у всего идет с левого верхнего угла
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -5:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 5

    # код для прыжка
    # Прыжок является параболлой, поэтому состоит из
    # повышение и падение
    # падение начинается на середине прыжка, поэтому мы ждем
    # когда jumpCount станет на середине своего диапазона
    # и начинаем опускать
    drawWindow()

pygame.quit() # закрывает собственно окно