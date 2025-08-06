import pygame, sys


def run_game():
    pass

pygame.init() 

#varibles
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
fullscreen_w = pygame.display.Info().current_w #gets the monitor screen size - width
fullscreen_h = pygame.display.Info().current_h #gets the monitor screen size - height

monitor_size = (fullscreen_w, fullscreen_h)

scaling_w = fullscreen_w/SCREEN_WIDTH
scaling_h = fullscreen_h/SCREEN_HEIGHT


FPS = 60
game_state = "menu"
lives = 3

#colou1r
GREY = (29, 29, 27)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#displays the program

screen = pygame.display.set_mode(monitor_size, pygame.NOFRAME) #.NOFRAME displays just the screen. there is no top right options
pygame.display.set_caption("game")


clock = pygame.time.Clock()

quit_btn_surface = pygame.Surface((30,30))
quit_btn_rect = quit_btn_surface.get_rect(center = (fullscreen_w - 30, 30))


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

test_font = pygame.font.Font("Grand Casino Demo.otf", 60)
text_surface = test_font.render("Invaders", False, "White")

btn_font = pygame.font.Font("Grand Casino Demo.otf", 30)

play_text_surface = btn_font.render("play", False, "White")
play_text_rect = play_text_surface.get_rect(midbottom = (980, 250))

leaderboard_text_surface = btn_font.render("leaderboard", False, "White")
leaderboard_text_rect = leaderboard_text_surface.get_rect(midbottom = (980, 350))

test_text_surface = btn_font.render("test", False, "White")
test_text_rect = test_text_surface.get_rect(midbottom = (980, 450))



#---------------------------- gameplay page -----------
payout_btn_surface = pygame.Surface((250,75))
payout_btn_rect = payout_btn_surface.get_rect(midbottom = (fullscreen_w - 300, fullscreen_h - 100))

bet_decrease_btn_surface = pygame.Surface((75,75))
bet_decrease_btn_rect = bet_decrease_btn_surface.get_rect(midbottom = (200, fullscreen_h - 220))

bet_increase_btn_surface = pygame.Surface((75,75))
bet_increase_btn_rect = bet_increase_btn_surface.get_rect(midbottom = (500, fullscreen_h - 220))

diff_decrease_btn_surface = pygame.Surface((75,75))
diff_decrease_btn_rect = diff_decrease_btn_surface.get_rect(midbottom = (700, fullscreen_h - 220))

diff_increase_btn_surface = pygame.Surface((75,75))
diff_increase_btn_rect = diff_increase_btn_surface.get_rect(midbottom = (1000, fullscreen_h - 220))

diff_dis_surface = pygame.Surface((200,75))
diff_dis_rect = diff_dis_surface.get_rect(midbottom = (350, fullscreen_h - 220))

bet_dis_surface = pygame.Surface((200,75))
bet_dis_rect = bet_dis_surface.get_rect(midbottom = (850, fullscreen_h - 220))



gameplay_font = pygame.font.Font("Grand Casino Demo.otf", 60)

gameplay_text_surface = gameplay_font.render("gameplay", False, "White")

gameplay_btn_font = pygame.font.Font("Grand Casino Demo.otf", 30)

payout_text_surface = gameplay_btn_font.render("pay out", False, "White")
payout_text_rect = payout_text_surface.get_rect(midbottom = (fullscreen_w - 300, fullscreen_h - 100))

bet_decrease_text_surface = gameplay_btn_font.render("-", False, "White")
bet_decrease_text_rect = bet_decrease_text_surface.get_rect(midbottom = (200, fullscreen_h - 220))

bet_increase_text_surface = gameplay_btn_font.render("+", False, "White")
bet_increase_text_rect = bet_increase_text_surface.get_rect(midbottom = (500, fullscreen_h - 220))

diff_decrease_text_surface = gameplay_btn_font.render("-", False, "White")
diff_decrease_text_rect = bet_decrease_text_surface.get_rect(midbottom = (700, fullscreen_h - 220))

diff_increase_text_surface = gameplay_btn_font.render("+", False, "White")
diff_increase_text_rect = bet_increase_text_surface.get_rect(midbottom = (1000, fullscreen_h - 220))

diff_dis_text_surface = gameplay_btn_font.render("diff", False, "White")
diff_dis_text_rect = bet_decrease_text_surface.get_rect(midbottom = (350, fullscreen_h - 220))

bet_dis_text_surface = gameplay_btn_font.render("bet", False, "White")
bet_dis_text_rect = bet_increase_text_surface.get_rect(midbottom = (850, fullscreen_h - 220))


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

gameover_font = pygame.font.Font("Grand Casino Demo.otf", 60)

gameover_text_surface = gameover_font.render("game over", False, "White")

gameover_btn_font = pygame.font.Font("Grand Casino Demo.otf", 30)

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

        #game mechanics/ how game works
        if event.type == pygame.MOUSEBUTTONUP:
            
            if game_state == "menu":
                if play_btn_rect.collidepoint(event.pos):
                    game_state = "gameplay"
                    print("game state is gameplay")

            elif game_state == "gameplay":
                if payout_btn_rect.collidepoint(event.pos):
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
            if quit_btn_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()


            
#drawing (displaying sprites/objects)
    #menu page
    if game_state == "menu":
        screen.fill(GREY)
        screen.blit(text_surface,(800, 50))
        screen.blit(play_btn_surface, play_btn_rect)
        screen.blit(leaderboard_btn_surface, leaderboard_btn_rect)
        screen.blit(test_btn_surface, test_btn_rect)
        screen.blit(play_text_surface, play_text_rect)
        screen.blit(leaderboard_text_surface, leaderboard_text_rect)
        screen.blit(test_text_surface, test_text_rect)
        screen.blit(quit_btn_surface, quit_btn_rect)

    #gameplay page    fullscreen_w, fullscreen_h
    elif game_state == "gameplay":
        screen.fill(RED)
        screen.blit(gameplay_text_surface,(800, 50))
        screen.blit(payout_btn_surface, payout_btn_rect)
        screen.blit(bet_decrease_btn_surface, bet_decrease_btn_rect)
        screen.blit(bet_increase_btn_surface, bet_increase_btn_rect)
        screen.blit(diff_decrease_btn_surface, diff_decrease_btn_rect)
        screen.blit(diff_increase_btn_surface, diff_increase_btn_rect)
        screen.blit(bet_dis_surface, bet_dis_rect)
        screen.blit(diff_dis_surface, diff_dis_rect)

        screen.blit(quit_btn_surface, quit_btn_rect)
        screen.blit(payout_text_surface, payout_text_rect)
        screen.blit(bet_decrease_text_surface, bet_decrease_text_rect)
        screen.blit(bet_increase_text_surface, bet_increase_text_rect)
        screen.blit(diff_decrease_text_surface, diff_decrease_text_rect)
        screen.blit(diff_increase_text_surface, diff_increase_text_rect)
        screen.blit(bet_dis_text_surface, bet_dis_text_rect)
        screen.blit(diff_dis_text_surface, diff_dis_text_rect)
        pygame.draw.line(screen, BLUE, (fullscreen_w - 100, fullscreen_h - 300),(fullscreen_w - 100, fullscreen_h - 50), 4) #options - right
        pygame.draw.line(screen, BLUE, (100, fullscreen_h - 300),(100, fullscreen_h - 50), 4) #options - left
        pygame.draw.line(screen, BLUE, (100, fullscreen_h - 300),(fullscreen_w - 100, fullscreen_h - 300), 4) #options - top
        pygame.draw.line(screen, BLUE, (100, fullscreen_h - 50),(fullscreen_w - 100, fullscreen_h - 50), 4) #options - bottom
        
    #gameover page
    elif game_state == "gameover":
        screen.fill(BLUE)
        screen.blit(gameover_text_surface,(800, 50))
        screen.blit(gameover1_btn_surface, gameover1_btn_rect)
        screen.blit(gameover2_btn_surface, gameover2_btn_rect)
        screen.blit(gameover3_btn_surface, gameover3_btn_rect)
        screen.blit(gameover1_text_surface, gameover1_text_rect)
        screen.blit(gameover2_text_surface, gameover2_text_rect)
        screen.blit(gameover3_text_surface, gameover3_text_rect)
        screen.blit(quit_btn_surface, quit_btn_rect)

    #continuous updates the game
    pygame.display.update()
    clock.tick(FPS)
