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

    if (scene_nr == 2 and choice == True) or scene_nr == 4:
        to_menu()
    else:
        if scene_nr != 3:
            choice = False
    
        scene_nr += 1
    game_code()

def next_scene_2():
    global scene_nr
    global choice    

    choice = True

    scene_nr += 1
    game_code()

def exit_menu_and_set_scene_1():
    global scene_nr
    scene_nr = 1

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
menu_bg = ImageTk.PhotoImage(Image.open("assets\menu_plus_extra_pictures\Menu.png"))

##########################

#---scene variables---#
scene1_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\Scene1.png"))

scene2_c1_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\Scene2.png"))
scene2_c2_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\you_died.png"))

scene3_c1_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\scene3_if_conf.png"))
scene3_c2_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\second_last_scene_if_sneaky.png"))

scene4_c1_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\last_scene_if_escape.png"))
scene4_c2_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\last_scene_if_escape_sneaky.png"))

scene_text_var = "Ugh... my head. What happened? Did i pass out? \nOh, no. Why isnt anyone moving. Could it be that i'm the only one alive?"



choice_1 = tk.Button(
    root, 
    text="Look around", 
    command=next_scene_1,
    font=("Arial", 20),
    bg="#B0C4DE",
    width=15,
    height=1
)

choice_2 = tk.Button(
    root, 
    text="Stay", 
    command=next_scene_2,
    font=("Arial", 20),
    bg="#B0C4DE",
    width=15,
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
            scene_text_var = "Ugh... my head. What happened? Did i pass out? \nOh, no. Why isnt anyone moving. Could it be that i'm the only one alive?"
            choice_1.config(text="Look around")
            choice_2.config(text="Stay")

        elif scene_nr == 2:
            if choice == False:
                canvas.create_image(-50,0, anchor="nw", image=scene2_c1_img)
                scene_text_var = "A massive guard blocks the path. My friends are dead, and I’m a round target in a \nsquare city. I can try to find a heart in this machine, or I can trust only myself."
                choice_1.config(text="ask for help")
                choice_2.config(text="go the other way")
                
            else:
                canvas.create_image(-50,-100, anchor="nw", image=scene2_c2_img)
                choice_1.config(text="Menu")
                scene_text_var = "No, i cant leave them. Not this time. \n*You died from hunger after around 24 hours.\n GEOMETRY STORIES: THE SHARED GRAVE"
                
        elif scene_nr == 3:
            if choice == False:
                canvas.create_image(-50,-100, anchor="nw", image=scene3_c1_img)
                scene_text_var = "I step out. The guard’s eyes lock onto me. He leans down and whispers: \nI’ve heard stories of your kind... the Circle World. \nYou aren't safe here. There are others who might want to help. Follow me."
                choice_1.config(text="Next")
            else:
                canvas.create_image(-50,0, anchor="nw", image=scene3_c2_img)
                choice_1.config(text="Next")
                scene_text_var = "I don't trust him. I slip back into the shadows and keep moving. \nAfter hours of wandering through the maze of gray blocks, the alley finally opens up. \nThere it is. A gleaming space facility and a spaceship as well, towering over the cubic city. \nIt’s my only way home."
        elif scene_nr == 4:
            if choice == False:
                canvas.create_image(-50,-100, anchor="nw", image=scene4_c1_img)
                choice_1.config(text="Menu")    
                scene_text_var = "We reached the platform just in time. The Guard held the line while I prepped the engines. \nAs the thrusters ignited, I looked down. He wasn't just a machine, he was infact a friend. \nIn the end, the square world didn't feel so cold.\n GEOMETRY STORIES: THE ALLIANCE"
            
            else: 
                canvas.create_image(-50,-100, anchor="nw", image=scene4_c2_img)
                choice_1.config(text="Menu")
                scene_text_var = "It’s held together by scrap and desperation, but it flies. I did it alone. \nNo guards, no help, no witnesses. The city shrinks into a tiny gray grid below me \nas I leave this graveyard behind. I’m going home but I'll never forget you, friends.\n GEOMETRY STORIES: THE SOLO RUN"      


        canvas.create_rectangle(
            0, 550, 1280, 720,
            fill= "#B0C4DE",
            outline="#E6E6FA",
            width=4)
        
        scene_text = canvas.create_text(5, 567,
            text= scene_text_var,
            fill="black", 
            font=("Arial", 18),
            anchor="nw")
        

        canvas.create_window(1000, 560,anchor="nw", window=choice_1)
        
        if scene_nr not in [3, 4]:
            if scene_nr == 2 and choice == True:
                return
            else:
                canvas.create_window(1000, 620,anchor="nw", window=choice_2)

game_code()
root.mainloop()