import pygame, sys


def run_game():
    pass


pygame.init() 

#varibles
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
fullscreen_w = pygame.display.Info().current_w
fullscreen_h = pygame.display.Info().current_h

monitor_size = (fullscreen_w, fullscreen_h)

fullscreen = False

FPS = 60
game_state = "menu"
lives = 3

#colou1r
GREY = (29, 29, 27)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#displays the program

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("game")


clock = pygame.time.Clock()

fullscreen_btn_surface = pygame.Surface((75,75))
fullscreen_btn_rect = fullscreen_btn_surface.get_rect(midbottom = (980, 500))

#---------------------------- menu page -----------
play_btn_surface = pygame.Surface((300,75))
play_btn_surface.fill("Yellow")
play_btn_rect = play_btn_surface.get_rect(midbottom = (980, 250))

leaderboard_btn_surface = pygame.Surface((300,75))
leaderboard_btn_surface.fill("Yellow")
leaderboard_btn_rect = leaderboard_btn_surface.get_rect(midbottom = (980, 350))

test_btn_surface = pygame.Surface((300,75))
test_btn_surface.fill("Yellow")
test_btn_rect = test_btn_surface.get_rect(midbottom = (980, 450))

test_font = pygame.font.Font("Typo Draft Demo.otf", 60)
text_surface = test_font.render("Invaders", False, "White")

btn_font = pygame.font.Font("Typo Draft Demo.otf", 30)

play_text_surface = btn_font.render("play", False, "White")
play_text_rect = play_text_surface.get_rect(midbottom = (980, 250))

leaderboard_text_surface = btn_font.render("leaderboard", False, "White")
leaderboard_text_rect = leaderboard_text_surface.get_rect(midbottom = (980, 350))

test_text_surface = btn_font.render("test", False, "White")
test_text_rect = test_text_surface.get_rect(midbottom = (980, 450))
 


#---------------------------- gameplay page -----------
gameplay1_btn_surface = pygame.Surface((300,75))
gameplay1_btn_rect = gameplay1_btn_surface.get_rect(midbottom = (980, 250))

gameplay2_btn_surface = pygame.Surface((300,75))
gameplay2_btn_rect = gameplay2_btn_surface.get_rect(midbottom = (980, 350))

gameplay3_btn_surface = pygame.Surface((300,75))
gameplay3_btn_rect = gameplay3_btn_surface.get_rect(midbottom = (980, 450))

gameplay_font = pygame.font.Font("Typo Draft Demo.otf", 60)

gameplay_text_surface = gameplay_font.render("gameplay", False, "White")


#---------------------------- game over page -----------
gameover1_btn_surface = pygame.Surface((300,75))
gameover1_btn_surface.fill("green")
gameover1_btn_rect = gameover1_btn_surface.get_rect(midbottom = (980, 250))

gameover2_btn_surface = pygame.Surface((300,75))
gameover2_btn_surface.fill("green")
gameover2_btn_rect = gameover2_btn_surface.get_rect(midbottom = (980, 350))

gameover3_btn_surface = pygame.Surface((300,75))    
gameover3_btn_surface.fill("green")
gameover3_btn_rect = gameover3_btn_surface.get_rect(midbottom = (980, 450))

gameover_font = pygame.font.Font("Typo Draft Demo.otf", 60)

gameover_text_surface = gameover_font.render("game over", False, "White")

gameover_btn_font = pygame.font.Font("Typo Draft Demo.otf", 30)

gameover1_text_surface = gameover_btn_font.render("play again", False, "White")
gameover1_text_rect = gameover1_text_surface.get_rect(midbottom = (980, 250))

gameover2_text_surface = gameover_btn_font.render("back to menu", False, "White")
gameover2_text_rect = gameover2_text_surface.get_rect(midbottom = (980, 350))

gameover3_text_surface = gameover_btn_font.render("quit", False, "White")
gameover3_text_rect = gameover3_text_surface.get_rect(midbottom = (980, 450))
 



#game loop
while True:
    #checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        print(fullscreen_w)
        #game mechanics/ how game works
        if event.type == pygame.MOUSEBUTTONUP:
            
            if game_state == "menu":
                if play_btn_rect.collidepoint(event.pos):
                    game_state = "gameplay"
                    print("game state is gameplay")

            elif game_state == "gameplay":
                if gameplay1_btn_rect.collidepoint(event.pos):
                    game_state = "gameover"
                    lives = 0
                    print("game state is game over")

            elif game_state == "gameover":
                if gameover1_btn_rect.collidepoint(event.pos):
                    game_state = "gameplay"
                    lives = 3
                    print("game state is menu")
                elif gameover2_btn_rect.collidepoint(event.pos):
                    game_state = "menu"
                    lives = 3
                    print("game state is menu")
                elif gameover3_btn_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            if fullscreen_btn_rect.collidepoint(event.pos):
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)


            
    #drawing (displaying sprites/objects)
    if game_state == "menu":
        screen.fill(GREY)
        screen.blit(text_surface,(800, 50))
        screen.blit(play_btn_surface, play_btn_rect)
        screen.blit(leaderboard_btn_surface, leaderboard_btn_rect)
        screen.blit(test_btn_surface, test_btn_rect)
        screen.blit(play_text_surface, play_text_rect)
        screen.blit(leaderboard_text_surface, leaderboard_text_rect)
        screen.blit(test_text_surface, test_text_rect)
        screen.blit(fullscreen_btn_surface, fullscreen_btn_rect)
        
    elif game_state == "gameplay":
        screen.fill(RED)
        screen.blit(gameplay_text_surface,(800, 50))
        screen.blit(gameplay1_btn_surface, gameplay1_btn_rect)
        screen.blit(gameplay2_btn_surface, gameplay2_btn_rect)
        screen.blit(gameplay3_btn_surface, gameplay3_btn_rect)
        screen.blit(fullscreen_btn_surface, fullscreen_btn_rect)

    elif game_state == "gameover":
        screen.fill(BLUE)
        screen.blit(gameover_text_surface,(800, 50))
        screen.blit(gameover1_btn_surface, gameover1_btn_rect)
        screen.blit(gameover2_btn_surface, gameover2_btn_rect)
        screen.blit(gameover3_btn_surface, gameover3_btn_rect)
        screen.blit(gameover1_text_surface, gameover1_text_rect)
        screen.blit(gameover2_text_surface, gameover2_text_rect)
        screen.blit(gameover3_text_surface, gameover3_text_rect)
        screen.blit(fullscreen_btn_surface, fullscreen_btn_rect)

    #continuous updates the game
    pygame.display.update()
    clock.tick(FPS)