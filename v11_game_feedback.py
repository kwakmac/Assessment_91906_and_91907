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
    CHILL_BLUE = (69, 146, 255)
    BLACK = (0,0,0)


    #displays the program
    screen = pygame.display.set_mode(monitor_size, pygame.NOFRAME) #.NOFRAME displays just the screen. there is no top right options
    pygame.display.set_caption("game")


    bg_size = (scale_obj_size(1920, 1080))
    bg_image = pygame.transform.scale(pygame.image.load("bg1.png"),bg_size).convert_alpha()
              

    clock = pygame.time.Clock()

    font_17 = pygame.font.Font("gvhs-gothic.ttf", 17)
    font_20 = pygame.font.Font("gvhs-gothic.ttf", 20)
    font_23 = pygame.font.Font("gvhs-gothic.ttf", 23)
    font_40 = pygame.font.Font("gvhs-gothic.ttf", 40)
    font_50 = pygame.font.Font("gvhs-gothic.ttf", 50)
    font_60 = pygame.font.Font("gvhs-gothic.ttf", 60)

    #---------------------------- menu page -----------
    play_btn_size = (scale_obj_size(300,75))
    play_btn_img = pygame.transform.scale(pygame.image.load("button.png"),play_btn_size).convert_alpha()
    play_btn_rect = play_btn_img.get_rect(midbottom = scale_obj_position(1690, 250))

    menu_quit_size = (scale_obj_size(300,75))
    menu_quit_img = pygame.transform.scale(pygame.image.load("button.png"),menu_quit_size).convert_alpha()
    menu_quit_rect = menu_quit_img.get_rect(midbottom = scale_obj_position(1690, 350))


    title_text_surface = font_40.render("math add-it", False, "White")
    title_text_rect = title_text_surface.get_rect(midbottom = scale_obj_position(1390, 100))

    play_text_surface = font_20.render("play", False, "White")
    play_text_rect = play_text_surface.get_rect(midbottom = scale_obj_position(1690, 230))

    menu_quit_text_surface = font_20.render("quit", False, "White")
    menu_quit_text_rect = menu_quit_text_surface.get_rect(midbottom = scale_obj_position(1690, 330))


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

    slots_machine_size = (scale_obj_size(1130, 360))
    slots_machine_img = pygame.transform.scale(pygame.image.load("slots_display.png"),slots_machine_size).convert_alpha()
    slots_machine_rect = slots_machine_img.get_rect(midbottom = scale_obj_position(725, 610))

    slots_size = (scale_obj_size(320, 300))
    slots_1_img = pygame.transform.scale(pygame.image.load("slots.png"),slots_size).convert_alpha()
    slots_1_rect = slots_1_img.get_rect(midbottom = scale_obj_position(365, 579))

    slots_2_img = pygame.transform.scale(pygame.image.load("slots.png"),slots_size).convert_alpha()
    slots_2_rect = slots_2_img.get_rect(midbottom = scale_obj_position(725, 579))

    slots_3_img = pygame.transform.scale(pygame.image.load("slots.png"),slots_size).convert_alpha()
    slots_3_rect = slots_3_img.get_rect(midbottom = scale_obj_position(1085, 579))

    spin_btn_size = (scale_obj_size(180, 282))
    spin_btn_img = pygame.transform.scale(pygame.image.load("spin_btn.png"),spin_btn_size).convert_alpha()
    spin_btn_rect = spin_btn_img.get_rect(midbottom = scale_obj_position(1647, 985))

    diff_increase_btn_size = (scale_obj_size(50, 50))
    diff_increase_btn_img = pygame.transform.scale(pygame.image.load("arrow_up.png"),diff_increase_btn_size).convert_alpha()
    diff_increase_btn_rect = diff_increase_btn_img.get_rect(midbottom = scale_obj_position(747, 790))

    diff_display_size = (scale_obj_size(100, 70))
    diff_display_img = pygame.transform.scale(pygame.image.load("diff_display.png"),diff_display_size).convert_alpha()
    diff_display_rect = diff_display_img.get_rect(midbottom = scale_obj_position(747, 880))

    diff_decrease_btn_size = (scale_obj_size(50, 50))
    diff_decrease_btn_img = pygame.transform.scale(pygame.image.load("arrow_down.png"),diff_decrease_btn_size).convert_alpha()
    diff_decrease_btn_rect = diff_decrease_btn_img.get_rect(midbottom = scale_obj_position(747, 947))

    op_mult_display_size = (scale_obj_size(90, 70))
    op_mult_display_img = pygame.transform.scale(pygame.image.load("op_multi.png"),op_mult_display_size).convert_alpha()
    op_mult_display_rect = op_mult_display_img.get_rect(midbottom = scale_obj_position(1420, 837))

    bet_increase_btn_size = (scale_obj_size(50, 50))
    bet_increase_btn_img = pygame.transform.scale(pygame.image.load("arrow_right.png"),bet_increase_btn_size).convert_alpha()
    bet_increase_btn_rect = bet_increase_btn_img.get_rect(midbottom = scale_obj_position(1217, 826))

    bet_display_size = (scale_obj_size(150, 70))
    bet_display_img = pygame.transform.scale(pygame.image.load("bet_display.png"),bet_display_size).convert_alpha()
    bet_display_rect = bet_display_img.get_rect(midbottom = scale_obj_position(1095, 837))

    bet_decrease_btn_size = (scale_obj_size(50, 50))
    bet_decrease_btn_img = pygame.transform.scale(pygame.image.load("arrow_left.png"),bet_decrease_btn_size).convert_alpha()
    bet_decrease_btn_rect = bet_decrease_btn_img.get_rect(midbottom = scale_obj_position(973, 826))

    bet_increase_amount_multi_size = (scale_obj_size(50, 50))
    bet_increase_amount_multi_img = pygame.transform.scale(pygame.image.load("arrow_right.png"),bet_increase_amount_multi_size).convert_alpha()
    bet_increase_amount_multi_rect = bet_increase_amount_multi_img.get_rect(midbottom = scale_obj_position(1173, 911))

    bet_amount_multi_display_size = (scale_obj_size(60, 60))
    bet_amount_multi_display_img = pygame.transform.scale(pygame.image.load("bet_multi.png"),bet_amount_multi_display_size).convert_alpha()
    bet_amount_multi_display_rect = bet_amount_multi_display_img.get_rect(midbottom = scale_obj_position(1095, 915))

    bet_decrease_amount_multi_size = (scale_obj_size(50, 50))
    bet_decrease_amount_multi_img = pygame.transform.scale(pygame.image.load("arrow_left.png"),bet_decrease_amount_multi_size).convert_alpha()
    bet_decrease_amount_multi_rect = bet_decrease_amount_multi_img.get_rect(midbottom = scale_obj_position(1018, 911))

    crt_ans_size = (scale_obj_size(150, 145))
    crt_ans_img = pygame.transform.scale(pygame.image.load("crt_ans.png"),crt_ans_size).convert_alpha()
    crt_ans_rect = crt_ans_img.get_rect(midbottom = scale_obj_position(470, 985))

    option_display_btn_size = (scale_obj_size(150, 145))
    option_display_btn_img = pygame.transform.scale(pygame.image.load("opt_btn.png"),option_display_btn_size).convert_alpha()
    option_display_btn_rect = option_display_btn_img.get_rect(midbottom = scale_obj_position(290, 985))

    score_display_size = (scale_obj_size(410, 110))
    score_display_img = pygame.transform.scale(pygame.image.load("score_display.png"),score_display_size).convert_alpha()
    score_display_rect = score_display_img.get_rect(midbottom = scale_obj_position(385, 814))

    feedback_display_size = (scale_obj_size(1000, 150))
    feedback_display_img = pygame.transform.scale(pygame.image.load("feedback_grey.png"),feedback_display_size).convert_alpha()
    feedback_display_rect = feedback_display_img.get_rect(midbottom = scale_obj_position(960, 200))

    #------------------------ gameplay font ----------------------    

    diff_text_surface = font_20.render("1", False, "White")
    diff_text_rect = diff_text_surface.get_rect(midbottom = scale_obj_position(747, 860))

    bet_text_surface = font_20.render("100", False, "White")
    bet_text_rect = bet_text_surface.get_rect(midbottom = scale_obj_position(1095, 817))

    bet_amount_multi_text_surface = font_20.render("1"+"x", False, "White")
    bet_amount_multi_text_rect = bet_amount_multi_text_surface.get_rect(midbottom = scale_obj_position(1095, 895))

    op_mult_display_text_surface = font_20.render("0", False, "White")
    op_mult_display_text_rect = op_mult_display_text_surface.get_rect(midbottom = scale_obj_position(1420, 817))

    option_display_btn_text_surface = font_20.render("options", False, "White")
    option_display_btn_text_rect = option_display_btn_text_surface.get_rect(midbottom = scale_obj_position(290, 925))

    crt_ans_text_surface = font_20.render(str(current_player_answered_correct), False, "White")
    crt_ans_text_rect = crt_ans_text_surface.get_rect(midbottom = scale_obj_position(470, 955))

    crt_ans_text1_surface = font_17.render(("CORRECTLY"), False, "White")
    crt_ans_text1_rect = crt_ans_text_surface.get_rect(midbottom = scale_obj_position(420, 880))

    crt_ans_text2_surface = font_17.render(("ANSWERED"), False, "White")
    crt_ans_text2_rect = crt_ans_text_surface.get_rect(midbottom = scale_obj_position(425, 905))

    score_display_text_surface = font_20.render(str(current_player_score_display_value), False, "White")
    score_display_text_rect = score_display_text_surface.get_rect(midbottom = scale_obj_position(385, 794))

    score_display_text1_surface = font_20.render(("SCORE"), False, "White")
    score_display_text1_rect = score_display_text1_surface.get_rect(midbottom = scale_obj_position(385, 745))

    spin_btn_text_surface = font_20.render("spin", False, "White")
    spin_btn_text_rect = spin_btn_text_surface.get_rect(midbottom = scale_obj_position(1647, 945))

    slots_1_text_surface = font_60.render("spin", False, "White")
    slots_1_text_rect = slots_1_text_surface.get_rect(midbottom = scale_obj_position(350, 470))

    slots_2_text_surface = font_60.render("2", False, "White")
    slots_2_text_rect = slots_2_text_surface.get_rect(midbottom = scale_obj_position(710, 470))

    slots_3_text_surface = font_60.render("win", False, "White")
    slots_3_text_rect = slots_3_text_surface.get_rect(midbottom = scale_obj_position(1070, 470))

    feedback_display_text_surface = font_50.render("", False, "White")
    feedback_display_text_rect = feedback_display_text_surface.get_rect(midbottom = scale_obj_position(500, 150))

    multi_text_surface = font_40.render("X", False, "White")
    multi_text_rect = multi_text_surface.get_rect(midbottom = scale_obj_position(1300, 827))

    equal_text_surface = font_60.render("=", False, "White")
    equal_text_rect = equal_text_surface.get_rect(midbottom = scale_obj_position(1375, 480))



    #---------------------------- game over page -----------
    play_again_btn_size = (scale_obj_size(300,75))
    play_again_btn_img = pygame.transform.scale(pygame.image.load("button.png"),play_again_btn_size).convert_alpha()
    play_again_btn_rect = play_again_btn_img.get_rect(midbottom = scale_obj_position(1690, 250))

    gameover_back_menu_btn_size = (scale_obj_size(300,75))
    gameover_back_menu_btn_img = pygame.transform.scale(pygame.image.load("button.png"),gameover_back_menu_btn_size).convert_alpha()
    gameover_back_menu_btn_rect = gameover_back_menu_btn_img.get_rect(midbottom = scale_obj_position(1690, 350))

    gameover_quit_btn_size = (scale_obj_size(300,75))    
    gameover_quit_btn_img = pygame.transform.scale(pygame.image.load("button.png"),gameover_quit_btn_size).convert_alpha()
    gameover_quit_btn_rect = gameover_quit_btn_img.get_rect(midbottom = scale_obj_position(1690, 450))

    gameover_title_text_surface = font_40.render("game over", False, "White")
    gameover_title_text_rect = gameover_title_text_surface.get_rect(midbottom = scale_obj_position(1390, 100))

    play_again_text_surface = font_20.render("play again", False, "White")
    play_again_text_rect = play_again_text_surface.get_rect(midbottom = scale_obj_position(1690, 230))

    gameover_back_menu_text_surface = font_20.render("back to menu", False, "White")
    gameover_back_menu_text_rect = gameover_back_menu_text_surface.get_rect(midbottom = scale_obj_position(1690, 330))

    gameover_quit_text_surface = font_20.render("quit", False, "White")
    gameover_quit_text_rect = gameover_quit_text_surface.get_rect(midbottom = scale_obj_position(1690, 430))


    #------------------------------- options menu-----------------------------

    back_to_menu_size = (scale_obj_size(300,75))
    back_to_menu_img = pygame.transform.scale(pygame.image.load("button.png"),back_to_menu_size).convert_alpha()
    back_to_menu_rect = back_to_menu_img.get_rect(midbottom = scale_obj_position(1690, 250))

    options_quit_size = (scale_obj_size(300,75))    
    options_quit_img = pygame.transform.scale(pygame.image.load("button.png"),options_quit_size).convert_alpha()
    options_quit_rect = options_quit_img.get_rect(midbottom = scale_obj_position(1690, 350))

    back_to_game_size = (scale_obj_size(300,75))    
    back_to_game_img = pygame.transform.scale(pygame.image.load("button1.png"),back_to_game_size).convert_alpha()
    back_to_game_rect = back_to_game_img.get_rect(midbottom = scale_obj_position(1690, 450))

    option_title_text_surface = font_40.render("options", False, "White")
    option_title_text_rect = option_title_text_surface.get_rect(midbottom = scale_obj_position(1390, 100))

    back_to_menu_text_surface = font_20.render("back to menu", False, "White")
    back_to_menu_text_rect = back_to_menu_text_surface.get_rect(midbottom = scale_obj_position(1690, 230))

    back_to_game_text_surface = font_20.render("back", False, "White")
    back_to_game_text_rect = back_to_game_text_surface.get_rect(midbottom = scale_obj_position(1690, 430))

    options_quit_text_surface = font_20.render("quit", False, "White")
    options_quit_text_rect = options_quit_text_surface.get_rect(midbottom = scale_obj_position(1690, 330))




    player_input_rect = pygame.Rect(int(1465 * SCALE), int(393 * SCALE), int(290 * SCALE), int(100 * SCALE), )
    


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
                                        score_reward = round(bet_value * 5)
                                    else:
                                        score_reward = round(bet_value * 1.5)
                                elif op_choice == "-":
                                    if difficulty_value == 3:
                                        score_reward = round(bet_value * 6)
                                    else:
                                        score_reward = round(bet_value * 2)
                                elif op_choice == "x":
                                    if difficulty_value == 3:
                                        score_reward = round(bet_value * 7)
                                    else:
                                        score_reward = round(bet_value * 3)
                                elif op_choice == "/":
                                    score_reward = round(bet_value * 4)

                                current_player_score_display_value += score_reward
                                player_new_score = current_player_score_display_value
                                current_player_answered_correct += 1
                                total_answered_correct += 1

                                slots_1_text_surface = font_60.render("spin", False, "White")
                                slots_2_text_surface = font_60.render("2", False, "White")
                                slots_3_text_surface = font_60.render("win", False, "White")

                                question_crt_ans = None
                                
                                
                                

                                update_player_data(player_id, "current score", current_player_score_display_value)
                                if player_new_score > get_player_data(player_id, "highscore", default = 100):
                                    update_player_data(player_id, "highscore", player_new_score)

                                feedback_display_img = pygame.transform.scale(pygame.image.load("feedback_green.png"),feedback_display_size).convert_alpha()
                                
                                score_display_text_surface = font_20.render(str(current_player_score_display_value), False, "White")
                                op_mult_display_text_surface = font_20.render(str("0"), False, "White")
                                crt_ans_text_surface = font_20.render(str(current_player_answered_correct), False, "White")
                                update_player_data(player_id, "current answered correctly", current_player_answered_correct)

                            else:
                                return
                        elif player_answer != question_crt_ans and current_player_score_display_value == 0:
                            game_state = "gameover"

                        else:
                            question_active = False
                            player_can_type = False

                            print("wrong")
                            feedback_display_img = pygame.transform.scale(pygame.image.load("feedback_red.png"),feedback_display_size).convert_alpha()
    
                            print(question_crt_ans)

                            slots_1_text_surface = font_60.render("spin", False, "White")
                            slots_2_text_surface = font_60.render("2", False, "White")
                            slots_3_text_surface = font_60.render("win", False, "White")

                            question_crt_ans = None

                            op_mult_display_text_surface = font_20.render(str("0"), False, "White")

                                

                    except ValueError:
                        print("error")
                        feedback_display_img = pygame.transform.scale(pygame.image.load("feedback_red.png"),feedback_display_size).convert_alpha()
    
                        slots_1_text_surface = font_60.render("spin", False, "White")
                        slots_2_text_surface = font_60.render("2", False, "White")
                        slots_3_text_surface = font_60.render("win", False, "White")

                        question_crt_ans = None
                        
                    user_text = ""





            #game mechanics/ how game works
            if event.type == pygame.MOUSEBUTTONUP:
                
                if game_state == "menu":
                    if current_player_score_display_value == 0 and play_btn_rect.collidepoint(event.pos):
                        game_state = "gameplay"
                        print("game state is gameplay, but game reset")

                        current_player_score_display_value = 100
                        current_player_answered_correct = 0
                        current_player_spins = 0

                        score_display_text_surface = font_20.render(str("100"), False, "White")
                        crt_ans_text_surface = font_20.render(str("0"), False, "White")
                        op_mult_display_text_surface = font_20.render(str("0"), False, "White")

                        slots_1_text_surface = font_60.render("spin", False, "White")
                        slots_2_text_surface = font_60.render("2", False, "White")
                        slots_3_text_surface = font_60.render("win", False, "White")


                        update_player_data(player_id, "current score", current_player_score_display_value)
                        update_player_data(player_id, "current answered correctly", current_player_answered_correct)
                        update_player_data(player_id, "current spins", current_player_spins)
                        current_player_score_display_value = get_player_data(player_id, "current score", default= 100)
                        current_player_answered_correct = get_player_data(player_id, "current answered correctly", default = 0)
                        current_player_spins = get_player_data(player_id, "current spins", default = 0)
                    else:
                        game_state = "gameplay"
                        print("game state is gameplay")

                    if menu_quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()



                elif game_state == "gameplay":
                    if payout_btn_rect.collidepoint(event.pos):
                        game_state = "gameover"
                        print("game state is game over")
                #difficulty control
                    if difficulty_value < 3 and diff_increase_btn_rect.collidepoint(event.pos):
                        difficulty_value += 1
                        diff_text_surface = font_20.render(str(difficulty_value), False, "White")
                        
                    if difficulty_value > 1 and diff_decrease_btn_rect.collidepoint(event.pos):
                        difficulty_value -= 1
                        diff_text_surface = font_20.render(str(difficulty_value), False, "White")
                #bet amount multi
                    if bet_amount_multi < 1000 and bet_increase_amount_multi_rect.collidepoint(event.pos):
                        bet_amount_multi *= 10
                        bet_amount_multi_text_surface = font_20.render(str(bet_amount_multi)+"x", False, "White")
                        
                    if bet_amount_multi > 1 and bet_decrease_amount_multi_rect.collidepoint(event.pos):
                        bet_amount_multi //= 10
                        bet_amount_multi_text_surface = font_20.render(str(bet_amount_multi)+"x", False, "White")
                #bet control
                    if bet_amount_multi > bet_value and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value = 1
                        bet_text_surface = font_20.render(str(bet_value), False, "White")
                        
                    if bet_value < 10000 and bet_amount_multi == 1 and bet_increase_btn_rect.collidepoint(event.pos):
                        bet_value += 1
                        bet_text_surface = font_20.render(str(bet_value), False, "White")

                    if bet_value < 10000 and bet_amount_multi == 10 and bet_increase_btn_rect.collidepoint(event.pos):
                        bet_value += 10
                        bet_text_surface = font_20.render(str(bet_value), False, "White")

                    if bet_value < 10000 and bet_amount_multi == 100 and bet_increase_btn_rect.collidepoint(event.pos):
                        bet_value += 100
                        bet_text_surface = font_20.render(str(bet_value), False, "White")

                    if bet_value < 10000 and bet_amount_multi == 1000 and bet_increase_btn_rect.collidepoint(event.pos):
                        bet_value += 1000
                        bet_text_surface = font_20.render(str(bet_value), False, "White")
                
                    if bet_value > 2 and bet_amount_multi == 1 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 1
                        bet_text_surface = font_20.render(str(bet_value), False, "White")

                    if bet_value > 2 and bet_amount_multi == 10 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 10
                        bet_text_surface = font_20.render(str(bet_value), False, "White")

                    if bet_value > 2 and bet_amount_multi == 100 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 100
                        bet_text_surface = font_20.render(str(bet_value), False, "White")

                    if bet_value > 2 and bet_amount_multi == 1000 and bet_decrease_btn_rect.collidepoint(event.pos):
                        bet_value -= 1000
                        bet_text_surface = font_20.render(str(bet_value), False, "White")
                #options btn
                    if option_display_btn_rect.collidepoint(event.pos):
                        game_state = "options"
                        print("options")

                        
                #spin btn
                    if spin_btn_rect.collidepoint(event.pos):
                        
                        feedback_display_img = pygame.transform.scale(pygame.image.load("feedback_grey.png"),feedback_display_size).convert_alpha()
    
                        if current_player_score_display_value < bet_value :
                            feedback_display_text_surface = font_50.render(str("u dont have enough coins"), False, "White")


                        else:

                            if question_active:
                                user_text = ""
                            else:
                                question_active = True

                            player_can_type = True
                            current_player_spins += 1
                            total_spins += 1

                            update_player_data(player_id, "current spins", current_player_spins)

                            current_player_score_display_value -= bet_value
                            update_player_data(player_id, "current score", current_player_score_display_value)
                            score_display_text_surface = font_20.render(str(current_player_score_display_value), False, "White")
                            feedback_display_text_surface = font_50.render(str(""), False, "White")


                            if difficulty_value == 1:
                                
                                question_crt_ans = None
                                num1 = random.randint(1,30)
                                num2 = random.randint(1,30)
                                
                                op_choice = random.choice(["+", "-"])

                                slots_1_text_surface = font_60.render(str(num1), False, "White")
                                slots_2_text_surface = font_60.render(str(op_choice), False, "White")
                                slots_3_text_surface = font_60.render(str(num2), False, "White")

                                if op_choice == "+":
                                    question_crt_ans = num1 + num2
                                elif op_choice == "-":
                                    question_crt_ans = num1 - num2
                                else:
                                    question_crt_ans = 0

                                
                            
                            elif difficulty_value == 2:
                                question_crt_ans = None
                                num1 = random.randint(1,50)
                                num2 = random.randint(1,50)
                                
                                op_choice = random.choice(["+", "-", "x", "/"])

                                slots_1_text_surface = font_60.render(str(num1), False, "White")
                                slots_2_text_surface = font_60.render(str(op_choice), False, "White")
                                slots_3_text_surface = font_60.render(str(num2), False, "White")

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
                                    slots_1_text_surface = font_60.render(str(num1), False, "White")
                                    slots_2_text_surface = font_60.render(str(op_choice), False, "White")
                                    slots_3_text_surface = font_60.render(str(num2), False, "White")

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

                                    slots_1_text_surface = font_60.render(str(num1) + "/" + str(num2), False, "White")
                                    slots_2_text_surface = font_60.render(str(op_choice), False, "White")
                                    slots_3_text_surface = font_60.render(str(num3) + "/" + str(num4), False, "White")
            

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
                                op_mult_display_text_surface = font_20.render(str("5"), False, "White")
                            else:
                                op_mult_display_text_surface = font_20.render(str("1.5"), False, "White")
                        elif op_choice == "-":
                            if difficulty_value == 3:
                                op_mult_display_text_surface = font_20.render(str("6"), False, "White")
                            else:
                                op_mult_display_text_surface = font_20.render(str("2"), False, "White")
                        elif op_choice == "x":
                            if difficulty_value == 3:
                                op_mult_display_text_surface = font_20.render(str("7"), False, "White")
                            else:
                                op_mult_display_text_surface = font_20.render(str("3"), False, "White")
                        elif op_choice == "/":
                            op_mult_display_text_surface = font_20.render(str("4"), False, "White")


                
                elif game_state == "gameover":
                    if play_again_btn_rect.collidepoint(event.pos):
                        game_state = "gameplay"
                        print("game state is gameplay")

                        current_player_score_display_value = 100
                        current_player_answered_correct = 0
                        current_player_spins = 0

                        score_display_text_surface = font_20.render(str("100"), False, "White")
                        crt_ans_text_surface = font_20.render(str("0"), False, "White")
                        op_mult_display_text_surface = font_20.render(str("0"), False, "White")

                        slots_1_text_surface = font_60.render("spin", False, "White")
                        slots_2_text_surface = font_60.render("2", False, "White")
                        slots_3_text_surface = font_60.render("win", False, "White")


                        update_player_data(player_id, "current score", current_player_score_display_value)
                        update_player_data(player_id, "current answered correctly", current_player_answered_correct)
                        update_player_data(player_id, "current spins", current_player_spins)
                        current_player_score_display_value = get_player_data(player_id, "current score", default= 100)
                        current_player_answered_correct = get_player_data(player_id, "current answered correctly", default = 0)
                        current_player_spins = get_player_data(player_id, "current spins", default = 0)


                    elif gameover_back_menu_btn_rect.collidepoint(event.pos):
                        game_state = "menu"
                        print("game state is menu")

                        current_player_score_display_value = 100
                        current_player_answered_correct = 0
                        current_player_spins = 0

                        score_display_text_surface = font_20.render(str("100"), False, "White")
                        crt_ans_text_surface = font_20.render(str("0"), False, "White")
                        op_mult_display_text_surface = font_20.render(str("0"), False, "White")

                        slots_1_text_surface = font_60.render("spin", False, "White")
                        slots_2_text_surface = font_60.render("2", False, "White")
                        slots_3_text_surface = font_60.render("win", False, "White")


                        update_player_data(player_id, "current score", current_player_score_display_value)
                        update_player_data(player_id, "current answered correctly", current_player_answered_correct)
                        update_player_data(player_id, "current spins", current_player_spins)
                        current_player_score_display_value = get_player_data(player_id, "current score", default= 100)
                        current_player_answered_correct = get_player_data(player_id, "current answered correctly", default = 0)
                        current_player_spins = get_player_data(player_id, "current spins", default = 0)

                    elif gameover_quit_btn_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                elif game_state == "options":
                    if back_to_menu_rect.collidepoint(event.pos):
                        game_state = "menu"

                    if back_to_game_rect.collidepoint(event.pos):
                        game_state = "gameplay"

                    if options_quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()


            

            


                
    #drawing (displaying sprites/objects)
        #menu page
        if game_state == "menu":
            screen.blit(bg_image, (0,0))
            screen.blit(title_text_surface, title_text_rect)
            screen.blit(play_btn_img, play_btn_rect)
            screen.blit(menu_quit_img, menu_quit_rect)
            screen.blit(play_text_surface, play_text_rect)
            screen.blit(menu_quit_text_surface, menu_quit_text_rect)

        #gameplay page
        elif game_state == "gameplay":
            screen.blit(bg_image, (0,0))
            
            screen.blit(payout_btn_surface, payout_btn_rect)
            screen.blit(gui_hub_img, btn_hub_rect)
            screen.blit(diff_hub_img, diff_hub_rect)
            screen.blit(bet_hub_img, bet_hub_rect)
            screen.blit(slots_machine_img, slots_machine_rect)
            screen.blit(diff_increase_btn_img, diff_increase_btn_rect)
            screen.blit(diff_display_img, diff_display_rect)
            screen.blit(diff_decrease_btn_img, diff_decrease_btn_rect)
            screen.blit(op_mult_display_img, op_mult_display_rect)
            screen.blit(bet_increase_btn_img, bet_increase_btn_rect)
            screen.blit(bet_display_img, bet_display_rect)
            screen.blit(bet_decrease_btn_img, bet_decrease_btn_rect)
            screen.blit(bet_increase_amount_multi_img, bet_increase_amount_multi_rect)
            screen.blit(bet_amount_multi_display_img, bet_amount_multi_display_rect)
            screen.blit(bet_decrease_amount_multi_img, bet_decrease_amount_multi_rect)
            screen.blit(spin_btn_img, spin_btn_rect)
            screen.blit(crt_ans_img, crt_ans_rect)
            screen.blit(option_display_btn_img, option_display_btn_rect)
            screen.blit(score_display_img, score_display_rect)
            screen.blit(slots_1_img, slots_1_rect)
            screen.blit(slots_2_img, slots_2_rect)
            screen.blit(slots_3_img, slots_3_rect)
            screen.blit(feedback_display_img, feedback_display_rect)

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
            screen.blit(multi_text_surface, multi_text_rect)
            screen.blit(equal_text_surface, equal_text_rect)
            screen.blit(crt_ans_text1_surface, crt_ans_text1_rect)
            screen.blit(score_display_text1_surface, score_display_text1_rect)
            screen.blit(crt_ans_text2_surface, crt_ans_text2_rect)


            user_input_size = (player_input_rect.w, player_input_rect.h)
            user_input_img = pygame.transform.scale(pygame.image.load("user_input.png"),user_input_size).convert_alpha()
            
            player_answer_text_surface = font_23.render((user_text), False, "White")

            screen.blit(user_input_img, player_input_rect)
            screen.blit(player_answer_text_surface, (player_input_rect.x + 20, player_input_rect.y + 20))
            
        
        #gameover page
        elif game_state == "gameover":
            screen.blit(bg_image, (0,0))
            screen.blit(gameover_title_text_surface, gameover_title_text_rect)
            screen.blit(play_again_btn_img, play_again_btn_rect)
            screen.blit(gameover_back_menu_btn_img, gameover_back_menu_btn_rect)
            screen.blit(gameover_quit_btn_img, gameover_quit_btn_rect)
            screen.blit(play_again_text_surface, play_again_text_rect)
            screen.blit(gameover_back_menu_text_surface, gameover_back_menu_text_rect)
            screen.blit(gameover_quit_text_surface, gameover_quit_text_rect)

        elif game_state == "options":
            screen.fill(CHILL_BLUE)
            screen.blit(option_title_text_surface, option_title_text_rect)
            screen.blit(back_to_menu_img, back_to_menu_rect)
            screen.blit(back_to_game_img, back_to_game_rect)
            screen.blit(options_quit_img, options_quit_rect)
            screen.blit(back_to_menu_text_surface, back_to_menu_text_rect)
            screen.blit(back_to_game_text_surface, back_to_game_text_rect)
            screen.blit(options_quit_text_surface, options_quit_text_rect)


        #continuous updates the game
        pygame.display.flip()
        clock.tick(FPS)

