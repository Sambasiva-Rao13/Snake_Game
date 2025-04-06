import pygame
import time
import random

pygame.init()

width,height=600,400
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

snake_block=10
snake_speed=12
clock=pygame.time.Clock()
font_style=pygame.font.SysFont("arial",25)

def score_display(score):
    value=font_style.render("Score: "+str(score), True, red)
    win.blit(value,[0,0])

def draw_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(win, green, [i[0],i[1], snake_block,snake_block])

def message(msg, color):
    mseg=font_style.render(msg,True,color)
    win.blit(mseg, [width/6, height/3])

def gameLoop():

    game_over=False
    game_close=False

    x1,y1=width/2,height/2
    x1_change, y1_change= 0,0

    snake_list=[]
    length_of_snake=1

    foodx=round(random.randrange(0,width-snake_block,10))
    foody=round(random.randrange(0,height-snake_block,10))

    while not game_over:

        while game_close:

            win.fill(white)
            message("You lost! Press q-Quit or c-Play again", red)
            score_display(length_of_snake-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                    game_close=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    elif event.key==pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0

        
        x1+=x1_change
        y1+=y1_change

        if x1>=width or x1<0 or y1>=height or y1<0:
            game_close=True
        

        win.fill(black)
        pygame.draw.rect(win, red, [foodx,foody,snake_block,snake_block])

        snake_head=[x1,y1]
        snake_list.append(snake_head)

        if len(snake_list)>length_of_snake:
            del snake_list[0]

        draw_snake(snake_block,snake_list)
        score_display(length_of_snake-1)
        pygame.display.update()

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close=True

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,width-snake_block,10))
            foody=round(random.randrange(0,height-snake_block,10))
            length_of_snake+=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()
