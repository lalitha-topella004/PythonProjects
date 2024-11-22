import pygame #pygame anedhi oka module adhi manam pip install pygame ani cmd prompt lo cheyyali
import random # endukante manam food ni random ga import chesthamu kabatti
#pygame ni call cheyyali adhi manam init method tho chesthamuu
pygame.init() #init anedhi python lo oka constructor manam init ani ivvagane adhi call avthundhi so ikkada manam pygame tho
              #paatu isthunnam kabatti automatic ga pygame anedhi call avthindhi

width,height = 600,600 #snake dabba yokka size and height
game_screen = pygame.display.set_mode((width,height)) #coordinates ivvali so manaki ikkada width and height avthai
pygame.display.set_caption("Welcome to my snake game") #manaki starting kavalsina game caption kosam

#ikkada manam snake coordinates isthunnam
snake_x,snake_y = width/2,height/2
#entha variables tho move avvali anedhi manam create cheskuntam
change_x,change_y = 0,0

food_x,food_y = random.randrange(0,width)//10*10 , random.randrange(0,height)//10*10

clock = pygame.time.Clock() #clock module pygame anedhi isthundhi manaki

snake_body = [(snake_x,snake_y)]

def display_snake_and_food(): #and food ani endukuu icham antey manam akkada food and snake ni kuda dispaly chesthunnam kababti

    global snake_x,snake_y,food_x,food_y
    snake_x = (snake_x + change_x)%width
    snake_y = (snake_y + change_y) % height  #coordinates change cheyyali kabatti defined from line 30 to line 40 

    if((snake_x,snake_y) in snake_body[1:]):
        print("GAME OVER!!")
        quit()

    snake_body.append((snake_x,snake_y)) #okate append chestham kabatti dhanni  manam tuple lo pedatham

    if (food_x == snake_x  and food_y == snake_y):
        food_x,food_y = random.randrange(0,width)//10*10 , random.randrange(0,height)//10*10
    else:
        del snake_body[0]


    game_screen.fill((0,0,0))
    pygame.draw.rect(game_screen,(0,255,0),[food_x,food_y,10,10]) #color we are changing to differentiate the food and the snake

    for (x,y) in snake_body:
        pygame.draw.rect(game_screen,(255,255,255),[x,y,10,10]) #snake ni draw chesam kabatti paina line lo food ni kuda draw  chestham
    pygame.display.update() #update chesthey ne manaki display avthundhi

while True:
    events = pygame.event.get() #prathisari manaki edhokati call avvali kabatti
    for event in events: #for specific tasks on events
        if(event.type==pygame.QUIT):
            pygame.QUIT
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                change_x = -10 #because the snake thickness is 10 mentioned in line number 17
                change_y = 0
            elif(event.key == pygame.K_RIGHT):
                change_x = 10
                change_y = 0
            elif(event.key == pygame.K_UP):
                change_x = 0
                change_y = -10
            elif(event.key == pygame.K_DOWN):
                change_x = 0
                change_y = 10

    display_snake_and_food() #ikkada display chesaka em panicheydhu endukantey manam dheniki action ivvaledhu kabatti
    clock.tick(12)


#ippudu manam game start cheyyali antey manaki two things kavali
# 1.FOOD 
# 2.SNAKE
#so ippudu manam food ki snake ki code raadham
