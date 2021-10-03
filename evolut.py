import pygame
import random
import time



win = pygame.display.set_mode((1650, 850))
run = True
animals = [[[20, 19], 1, 5, 0, 5, 5, 0], [[30, 25], 2, 3, 0, 5, 5, 1], [[5, 25], 3, 2, 0, 5, 5, 1]]  # pole 50x38
food = []
point = 0

show = 0
for n in range(0, random.randint(45, 55)):
    food.append([random.randint(0, 49), random.randint(0, 37)]) 


def run(pos1, pos2):
    if pos1[1] < pos2[1]:
        if not pos2[1] > 30:
            return [0, 1]
        else:
            if pos1[0] < pos2[0]:
                return [1, 0]

            else:
                return [-1, 0]
    elif pos1[1] > pos2[1]:
        if not pos2[1] > 8:
            return [0, -1]
        else:
            if pos1[0] < pos2[0]:
                return [1, 0]

            else:
                return [-1, 0]
    elif pos2[0] > pos1[0]:
        if not pos2[0] > 42:
            return [1, 0]
        else:
            if pos1[1] < pos2[1]:
                return [0, 1]

            else:
                return [0, -1]
    else:
        if not pos2[0] < 8:
            return [-1, 0]
        else:
            if pos1[0] < pos2[0]:
                return [0, 1]

            else:
                return [0, -1]

        


def bot(player):
    global animals
        
    for n in animals:
        if n[2] > animals[player][2] and n[6] == 0:
            if n[0][1] - animals[player][0][1] < 7 and n[0][1] - animals[player][0][1] > -7 and n[0][0] - animals[player][0][0] < 7 and n[0][0] - animals[player][0][0] > -7:
                
                animals[player][0][0] += run(n[0], animals[player][0])[0] #
                animals[player][0][1] += run(n[0], animals[player][0])[1] #
                return 1

        elif n[2] < animals[player][2] and 1 != animals[player][6] == n[6]:
            if n[0][1] - animals[player][0][1] < 7 and n[0][1] - animals[player][0][1] > -7 and n[0][0] - animals[player][0][0] < 7 and n[0][0] - animals[player][0][0] > -7:
                animals[player][0][0] += run(n[0], animals[player][0])[0]*-1 #
                animals[player][0][1] += run(n[0], animals[player][0])[1]*-1 #
                return 1

    if [animals[player][0][0], animals[player][0][1]] in food:
        food.pop(food.index([animals[player][0][0], animals[player][0][1]]))
        animals[player][3] += 1

    for n in range(0, 60):
        i = [n-1, 0-1]
        k1 = 1
        k2 = 1
        for n1 in range(n*4):

            
            i[0] += k1
            i[1] += k2
            if i[0] == n*2:
                k1 = -1
            elif i[1] == n*2:
                k2 = -1
            elif i[0] == 0:
                k1 = 1

            if [animals[player][0][0]+i[0]-n, animals[player][0][1]+i[1]-n] in food:

                if animals[player][0][0]+i[0]-n < animals[player][0][0]:
                    animals[player][0][0] -= 1 #
                    return False

                elif animals[player][0][0]+i[0]-n > animals[player][0][0]:
                    animals[player][0][0] += 1 #
                    return False

                elif animals[player][0][1]+i[1]-n > animals[player][0][1]:
                    animals[player][0][1] += 1 #
                    return False
                else:
                    animals[player][0][1] -= 1 #
                    return False


while run:
    pygame.draw.rect(win, (192,192,192), (0, 0, 1680, 850))
    pygame.draw.rect(win, (0, 0, 114), (600, 50, 1000, 760))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for animal in animals:
        pygame.draw.rect(win, (20* animal[2], 10* animal[1], 0), (600 + animal[0][0]*20, 50 + animal[0][1]*20, 20, 20))



    for n in food:
        pygame.draw.circle(win, (50, 160, 20), (600 + n[0]*20+10, 50 + n[1]*20+10), 10)
    if len(animals) > 10:
        print(animals[5])
    if show == 1:
        show = 0
        for animal in range(len(animals)):
            for n in range(animals[animal][1]):
                bot(animal)
        stop = False
        for n in range(len(animals)):
            for n1 in range(len(animals)):
                if not n == n1 and not stop:
                    if animals[n][0][0] == animals[n1][0][0] and animals[n][0][1] == animals[n1][0][1]:
                        if animals[n][2] > animals[n1][2]:
                            animals[n][3] += animals[n1][3]
                            animals.pop(n1)
                            stop = True
                        elif animals[n][2] < animals[n1][2]:
                            animals[n1][3] += animals[n][3]
                            animals.pop(n)
                            stop = True

    for animal in range(len(animals)):
        if animals[animal][0][0] < 0:
            animals[animal][0][0] = 0
        elif animals[animal][0][0] > 49:
            animals[animal][0][0] = 49
        if animals[animal][0][1] < 0:
            animals[animal][0][1] = 0
        if animals[animal][0][1] > 37:
            animals[animal][0][1] = 37

    if not food:
        point = 3
        l = len(animals)
        
        for n in range(l):
            while animals[n][3] > animals[n][4]:
                ap = animals[n]
                animals.append([[   animals[n][0][0]   , animals[n][0][1]     ], animals[n][1], animals[n][2], animals[n][3], animals[n][4], animals[n][5], animals[n][6]])
                animals[n][3] -= animals[n][4]
            animals[n][3] = 0

    
        for animal in range(len(animals)):
            animals[animal][3] = 0
            ranx = random.randint(1, 48)
            rany = random.randint(1, 36)
            print(ranx, rany)
            animals[animal][0][0] = ranx
            animals[animal][0][1] = rany
            print(animals[animal][0][0], animals[animal][0][1])

        for n in range(0, random.randint(45, 55)):
            food.append([random.randint(0, 49), random.randint(0, 37)])

    


    pygame.display.update()
    show+=1
    time.sleep(0.1)
pygame.quit