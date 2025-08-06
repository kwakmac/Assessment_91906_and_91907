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

#values
FPS = 60
game_state = "menu"
difficulty_value = 1
bet_value = 100
bet_amount_multi = 1

#colou1r
GREY = (29, 29, 27)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (0,0,0)

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
text_surface = test_font.render("math add-it", False, "White")

font_1 = pygame.font.Font("Grand Casino Demo.otf", 30)

play_text_surface = font_1.render("play", False, "White")
play_text_rect = play_text_surface.get_rect(midbottom = (980, 250))

leaderboard_text_surface = font_1.render("leaderboard", False, "White")
leaderboard_text_rect = leaderboard_text_surface.get_rect(midbottom = (980, 350))

test_text_surface = font_1.render("test", False, "White")
test_text_rect = test_text_surface.get_rect(midbottom = (980, 450))



#---------------------------- gameplay page -----------


payout_btn_surface = pygame.Surface((30,30))
payout_btn_rect = payout_btn_surface.get_rect(midbottom = (fullscreen_w - 30, 80))

btn_hub_surface = pygame.Surface((1100, 230))
btn_hub_rect = btn_hub_surface.get_rect(midbottom = (fullscreen_w/2, fullscreen_h - 40))

diff_hub_surface = pygame.Surface((130, 200))
diff_hub_surface.fill(GREY)
diff_hub_rect = diff_hub_surface.get_rect(midbottom = (498, fullscreen_h - 55))

bet_hub_surface = pygame.Surface((435, 200))
bet_hub_surface.fill(GREY)
bet_hub_rect = bet_hub_surface.get_rect(midbottom = (fullscreen_w - 475, fullscreen_h - 55))

slots_machine_surface = pygame.Surface((845, 350))
slots_machine_rect = slots_machine_surface.get_rect(midbottom = (513, 400))

slots_1_surface = pygame.Surface((230, 300))
slots_1_surface.fill(GREY)
slots_1_rect = slots_1_surface.get_rect(midbottom = (257, 375))

slots_2_surface = pygame.Surface((230, 300))
slots_2_surface.fill(GREY)
slots_2_rect = slots_2_surface.get_rect(midbottom = (513, 375))

slots_3_surface = pygame.Surface((230, 300))
slots_3_surface.fill(GREY)
slots_3_rect = slots_3_surface.get_rect(midbottom = (770, 375))


spin_btn_surface = pygame.Surface((100, 150))
spin_btn_surface.fill(GREY)
spin_btn_rect = spin_btn_surface.get_rect(midbottom = (fullscreen_w - 182, fullscreen_h - 79))

diff_increase_btn_surface = pygame.Surface((35, 35))
diff_increase_btn_surface.fill(WHITE)
diff_increase_btn_rect = diff_increase_btn_surface.get_rect(midbottom = (498, fullscreen_h - 200))

diff_display_surface = pygame.Surface((90, 60))
diff_display_surface.fill(WHITE)
diff_display_rect = diff_display_surface.get_rect(midbottom = (498, fullscreen_h - 128))

diff_decrease_btn_surface = pygame.Surface((35, 35))
diff_decrease_btn_surface.fill(WHITE)
diff_decrease_btn_rect = diff_decrease_btn_surface.get_rect(midbottom = (498, fullscreen_h - 80))

op_mult_display_surface = pygame.Surface((90, 60))
op_mult_display_surface.fill(WHITE)
op_mult_display_rect = op_mult_display_surface.get_rect(midbottom = (fullscreen_w - 320, fullscreen_h - 150))

bet_increase_btn_surface = pygame.Surface((35, 35))
bet_increase_btn_surface.fill(WHITE)
bet_increase_btn_rect = bet_increase_btn_surface.get_rect(midbottom = (fullscreen_w - 450, fullscreen_h - 163))

bet_display_surface = pygame.Surface((150, 60))
bet_display_surface.fill(WHITE)
bet_display_rect = bet_display_surface.get_rect(midbottom = (fullscreen_w - 550, fullscreen_h - 150))

bet_decrease_btn_surface = pygame.Surface((35, 35))
bet_decrease_btn_surface.fill(WHITE)
bet_decrease_btn_rect = bet_decrease_btn_surface.get_rect(midbottom = (fullscreen_w - 650, fullscreen_h - 163))

bet_increase_amount_multi_surface = pygame.Surface((35, 35))
bet_increase_amount_multi_surface.fill(WHITE)
bet_increase_amount_multi_rect = bet_increase_amount_multi_surface.get_rect(midbottom = (fullscreen_w - 500, fullscreen_h - 100))

bet_amount_multi_display_surface = pygame.Surface((40, 40))
bet_amount_multi_display_surface.fill(WHITE)
bet_amount_multi_display_rect = bet_amount_multi_display_surface.get_rect(midbottom = (fullscreen_w - 550, fullscreen_h - 97))

bet_decrease_amount_multi_surface = pygame.Surface((35, 35))
bet_decrease_amount_multi_surface.fill(WHITE)
bet_decrease_amount_multi_rect = bet_decrease_amount_multi_surface.get_rect(midbottom = (fullscreen_w - 600, fullscreen_h - 100))

crt_ans_surface = pygame.Surface((85, 90))
crt_ans_surface.fill(GREY)
crt_ans_rect = crt_ans_surface.get_rect(midbottom = (366, fullscreen_h - 56))

info_display_btn_surface = pygame.Surface((85, 90))
info_display_btn_surface.fill(GREY)
info_display_btn_rect = info_display_btn_surface.get_rect(midbottom = (262, fullscreen_h - 56))

option_display_btn_surface = pygame.Surface((85, 90))
option_display_btn_surface.fill(GREY)
option_display_btn_rect = option_display_btn_surface.get_rect(midbottom = (158, fullscreen_h - 56))

score_display_surface = pygame.Surface((293, 90))
score_display_surface.fill(GREY)
score_display_rect = score_display_surface.get_rect(midbottom = (262, fullscreen_h - 165))

#------------------------ gameplay font ----------------------

font_2 = pygame.font.Font("gvhs-gothic.ttf", 20)

diff_text_surface = font_2.render("1", False, "White")
diff_text_rect = diff_text_surface.get_rect(midbottom = (498, fullscreen_h - 128))

bet_text_surface = font_2.render("100", False, "White")
bet_text_rect = bet_text_surface.get_rect(midbottom = (fullscreen_w - 550, fullscreen_h - 150))

bet_amount_multi_text_surface = font_2.render("1"+"x", False, "White")
bet_amount_multi_text_rect = bet_amount_multi_text_surface.get_rect(midbottom = (fullscreen_w - 550, fullscreen_h - 97))

option_display_btn_text_surface = font_2.render("options", False, "White")
option_display_btn_text_rect = option_display_btn_text_surface.get_rect(midbottom = (158, fullscreen_h - 56))

info_display_btn_text_surface = font_2.render("info", False, "White")
info_display_btn_text_rect = info_display_btn_text_surface.get_rect(midbottom = (262, fullscreen_h - 56))

score_display_text_surface = font_2.render("0", False, "White")
score_display_text_rect = score_display_text_surface.get_rect(midbottom = (262, fullscreen_h - 165))

spin_btn_text_surface = font_2.render("spin", False, "White")
spin_btn_text_rect = spin_btn_text_surface.get_rect(midbottom = (fullscreen_w - 182, fullscreen_h - 79))

slots_1_text_surface = font_2.render("1", False, "White")
slots_1_text_rect = slots_1_text_surface.get_rect(midbottom = (257, 375))

slots_2_text_surface = font_2.render("+", False, "White")
slots_2_text_rect = slots_2_text_surface.get_rect(midbottom = (513, 375))

slots_3_text_surface = font_2.render("1", False, "White")
slots_3_text_rect = slots_3_text_surface.get_rect(midbottom = (770, 375))

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

gameover_font_2 = pygame.font.Font("Grand Casino Demo.otf", 30)

gameover1_text_surface = gameover_font_2.render("play again", False, "White")
gameover1_text_rect = gameover1_text_surface.get_rect(midbottom = (980, 250))

gameover2_text_surface = gameover_font_2.render("back to menu", False, "White")
gameover2_text_rect = gameover2_text_surface.get_rect(midbottom = (980, 350))

gameover3_text_surface = gameover_font_2.render("quit", False, "White")
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
                    print("game state is game over")
            #difficulty control
                if difficulty_value < 3 and diff_increase_btn_rect.collidepoint(event.pos):
                    difficulty_value += 1
                    diff_text_surface = font_2.render(str(difficulty_value), False, "White")
                    
                if difficulty_value > 1 and diff_decrease_btn_rect.collidepoint(event.pos):
                    difficulty_value -= 1
                    diff_text_surface = font_2.render(str(difficulty_value), False, "White")
            #bet amount multi
                if bet_amount_multi < 1000 and bet_increase_amount_multi_rect.collidepoint(event.pos):
                    bet_amount_multi *= 10
                    bet_amount_multi = bet_amount_multi
                    bet_amount_multi_text_surface = font_2.render(str(bet_amount_multi)+"x", False, "White")
                    
                if bet_amount_multi > 1 and bet_decrease_amount_multi_rect.collidepoint(event.pos):
                    bet_amount_multi //= 10
                    bet_amount_multi = bet_amount_multi
                    bet_amount_multi_text_surface = font_2.render(str(bet_amount_multi)+"x", False, "White")
            #bet control 
                if bet_value < 10000 and bet_amount_multi == 1 and bet_increase_btn_rect.collidepoint(event.pos):
                    bet_value += 1
                    bet_text_surface = font_2.render(str(bet_value), False, "White")

                if bet_value < 10000 and bet_amount_multi == 10 and bet_increase_btn_rect.collidepoint(event.pos):
                    bet_value += 10
                    bet_text_surface = font_2.render(str(bet_value), False, "White")

                if bet_value < 10000 and bet_amount_multi == 100 and bet_increase_btn_rect.collidepoint(event.pos):
                    bet_value += 100
                    bet_text_surface = font_2.render(str(bet_value), False, "White")

                if bet_value < 10000 and bet_amount_multi == 1000 and bet_increase_btn_rect.collidepoint(event.pos):
                    bet_value += 1000
                    bet_text_surface = font_2.render(str(bet_value), False, "White")
            
                if bet_value > 1 and bet_amount_multi == 1 and bet_decrease_btn_rect.collidepoint(event.pos):
                    bet_value -= 1
                    bet_text_surface = font_2.render(str(bet_value), False, "White")

                if bet_value > 1 and bet_amount_multi == 10 and bet_decrease_btn_rect.collidepoint(event.pos):
                    bet_value -= 10
                    bet_text_surface = font_2.render(str(bet_value), False, "White")

                if bet_value > 1 and bet_amount_multi == 100 and bet_decrease_btn_rect.collidepoint(event.pos):
                    bet_value -= 100
                    bet_text_surface = font_2.render(str(bet_value), False, "White")

                if bet_value > 1 and bet_amount_multi == 1000 and bet_decrease_btn_rect.collidepoint(event.pos):
                    bet_value -= 1000
                    bet_text_surface = font_2.render(str(bet_value), False, "White")
            #options btn
                if option_display_btn_rect.collidepoint(event.pos):
                    print("options")
            #info  btn
                if info_display_btn_text_rect.collidepoint(event.pos):
                    print("info")
                    
            
            elif game_state == "gameover":
                if gameover1_btn_rect.collidepoint(event.pos):
                    game_state = "gameplay"
                    print("game state is gameplay")
                elif gameover2_btn_rect.collidepoint(event.pos):
                    game_state = "menu"
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
        screen.blit(payout_btn_surface, payout_btn_rect)
        screen.blit(btn_hub_surface, btn_hub_rect)
        screen.blit(diff_hub_surface, diff_hub_rect)
        screen.blit(bet_hub_surface, bet_hub_rect)
        screen.blit(diff_increase_btn_surface, diff_increase_btn_rect)
        screen.blit(diff_display_surface, diff_display_rect)
        screen.blit(diff_decrease_btn_surface, diff_decrease_btn_rect)
        screen.blit(op_mult_display_surface, op_mult_display_rect)
        screen.blit(bet_increase_btn_surface, bet_increase_btn_rect)
        screen.blit(bet_display_surface, bet_display_rect)
        screen.blit(bet_decrease_btn_surface, bet_decrease_btn_rect)
        screen.blit(bet_increase_amount_multi_surface, bet_increase_amount_multi_rect)
        screen.blit(bet_amount_multi_display_surface, bet_amount_multi_display_rect)
        screen.blit(bet_decrease_amount_multi_surface, bet_decrease_amount_multi_rect)
        screen.blit(spin_btn_surface, spin_btn_rect)
        screen.blit(crt_ans_surface, crt_ans_rect)
        screen.blit(info_display_btn_surface, info_display_btn_rect)
        screen.blit(option_display_btn_surface, option_display_btn_rect)
        screen.blit(score_display_surface, score_display_rect)
        screen.blit(slots_machine_surface, slots_machine_rect)
        screen.blit(slots_1_surface, slots_1_rect)
        screen.blit(slots_2_surface, slots_2_rect)
        screen.blit(slots_3_surface, slots_3_rect)

        screen.blit(diff_text_surface, diff_text_rect)
        screen.blit(bet_text_surface, bet_text_rect)
        screen.blit(bet_amount_multi_text_surface, bet_amount_multi_text_rect)
        screen.blit(option_display_btn_text_surface, option_display_btn_text_rect)
        screen.blit(info_display_btn_text_surface, info_display_btn_text_rect)
        screen.blit(score_display_text_surface, score_display_text_rect)
        screen.blit(spin_btn_text_surface, spin_btn_text_rect)
        screen.blit(slots_1_text_surface, slots_1_text_rect)
        screen.blit(slots_2_text_surface, slots_2_text_rect)
        screen.blit(slots_3_text_surface, slots_3_text_rect)
        
        

        
        
        
        
        
        


        screen.blit(quit_btn_surface, quit_btn_rect)
       
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

