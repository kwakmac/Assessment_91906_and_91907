#AUTHOR - KAEA MACDONALD
#DATE - 28/03/25 - 07/08/25
#PURPOSE - THE PURPOSE OF MY PROGRAM IS TO HELP PEOPLE AT ANY AGE WITH LEARNING MATH



import pygame, sys
import random
import json
import os
from fractions import Fraction


def load_player_account(filename = "player_account_details.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return {}
    
def save_player_account(account, filename = "player_account_details.json"):
    with open(filename, "w") as f:
        json.dump(account, f, indent = 3)

def get_player_data(player_id, data, default = 0):
    account = load_player_account()
    return account.get(player_id, {}).get(data, default)

def update_player_data(player_id, data, value):
    account = load_player_account()
    if player_id not in account:
        account[player_id] = {}
    account[player_id][data] = value
    save_player_account(account)

def run_game(player_id):
    pygame.init() 

    #varibles
    BASE_SCREEN_WIDTH = 1920
    BASE_SCREEN_HEIGHT = 1080
    ACTUAL_SCREEN_WIDTH = pygame.display.Info().current_w #gets the monitor screen size - width
    ACTUAL_SCREEN_HEIGHT = pygame.display.Info().current_h #gets the monitor screen size - height

    #laptop screen size = 1280,720
    #desktop screen size = 1920,1080
    
    monitor_size = (ACTUAL_SCREEN_WIDTH, ACTUAL_SCREEN_HEIGHT)

    SCALE_W = ACTUAL_SCREEN_WIDTH/BASE_SCREEN_WIDTH
    SCALE_H = ACTUAL_SCREEN_HEIGHT/BASE_SCREEN_HEIGHT

    SCALE = min(SCALE_W,SCALE_H)

    #helps with scaling every object/component in my program so it can fit nicly on different monitor screens
    def scale_obj_position(x,y):
        return(int(x * SCALE), (y * SCALE))
    def scale_obj_size(w,h):
        return((w * SCALE), (h * SCALE))

    #data values/varibles
    FPS = 60
    game_state = "menu"
    difficulty_value = 1
    bet_value = 100
    bet_amount_multi = 1
    user_text = ""
    question_crt_ans = None
    op_choice = None

    current_player_score_display_value = 100
    current_player_answered_correct = 0
    current_player_spins = 0
    total_spins = 0
    total_answered_correct = 0

    if get_player_data (player_id, "current score", None) is None:
        update_player_data(player_id, "current score", 100)
        update_player_data(player_id, "current answered correctly", 0)
        update_player_data(player_id, "current spins", 0)


    current_player_score_display_value = get_player_data(player_id, "current score", default= 100)
    current_player_answered_correct = get_player_data(player_id, "current answered correctly", default = 0)
    current_player_spins = get_player_data(player_id, "current spins", default = 0)

    player_can_type = False
    question_active = False

    operators = ["+", "-", "x", "/"]



    #colours
    GREY = (29, 29, 27)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255,255,255)
    CHILL_BLUE = (12, 137, 144)
    BLACK = (0,0,0)


    #displays the program
    screen = pygame.display.set_mode(monitor_size, pygame.NOFRAME) #.NOFRAME displays just the screen. there is no top right options
    pygame.display.set_caption("game")


    bg_size = (scale_obj_size(1920, 1080))
    bg_image = pygame.transform.scale(pygame.image.load("bg1.png"),bg_size).convert_alpha()
              

    clock = pygame.time.Clock()

    quit_btn_surface = pygame.Surface(scale_obj_size(30,30))
    quit_btn_rect = quit_btn_surface.get_rect(center = scale_obj_position(1890, 30))


    #---------------------------- menu page -----------
    play_btn_surface = pygame.Surface(scale_obj_size(300,75))
    play_btn_surface.fill("Yellow")
    play_btn_rect = play_btn_surface.get_rect(midbottom = scale_obj_position(1690, 250))

    test_font = pygame.font.Font("gvhs-gothic.ttf", 40)
    font_1 = pygame.font.Font("gvhs-gothic.ttf", 20)

    title_text_surface = test_font.render("math add-it", False, "White")
    title_text_rect = title_text_surface.get_rect(midbottom = scale_obj_position(1390, 100))

    play_text_surface = font_1.render("play", False, "White")
    play_text_rect = play_text_surface.get_rect(midbottom = scale_obj_position(1690, 250))


    #---------------------------- gameplay page -----------
    payout_btn_surface = pygame.Surface(scale_obj_size(30,30))
    payout_btn_rect = payout_btn_surface.get_rect(midbottom = scale_obj_position(1890, 80))

    gui_hub_size = (scale_obj_size(1630, 350))
    gui_hub_img = pygame.transform.scale(pygame.image.load("hub16.png"),gui_hub_size).convert_alpha()
    btn_hub_rect = gui_hub_img.get_rect(midbottom = scale_obj_position(960, 1020))

    diff_hub_size = (scale_obj_size(200, 282))
    diff_hub_img = pygame.transform.scale(pygame.image.load("diff_hub7.png"),diff_hub_size).convert_alpha()
    diff_hub_rect = diff_hub_img.get_rect(midbottom = scale_obj_position(747, 985))

    bet_hub_size = (scale_obj_size(600, 282))
    bet_hub_img = pygame.transform.scale(pygame.image.load("bet_hub2.png"),bet_hub_size).convert_alpha()
    bet_hub_rect = bet_hub_img.get_rect(midbottom = scale_obj_position(1205, 985))

    slots_machine_surface = pygame.Surface(scale_obj_size(1130, 560))
    slots_machine_rect = slots_machine_surface.get_rect(midbottom = scale_obj_position(710, 610))

    slots_1_surface = pygame.Surface(scale_obj_size(320, 500))
    slots_1_surface.fill(GREY)
    slots_1_rect = slots_1_surface.get_rect(midbottom = scale_obj_position(350, 579))

    slots_2_surface = pygame.Surface(scale_obj_size(320, 500))
    slots_2_surface.fill(GREY)
    slots_2_rect = slots_2_surface.get_rect(midbottom = scale_obj_position(710, 579))

    slots_3_surface = pygame.Surface(scale_obj_size(320, 500))
    slots_3_surface.fill(GREY)
    slots_3_rect = slots_3_surface.get_rect(midbottom = scale_obj_position(1070, 579))

    spin_btn_size = (scale_obj_size(180, 282))
    spin_btn_img = pygame.transform.scale(pygame.image.load("spin_btn.png"),spin_btn_size).convert_alpha()
    spin_btn_rect = spin_btn_img.get_rect(midbottom = scale_obj_position(1647, 985))

    diff_increase_btn_size = (scale_obj_size(50, 50))
    diff_increase_btn_img = pygame.transform.scale(pygame.image.load("arrow_up.png"),diff_increase_btn_size).convert_alpha()
    diff_increase_btn_rect = diff_increase_btn_img.get_rect(midbottom = scale_obj_position(747, 790))

    diff_display_surface = pygame.Surface(scale_obj_size(100, 70))
    diff_display_surface.fill(BLACK)
    diff_display_rect = diff_display_surface.get_rect(midbottom = scale_obj_position(747, 880))

    diff_decrease_btn_size = (scale_obj_size(50, 50))
    diff_decrease_btn_img = pygame.transform.scale(pygame.image.load("arrow_down.png"),diff_decrease_btn_size).convert_alpha()
    diff_decrease_btn_rect = diff_decrease_btn_img.get_rect(midbottom = scale_obj_position(747, 947))

    op_mult_display_surface = pygame.Surface(scale_obj_size(90, 70))
    op_mult_display_surface.fill(BLACK)
    op_mult_display_rect = op_mult_display_surface.get_rect(midbottom = scale_obj_position(1420, 837))

    bet_increase_btn_size = (scale_obj_size(50, 50))
    bet_increase_btn_img = pygame.transform.scale(pygame.image.load("arrow_right.png"),bet_increase_btn_size).convert_alpha()
    bet_increase_btn_rect = bet_increase_btn_img.get_rect(midbottom = scale_obj_position(1217, 826))

    bet_display_surface = pygame.Surface(scale_obj_size(150, 70))
    bet_display_surface.fill(BLACK)
    bet_display_rect = bet_display_surface.get_rect(midbottom = scale_obj_position(1095, 837))

    bet_decrease_btn_size = (scale_obj_size(50, 50))
    bet_decrease_btn_img = pygame.transform.scale(pygame.image.load("arrow_left.png"),bet_decrease_btn_size).convert_alpha()
    bet_decrease_btn_rect = bet_decrease_btn_img.get_rect(midbottom = scale_obj_position(973, 826))

    bet_increase_amount_multi_size = (scale_obj_size(50, 50))
    bet_increase_amount_multi_img = pygame.transform.scale(pygame.image.load("arrow_right.png"),bet_increase_amount_multi_size).convert_alpha()
    bet_increase_amount_multi_rect = bet_increase_amount_multi_img.get_rect(midbottom = scale_obj_position(1173, 911))

    bet_amount_multi_display_surface = pygame.Surface(scale_obj_size(60, 60))
    bet_amount_multi_display_surface.fill(BLACK)
    bet_amount_multi_display_rect = bet_amount_multi_display_surface.get_rect(midbottom = scale_obj_position(1095, 915))

    bet_decrease_amount_multi_size = (scale_obj_size(50, 50))
    bet_decrease_amount_multi_img = pygame.transform.scale(pygame.image.load("arrow_left.png"),bet_decrease_amount_multi_size).convert_alpha()
    bet_decrease_amount_multi_rect = bet_decrease_amount_multi_img.get_rect(midbottom = scale_obj_position(1018, 911))

    crt_ans_size = (scale_obj_size(150, 145))
    crt_ans_img = pygame.transform.scale(pygame.image.load("crt_ans.png"),crt_ans_size).convert_alpha()
    crt_ans_rect = crt_ans_img.get_rect(midbottom = scale_obj_position(470, 985))

    option_display_btn_size = (scale_obj_size(150, 145))
    option_display_btn_img = pygame.transform.scale(pygame.image.load("opt_btn.png"),option_display_btn_size).convert_alpha()
    option_display_btn_rect = option_display_btn_img.get_rect(midbottom = scale_obj_position(290, 985))

    score_display_surface = pygame.Surface(scale_obj_size(410, 110))
    score_display_surface.fill(GREY)
    score_display_rect = score_display_surface.get_rect(midbottom = scale_obj_position(385, 814))

    feedback_display_surface = pygame.Surface(scale_obj_size(410, 110))
    feedback_display_surface.fill(BLACK)
    feedback_display_rect = feedback_display_surface.get_rect(midbottom = scale_obj_position(1600, 500))

    #------------------------ gameplay font ----------------------

    font_2 = pygame.font.Font("gvhs-gothic.ttf", 20)

    diff_text_surface = font_2.render("1", False, "White")
    diff_text_rect = diff_text_surface.get_rect(midbottom = scale_obj_position(747, 880))

    bet_text_surface = font_2.render("100", False, "White")
    bet_text_rect = bet_text_surface.get_rect(midbottom = scale_obj_position(1095, 837))

    bet_amount_multi_text_surface = font_2.render("1"+"x", False, "White")
    bet_amount_multi_text_rect = bet_amount_multi_text_surface.get_rect(midbottom = scale_obj_position(1095, 915))

    op_mult_display_text_surface = font_2.render("0", False, "White")
    op_mult_display_text_rect = op_mult_display_text_surface.get_rect(midbottom = scale_obj_position(1420, 837))

    option_display_btn_text_surface = font_2.render("opt", False, "White")
    option_display_btn_text_rect = option_display_btn_text_surface.get_rect(midbottom = scale_obj_position(290, 985))

    crt_ans_text_surface = font_2.render(str(current_player_answered_correct), False, "White")
    crt_ans_text_rect = crt_ans_text_surface.get_rect(midbottom = scale_obj_position(470, 985))

    score_display_text_surface = font_2.render(str(current_player_score_display_value), False, "White")
    score_display_text_rect = score_display_text_surface.get_rect(midbottom = scale_obj_position(385, 814))

    spin_btn_text_surface = font_2.render("spin", False, "White")
    spin_btn_text_rect = spin_btn_text_surface.get_rect(midbottom = scale_obj_position(1647, 985))

    slots_1_text_surface = font_2.render("spin", False, "White")
    slots_1_text_rect = slots_1_text_surface.get_rect(midbottom = scale_obj_position(350, 579))

    slots_2_text_surface = font_2.render("2", False, "White")
    slots_2_text_rect = slots_2_text_surface.get_rect(midbottom = scale_obj_position(710, 579))

    slots_3_text_surface = font_2.render("win", False, "White")
    slots_3_text_rect = slots_3_text_surface.get_rect(midbottom = scale_obj_position(1070, 579))

    feedback_display_text_surface = font_2.render("", False, "White")
    feedback_display_text_rect = feedback_display_text_surface.get_rect(midbottom = scale_obj_position(1600, 500))



    #---------------------------- game over page -----------
    gameover1_btn_surface = pygame.Surface(scale_obj_size(300,75))
    gameover1_btn_surface.fill("green")
    play_again_btn_rect = gameover1_btn_surface.get_rect(midbottom = scale_obj_position(1690, 250))

    gameover2_btn_surface = pygame.Surface(scale_obj_size(300,75))
    gameover2_btn_surface.fill("green")
    gameover2_btn_rect = gameover2_btn_surface.get_rect(midbottom = scale_obj_position(1690, 350))

    gameover3_btn_surface = pygame.Surface(scale_obj_size(300,75))    
    gameover3_btn_surface.fill("green")
    gameover3_btn_rect = gameover3_btn_surface.get_rect(midbottom = scale_obj_position(1690, 450))

    gameover_font = pygame.font.Font("gvhs-gothic.ttf", 40)
    gameover_font_2 = pygame.font.Font("gvhs-gothic.ttf", 20)

    gameover_title_text_surface = gameover_font.render("game over", False, "White")
    gameover_title_text_rect = gameover_title_text_surface.get_rect(midbottom = scale_obj_position(1390, 100))

    gameover1_text_surface = gameover_font_2.render("play again", False, "White")
    gameover1_text_rect = gameover1_text_surface.get_rect(midbottom = scale_obj_position(1690, 250))

    gameover2_text_surface = gameover_font_2.render("back to menu", False, "White")
    gameover2_text_rect = gameover2_text_surface.get_rect(midbottom = scale_obj_position(1690, 350))

    gameover3_text_surface = gameover_font_2.render("quit", False, "White")
    gameover3_text_rect = gameover3_text_surface.get_rect(midbottom = scale_obj_position(1690, 450))





    player_input_rect = pygame.Rect(int(1400 * SCALE), int(230 * SCALE), int(175 * SCALE), int(80 * SCALE), )
    


    #game loop
    while True:
        #checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #player typing
            if event.type == pygame.KEYDOWN and player_can_type:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.unicode.isdigit() and len(user_text) < 9:
                    user_text += event.unicode
                elif event.unicode == "-" and user_text == "":
                    user_text += event.unicode
                elif event.unicode == "." and "." not in user_text and "/" not in user_text:
                    user_text += event.unicode
                elif event.unicode == "/" and "/" not in user_text and "." not in user_text:
                    user_text += event.unicode


                if event.key == pygame.K_RETURN: # when the enter key on the keyboard is pressed...
                    try:
                        if "/" in user_text:
                            player_answer = Fraction(user_text)
                        else:
                            player_answer = int(user_text)

                        if player_answer == question_crt_ans:
                            if current_player_spins >= 1:
                                player_can_type = False
                                question_active = False
                                print("correct")
                                print(question_crt_ans)
                               
                                
                                if op_choice == "+":
                                    if difficulty_value == 3:
                                        score_reward = int(bet_value * 5)
                                    else:
                                        score_reward = int(bet_value * 1.5)
                                elif op_choice == "-":
                                    if difficulty_value == 3:
                                        score_reward = int(bet_value * 6)
                                    else:
                                        score_reward = int(bet_value * 2)
                                elif op_choice == "x":
                                    if difficulty_value == 3:
                                        score_reward = int(bet_value * 7)
                                    else:
                                        score_reward = int(bet_value * 3)
                                elif op_choice == "/":
                                    score_reward = int(bet_value * 4)

                                current_player_score_display_value += score_reward
                                player_new_score = current_player_score_display_value
                                current_player_answered_correct += 1
                                total_answered_correct += 1

                                slots_1_text_surface = font_2.render("spin", False, "White")
                                slots_2_text_surface = font_2.render("2", False, "White")
                                slots_3_text_surface = font_2.render("win", False, "White")

                                question_crt_ans = None
                                
                                
                                

                                update_player_data(player_id, "current score", current_player_score_display_value)
                                if player_new_score > get_player_data(player_id, "highscore", default = 100):
                                    update_player_data(player_id, "highscore", player_new_score)

                                feedback_display_text_surface = font_2.render(str("0" + " "+ "+"+str(score_reward)), False, "White")
                                
                                score_display_text_surface = font_2.render(str(current_player_score_display_value), False, "White")
                                op_mult_display_text_surface = font_2.render(str("0"), False, "White")
                                crt_ans_text_surface = font_2.render(str(current_player_answered_correct), False, "White")
                                update_player_data(player_id, "current answered correctly", current_player_answered_correct)

                            else:
                                return
                        elif player_answer != question_crt_ans and current_player_score_display_value == 0:
                            game_state = "gameover"

                        else:
                            question_active = False
                            player_can_type = False

                            print("wrong")
                            feedback_display_text_surface = font_2.render(("wrong" +" "+ str(question_crt_ans)), False, "White")
                            print(question_crt_ans)

                            slots_1_text_surface = font_2.render("spin", False, "White")
                            slots_2_text_surface = font_2.render("2", False, "White")
                            slots_3_text_surface = font_2.render("win", False, "White")

                            question_crt_ans = None

                            op_mult_display_text_surface = font_2.render(str("0"), False, "White")

                                

                    except ValueError:
                        print("error")
                        feedback_display_text_surface = font_2.render(("error"), False, "White")
                        
                        slots_1_text_surface = font_2.render("spin", False, "White")
                        slots_2_text_surface = font_2.render("2", False, "White")
                        slots_3_text_surface = font_2.render("win", False, "White")

                        question_crt_ans = None
                        
                    user_text = ""





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
                        bet_amount_multi_text_surface = font_2.render(str(bet_amount_multi)+"x", False, "White")
                        
                    if bet_amount_multi > 1 and bet_decrease_amount_multi_rect.collidepoint(event.pos):
                        bet_amount_multi //= 10
                        bet_amount_multi_text_surface = font_2.render(str(bet_amount_multi)+"x", False, "White")
                #bet control
                    if bet_amount_multi > bet_value and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value = 1
                        bet_text_surface = font_2.render(str(bet_value), False, "White")
                        
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
                
                    if bet_value > 2 and bet_amount_multi == 1 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 1
                        bet_text_surface = font_2.render(str(bet_value), False, "White")

                    if bet_value > 2 and bet_amount_multi == 10 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 10
                        bet_text_surface = font_2.render(str(bet_value), False, "White")

                    if bet_value > 2 and bet_amount_multi == 100 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 100
                        bet_text_surface = font_2.render(str(bet_value), False, "White")

                    if bet_value > 2 and bet_amount_multi == 1000 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 1000
                        bet_text_surface = font_2.render(str(bet_value), False, "White")
                #options btn
                    if option_display_btn_rect.collidepoint(event.pos):
                        print("options")
                        feedback_display_text_surface = font_2.render(("options"), False, "White")
                #spin btn
                    if spin_btn_rect.collidepoint(event.pos):
 
                        if bet_value > current_player_score_display_value and current_player_score_display_value >= 1:
                            feedback_display_text_surface = font_2.render(str("u dont have enough coins"), False, "White")
                            current_player_spins += 1
                            total_spins += 1
                            current_player_score_display_value -= bet_value
                        else:

                            if question_active:
                                user_text = ""
                            else:
                                question_active = True

                            player_can_type = True
                            current_player_spins += 1
                            total_spins += 1

                            update_player_data(player_id, "current spins", current_player_spins)

                            if difficulty_value == 1:
                                if current_player_score_display_value >= 1:
                                    current_player_score_display_value -= bet_value
                                    update_player_data(player_id, "current score", current_player_score_display_value)
                                    score_display_text_surface = font_2.render(str(current_player_score_display_value), False, "White")

                                    question_crt_ans = None
                                    num1 = random.randint(1,30)
                                    num2 = random.randint(1,30)
                                    
                                    op_choice = random.choice(["+", "-"])

                                    slots_1_text_surface = font_2.render(str(num1), False, "White")
                                    slots_2_text_surface = font_2.render(str(op_choice), False, "White")
                                    slots_3_text_surface = font_2.render(str(num2), False, "White")

                                    if op_choice == "+":
                                        question_crt_ans = num1 + num2
                                    elif op_choice == "-":
                                        question_crt_ans = num1 - num2
                                    else:
                                        question_crt_ans = 0

                                
                            
                            elif difficulty_value == 2:
                                if current_player_score_display_value >= 1:
                                    current_player_score_display_value -= bet_value
                                    update_player_data(player_id, "current score", current_player_score_display_value)
                                    score_display_text_surface = font_2.render(str(current_player_score_display_value), False, "White")

                                    question_crt_ans = None
                                    num1 = random.randint(1,50)
                                    num2 = random.randint(1,50)
                                    
                                    op_choice = random.choice(["+", "-", "x", "/"])

                                    slots_1_text_surface = font_2.render(str(num1), False, "White")
                                    slots_2_text_surface = font_2.render(str(op_choice), False, "White")
                                    slots_3_text_surface = font_2.render(str(num2), False, "White")

                                    if op_choice == "+":
                                        question_crt_ans = num1 + num2
                                    elif op_choice == "-":
                                        question_crt_ans = num1 - num2
                                    if op_choice == "x":
                                        question_crt_ans = num1 * num2
                                    elif op_choice == "/":
                                        question_crt_ans = round(num1 / num2, 2)
                                    else:
                                        question_crt_ans = 0


                            elif difficulty_value == 3:
                                if current_player_score_display_value >= 1:
                                    current_player_score_display_value -= bet_value
                                    update_player_data(player_id, "current score", current_player_score_display_value)
                                    score_display_text_surface = font_2.render(str(current_player_score_display_value), False, "White")

                                    question_crt_ans = None
                                    num2 = random.randint(2,20)
                                    num1 = random.randint(1,num2 - 1)
                                    num4 = random.randint(2,20)
                                    num3 = random.randint(1,num4 - 1)
                                    
                                    op_choice = random.choice(["+", "-", "x"])


                                    question_type1 = "int"
                                    question_type2 = "fraction"

                                    questions = [question_type1, question_type2]
                                    question_choice = random.choice(questions)

                                    if question_choice == "int":
                                        slots_1_text_surface = font_2.render(str(num1), False, "White")
                                        slots_2_text_surface = font_2.render(str(op_choice), False, "White")
                                        slots_3_text_surface = font_2.render(str(num2), False, "White")

                                        if op_choice == "+":
                                            question_crt_ans = num1 + num2
                                        elif op_choice == "-":
                                            question_crt_ans = num1 - num2
                                        if op_choice == "x":
                                            question_crt_ans = num1 * num2
                                        else:
                                            question_crt_ans = 0
                                    
                                    else:
                                        fraction_1 = Fraction(num1, num2)
                                        fraction_2 = Fraction(num3, num4)

                                        slots_1_text_surface = font_2.render(str(num1) + "/" + str(num2), False, "White")
                                        slots_2_text_surface = font_2.render(str(op_choice), False, "White")
                                        slots_3_text_surface = font_2.render(str(num3) + "/" + str(num4), False, "White")
                

                                        if op_choice == "+":
                                            question_crt_ans = fraction_1 + fraction_2
                                        elif op_choice == "-":
                                            question_crt_ans = fraction_1 - fraction_2
                                        if op_choice == "x":
                                            question_crt_ans = fraction_1 * fraction_2
                                        else:
                                            question_crt_ans = 0


                        if op_choice == "+":
                            if difficulty_value == 3:
                                op_mult_display_text_surface = font_2.render(str("5"), False, "White")
                            else:
                                op_mult_display_text_surface = font_2.render(str("1.5"), False, "White")
                        elif op_choice == "-":
                            if difficulty_value == 3:
                                op_mult_display_text_surface = font_2.render(str("6"), False, "White")
                            else:
                                op_mult_display_text_surface = font_2.render(str("2"), False, "White")
                        elif op_choice == "x":
                            if difficulty_value == 3:
                                op_mult_display_text_surface = font_2.render(str("7"), False, "White")
                            else:
                                op_mult_display_text_surface = font_2.render(str("3"), False, "White")
                        elif op_choice == "/":
                            op_mult_display_text_surface = font_2.render(str("4"), False, "White")
        

                
                elif game_state == "gameover":
                    if play_again_btn_rect.collidepoint(event.pos):
                        game_state = "gameplay"
                        print("game state is gameplay")

                        current_player_score_display_value = 100
                        current_player_answered_correct = 0
                        current_player_spins = 0

                        score_display_text_surface = font_2.render(str("100"), False, "White")
                        crt_ans_text_surface = font_2.render(str("0"), False, "White")
                        op_mult_display_text_surface = font_2.render(str("0"), False, "White")

                        slots_1_text_surface = font_2.render("spin", False, "White")
                        slots_2_text_surface = font_2.render("2", False, "White")
                        slots_3_text_surface = font_2.render("win", False, "White")


                        update_player_data(player_id, "current score", current_player_score_display_value)
                        update_player_data(player_id, "current answered correctly", current_player_answered_correct)
                        update_player_data(player_id, "current spins", current_player_spins)
                        current_player_score_display_value = get_player_data(player_id, "current score", default= 100)
                        current_player_answered_correct = get_player_data(player_id, "current answered correctly", default = 0)
                        current_player_spins = get_player_data(player_id, "current spins", default = 0)


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
            screen.blit(bg_image, (0,0))
            screen.blit(title_text_surface, title_text_rect)
            screen.blit(play_btn_surface, play_btn_rect)
            screen.blit(play_text_surface, play_text_rect)
            screen.blit(quit_btn_surface, quit_btn_rect)

        #gameplay page
        elif game_state == "gameplay":
            screen.blit(bg_image, (0,0))
            
            screen.blit(payout_btn_surface, payout_btn_rect)
            screen.blit(gui_hub_img, btn_hub_rect)
            screen.blit(diff_hub_img, diff_hub_rect)
            screen.blit(bet_hub_img, bet_hub_rect)
            screen.blit(slots_machine_surface, slots_machine_rect)
            screen.blit(diff_increase_btn_img, diff_increase_btn_rect)
            screen.blit(diff_display_surface, diff_display_rect)
            screen.blit(diff_decrease_btn_img, diff_decrease_btn_rect)
            screen.blit(op_mult_display_surface, op_mult_display_rect)
            screen.blit(bet_increase_btn_img, bet_increase_btn_rect)
            screen.blit(bet_display_surface, bet_display_rect)
            screen.blit(bet_decrease_btn_img, bet_decrease_btn_rect)
            screen.blit(bet_increase_amount_multi_img, bet_increase_amount_multi_rect)
            screen.blit(bet_amount_multi_display_surface, bet_amount_multi_display_rect)
            screen.blit(bet_decrease_amount_multi_img, bet_decrease_amount_multi_rect)
            screen.blit(spin_btn_img, spin_btn_rect)
            screen.blit(crt_ans_img, crt_ans_rect)
            screen.blit(option_display_btn_img, option_display_btn_rect)
            screen.blit(score_display_surface, score_display_rect)
            screen.blit(slots_1_surface, slots_1_rect)
            screen.blit(slots_2_surface, slots_2_rect)
            screen.blit(slots_3_surface, slots_3_rect)
            screen.blit(feedback_display_surface, feedback_display_rect)

            screen.blit(diff_text_surface, diff_text_rect)
            screen.blit(bet_text_surface, bet_text_rect)
            screen.blit(bet_amount_multi_text_surface, bet_amount_multi_text_rect)
            screen.blit(option_display_btn_text_surface, option_display_btn_text_rect)
            screen.blit(crt_ans_text_surface, crt_ans_text_rect)
            screen.blit(score_display_text_surface, score_display_text_rect)
            screen.blit(spin_btn_text_surface, spin_btn_text_rect)
            screen.blit(slots_1_text_surface, slots_1_text_rect)
            screen.blit(slots_2_text_surface, slots_2_text_rect)
            screen.blit(slots_3_text_surface, slots_3_text_rect)
            screen.blit(op_mult_display_text_surface, op_mult_display_text_rect)
            screen.blit(feedback_display_text_surface, feedback_display_text_rect)

            pygame.draw.rect(screen,"White", player_input_rect, 4)

            player_answer_text_surface = font_2.render((user_text), False, "White")

            screen.blit(player_answer_text_surface, (player_input_rect.x + 20, player_input_rect.y + 30))
            
            

            


            screen.blit(quit_btn_surface, quit_btn_rect)
        
        #gameover page
        elif game_state == "gameover":
            screen.blit(bg_image, (0,0))
            screen.blit(gameover_title_text_surface, gameover_title_text_rect)
            screen.blit(gameover1_btn_surface, play_again_btn_rect)
            screen.blit(gameover2_btn_surface, gameover2_btn_rect)
            screen.blit(gameover3_btn_surface, gameover3_btn_rect)
            screen.blit(gameover1_text_surface, gameover1_text_rect)
            screen.blit(gameover2_text_surface, gameover2_text_rect)
            screen.blit(gameover3_text_surface, gameover3_text_rect)
            screen.blit(quit_btn_surface, quit_btn_rect)

        #continuous updates the game
        pygame.display.flip()
        clock.tick(FPS)

