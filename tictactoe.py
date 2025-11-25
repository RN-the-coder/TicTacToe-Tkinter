import tkinter 
def set_tile(row, column):
   global curr_player, turns

   if(game_over):
       return

   if board[row][column]["text"] != "":
        return
   board[row][column]["text"] = curr_player
   turns+=1
   
   if curr_player == playerO:
       curr_player = playerX
   else:
         curr_player = playerO
   label["text"] = curr_player + "'s turn"
   check_winner()

def check_winner():
    global turns,game_over
    for row in range (3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " wins!", foreground=color_caqui)
            for column in range(3):
                board [row][column].config(background=color_caqui , foreground=color_gray)
            game_over = True
            return
    
    for column in range (3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_caqui)
            for row in range(3):
                board [row][column].config(background=color_caqui , foreground=color_gray)
            game_over = True
            return
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] !=""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_caqui)
        for i in range(3):
            board[i][i].config(foreground=color_gray, background=color_caqui)
        game_over = True
        return
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] !=""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_caqui)
        board[0][2].config(foreground=color_gray, background=color_caqui)
        board[1][1].config(foreground=color_gray, background=color_caqui)
        board[2][0].config(foreground=color_gray, background=color_caqui)
        game_over = True
        return
    
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_caqui)
        return
def new_game():
    global turns, game_over
    turns = 0
    game_over = False

    label.config(text=curr_player+ "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_gray, background=color_brown)




playerX = "X"
playerO = "0"

curr_player = playerX

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_green = "#0A4403"
color_brown = "#402903"
color_gray  = "#919191"
color_caqui = "#7C8447"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(True,True)

frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=curr_player+"'s turn", font=("Consolas", 20), background=color_green, foreground="white" )

label.grid(row=0, column = 0, columnspan=3, sticky="we")
frame.pack()

for row in range (3):
    for column in range (3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_brown, foreground=color_gray, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)
button = tkinter.Button(frame, text="Reset", font=("Consolas", 20), background=color_caqui, foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")




frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()