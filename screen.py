import pygame
from random import randint
from math import sqrt
from sklearn.cluster import KMeans
def distance(a,b):
    return sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))

pygame.init()

running = True
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("K means-Python")
clock = pygame.time.Clock()
#colors
color_background = (214, 214, 214)
black = (0, 0, 0)
background_panel = (249, 255, 230)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
maroon = (128, 0, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
pink = (255, 0, 255)
teal = (0, 128, 128)
orange = (255, 165, 0)
plum = (255, 165, 0)
navy = (0, 0, 128)
colors = [plum, red, blue, green, maroon, yellow, purple, pink, teal, navy, orange]
font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 15)
text_plus = font.render('+', True, white)
text_diff = font.render('-', True, white)
text_run = font.render('RUN', True, white)
text_random = font.render('RANDOM', True, white)
text_algorithm = font.render('ALGORITHM', True, white)
text_reset = font.render('RESET', True, white)

K = 0
ERROR = 0
points = []
clusters = []
label = []

while running:
    clock.tick(30)
    screen.fill(color_background)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    #draw interface
    #draw panel
    pygame.draw.rect(screen, black, (50, 50, 700, 500))
    pygame.draw.rect(screen, background_panel, (52, 52, 696, 496))

    #draw button K
    pygame.draw.rect(screen, black, (850, 50, 50, 50))
    screen.blit(text_plus, (860, 50))
    pygame.draw.rect(screen, black, (950, 50, 50, 50))
    screen.blit(text_diff, (960, 50))

    #draw button run
    pygame.draw.rect(screen, black, (850, 150, 200, 50))
    screen.blit(text_run, (900, 150))

    #draw button random
    pygame.draw.rect(screen, black, (850, 230, 200, 50))
    screen.blit(text_random, (900, 230))

    #draw button algorithm
    pygame.draw.rect(screen, black, (850, 400, 200, 50))
    screen.blit(text_algorithm, (850, 400))

    #draw button reset
    pygame.draw.rect(screen, black, (850, 500, 200, 50))
    screen.blit(text_reset, (900, 500))

    #draw K
    text_k = font.render("K = " + str(K), True, black)
    screen.blit(text_k, (1050, 50))

    #draw error
    text_err = font.render("ERROR = " + str(int(ERROR)), True, black)
    screen.blit(text_err, (850, 300))

    #mouse position
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_pos = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")", True, black)
        screen.blit(text_pos, (mouse_x + 10, mouse_y))

    #end draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_x >= 850 and mouse_x <= 900 and 50 <= mouse_y <= 100:
                if K < 10:
                    K += 1
                else:
                    continue
            if mouse_x >= 950 and mouse_x <= 1000 and mouse_y >= 50 and mouse_y <= 100:
                if K > 0:
                    K -= 1
                print("Diff")
            if mouse_x >= 850 and mouse_x <= 1050 and mouse_y >= 150 and mouse_y <= 200:
                if clusters==[]:
                    continue
                label.clear()
                for q in points:
                    min_distance = 9999999999999
                    index_min=0
                    for i in clusters:
                        if distance(q,i) < min_distance:
                            index_min=clusters.index(i)
                            min_distance = distance(q,i)
                    label.append(index_min)
                #update cluster
                for i in range(K):
                    new_x=0
                    new_y=0
                    count=0
                    for j in range(len(label)):
                        if label[j] == i:
                            new_x+=points[j][0]
                            new_y+=points[j][1]
                            count+=1
                    if(count!=0):
                        clusters[i]=[new_x/count,new_y/count]
                #update Error
                ERROR =0
                for i in range(K):
                    for j in range(len(label)):
                        if label[j] == i:
                            ERROR+=distance(clusters[i],points[j])
                print("run")
            if mouse_x >= 850 and mouse_x <= 1050 and mouse_y >= 230 and mouse_y <= 280:
                label.clear()
                clusters.clear()
                for i in range(K):
                    random_point = [randint(0, 700), randint(0, 500)]
                    clusters.append(random_point)
                print("Random")
            if mouse_x >= 850 and mouse_x <= 1050 and mouse_y >= 400 and mouse_y <= 450:
                try:
                    kmeans = KMeans(n_clusters=K).fit(points)
                    label = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_

                except:
                    print("error")
                print("Algorithm")
            if mouse_x >= 850 and mouse_x <= 1050 and mouse_y >= 500 and mouse_y <= 550:
                K = 0
                ERROR=0
                points.clear()
                clusters.clear()
                print("reset")
            #  point in panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                label= []
                point = [mouse_x - 50, mouse_y - 50]
                points.append(point)
    # draw cluster
    print(clusters)
    labels=[]
    for i in label:
        labels.append(i)
    tmp_clusters=[]
    for i in clusters:
        pass
    for i in range(len(clusters)):
        pygame.draw.circle(screen, colors[i], (clusters[i][0] + 50, clusters[i][1] + 50), 7)
        pygame.draw.circle(screen, black, (clusters[i][0] + 50, clusters[i][1] + 50), 4)
    # draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, black, (points[i][0] + 50, points[i][1] + 50), 5)
        if labels == []:
            pygame.draw.circle(screen, white, (points[i][0] + 50, points[i][1] + 50), 4)
        else :
            pygame.draw.circle(screen, colors[labels[i]], (points[i][0] + 50, points[i][1] + 50), 4)
    pygame.display.flip()
