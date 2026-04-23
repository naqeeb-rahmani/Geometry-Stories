import tkinter as tk 
from PIL import Image, ImageTk
#---------screen-----------#
root = tk.Tk()
root.title("Geometry Stories")
root.geometry("1280x720")
root.configure(bg="white")
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()
#--------------------------#

#----variables----#

in_menu = True
game_running = False
game_mode = None # play or continue
scene_nr = 0

choice = None #False = choice 1 and True = choice 2

########################

#---menu buttons---#

def exit_menu():
    global in_menu, game_running
    in_menu = False
    game_running = True
    canvas.delete("all")
    game_code()     

def next_scene_1():
    global scene_nr
    global choice

    if scene_nr == 2 and choice == False:
        to_menu()
    else:

        choice = False
    
        scene_nr += 1
    game_code()

def next_scene_2():
    global scene_nr
    global choice
    
    if scene_nr == 2:
        to_menu()
    else:

        choice = True

        scene_nr += 1
    game_code()

def exit_menu_and_set_scene_1():
    global scene_nr
    scene_nr += 1
    exit_menu()

play = tk.Button(
    root, 
    text="Play", 
    command=exit_menu_and_set_scene_1,
    font=("Arial", 20),
    bg="#B0C4DE",
    width=10,
    height=1
)

##############################

#---menu---#
menu_bg = ImageTk.PhotoImage(Image.open("assets\Menu.png"))
canvas.create_image(-50,0, anchor="nw", image=menu_bg)

canvas.create_window(600, 300,anchor="center", window=play)


##########################

#---scene variables---#
scene1_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\Scene1.png"))

scene2_c1_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\Scene2.png"))
scene2_c2_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\you_died.png"))

scene3_c1_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\scene3_if_conf.png"))
scene3_c2_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\second_last_scene_if_sneaky.png"))



scene_text_var = "Ugh... my head. What happened? Did i pass out? \nOh, no. Why isnt anyone moving. Could it be that i'm the only one alive?"



choice_1 = tk.Button(
    root, 
    text="Look around", 
    command=next_scene_1,
    font=("Arial", 20),
    bg="#B0C4DE",
    width=10,
    height=1
)

choice_2 = tk.Button(
    root, 
    text="stay", 
    command=next_scene_2,
    font=("Arial", 20),
    bg="#B0C4DE",
    width=10,
    height=1
)

def to_menu():
    global in_menu, game_running
    in_menu = True
    game_running = False



##############################333333


#-----------------------------------------------------------------------------------#


#---game variables and functions---#




#---game code---#
def game_code():
    global scene_text_var
    
    canvas.delete("all")

    if in_menu == True and game_running == False:
        canvas.create_image(-50,0, anchor="nw", image=menu_bg)

        canvas.create_window(600, 300,anchor="center", window=play)

    elif in_menu == False and game_running == True:

        if scene_nr == 1:
            canvas.create_image(-50,0, anchor="nw", image=scene1_img)


        elif scene_nr == 2:
            if choice == False:
                scene_text_var = "scene2"
                canvas.create_image(-50,0, anchor="nw", image=scene2_c1_img)
            else:
                canvas.create_image(-50,-100, anchor="nw", image=scene2_c2_img)
                choice_1.config(text="menu")
                choice_2.config(text="menu")
                scene_text_var = "No, i cant leave them. Not this time. \n*You died from hunger after around 24 hours."
                
    

        canvas.create_rectangle(
            0, 550, 1280, 720,
            fill= "#B0C4DE",
            outline="#E6E6FA",
            width=4)
        
        scene_text = canvas.create_text(5, 600,
            text= scene_text_var,
            fill="black", 
            font=("Arial", 18),
            anchor="nw")
        

        canvas.create_window(1000, 560,anchor="nw", window=choice_1)
        
        canvas.create_window(1000, 620,anchor="nw", window=choice_2)

        print(choice)

root.mainloop()
