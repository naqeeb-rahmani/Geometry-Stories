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

########################

#---menu buttons---#

def exit_menu():
    global in_menu, game_running
    in_menu = False
    game_running = True
    canvas.delete("all")
    game_code()

def set_scene():
    global scene_nr
    scene_nr = 0

def next_scene():
    global scene_nr
    if scene_nr < 5:
        scene_nr += 1

play = tk.Button(
    root, 
    text="Play", 
    command=exit_menu,
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
scene0_img = ImageTk.PhotoImage(Image.open("assets\Scene_pictures\Scene1.png"))

choice_1 = tk.Button(
    root, 
    text="Look around", 
    command=next_scene,
    font=("Arial", 20),
    bg="#B0C4DE",
    width=10,
    height=1
)

choice_2 = tk.Button(
    root, 
    text="Play", 
    command=exit_menu,
    font=("Arial", 20),
    bg="#B0C4DE",
    width=10,
    height=1
)

##############################333333


#-----------------------------------------------------------------------------------#


#---game variables and functions---#






#---game code---#
def game_code():
    if scene_nr == 0:
        canvas.create_image(-50,0, anchor="nw", image=scene0_img)
        #canvas.

    canvas.create_rectangle(
        0, 550, 960, 720,
        fill= "#B0C4DE",
        outline="#E6E6FA",
        width=4)

    canvas.create_text(5, 600,
    text= "What happened? Everyone is dead, but me\n my head",
    fill="black", 
    font=("Arial", 18),
    anchor="nw")

    canvas.create_window(1000, 600,anchor="nw", window=choice_1)

root.mainloop()



#----------------extra-----------------#

'''canvas.create_rectangle(
    0, 550, 960, 720,
    fill= "#B0C4DE",
    outline="#E6E6FA",
    width=4)

canvas.create_text(5, 600,
    text= "What happened? Everyone is dead, but me",
    fill="black", 
    font=("Arial", 18),
    anchor="nw")

def next_scene():
    print("")'''


'''next_btn = tk.Button(
    root, 
    text="Next →", 
    command=next_scene,
    font=("Arial", 14),
    bg="#B0C4DE"
)
canvas.create_window(850, 680, window=next_btn)'''

'''# Create empty text object
text_obj = canvas.create_text(5, 600,
    text= "", 
    fill="black", 
    font=("Arial", 18),
    anchor="nw")

# Typewriter function
def type_text(text, index=0):
    if index < len(text):
        current = canvas.itemcget(text_obj, "text")
        canvas.itemconfig(text_obj, text=current + text[index])
        root.after(50, type_text, text, index + 1)

# Start the effect
type_text("What happened? Everyone is dead, but me")'''
