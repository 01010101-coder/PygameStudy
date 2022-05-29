import pygame

pygame.init() # запускаем pygame

win = pygame.display.set_mode((500, 500)) # создаем окно и задаем ему размеры в px

pygame.display.set_caption("Pygame start") # даем окну название

# задаем координаты нашему объекту
x = 50
y = 50
# задаем размеры нашего объекта
width = 40
height = 60
# задаем скорость передвижения нашего объекта
speed = 5

run = True # переменная которая обозначает должна ли программа сейчас работать
while run:
    pygame.time.delay(30) # частота обновления программы(fps)

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
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed


    win.fill((0, 0, 0)) # а тут в конце мы просто делаем фон
    # снова черным, чтобы квадрат не оставлял следов
    # честно говоря весьма топорный способ и мне кажется есть по лучше
    pygame.draw.rect(win, (255,255,255), (x, y, width, height)) # рисуем наш объект, в данном случае квадрат
    # в начале идет, где мы его рисуем(наше окно), потом какого цвета(белый), а дальше его параметры(местоположение, размеры)
    pygame.display.update() # обновляет окно


pygame.quit() # закрывает собственно окно