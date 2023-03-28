from tkinter import *
from tkinter import messagebox
import random


root = Tk()
root.title('Tile Matching Game!')
root.geometry('500x550')

#shuffle matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)

#frame for the buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

#variables
count = 0
answer_list = []
answer_dict = {}
winner = 0

#reset game function
def reset():
    
    #reset matches
    global matches, winner
    winner = 0
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches)
    
    #reset label
    label.config(text='')
    
    #reset tiles
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    #change the color of buttons
    for button in button_list:
        button.config(text=' ', state='normal', bg='SystemButtonFace')

#winner function
def win():
    label.config(text='Congratulations! You win!!!')
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    #change the color of buttons
    for button in button_list:
        button.config(bg='green')


#function for clicking buttons
def button_click(b, button_num):
    global count, answer_dict, answer_list, winner
    
    if b['text'] == ' ' and count < 2:
        b['text'] = matches[button_num]
        answer_list.append(button_num)
        answer_dict[b] = matches[button_num]
        count += 1
        
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            label.config(text='MATCH!')
            for key in answer_dict:
                key['state'] = 'disabled'
            count = 0
            answer_list = []
            answer_dict = {}
            winner += 1
            if winner == 6 :
                win()
        else:
            count = 0
            answer_list = []
            #pop up message box
            messagebox.showinfo('Incorrect!', 'Incorrect')
            #reset the buttons
            for key in answer_dict:
                key['text'] = ' '
            answer_dict = {}
            
            
#define buttons
b0 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b0, 0), relief='groove')
b1 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b1, 1), relief='groove')
b2 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b2, 2), relief='groove')
b3 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b3, 3), relief='groove')
b4 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b4, 4), relief='groove')
b5 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b5, 5), relief='groove')
b6 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b6, 6), relief='groove')
b7 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b7, 7), relief='groove')
b8 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b8, 8), relief='groove')
b9 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b9, 9), relief='groove')
b10 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b10, 10), relief='groove')
b11 = Button(button_frame, text=' ', font=('Helvetica', 20), height=3, width=6, command=lambda: button_click(b11, 11), relief='groove')

b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

#label
label = Label(root, text='')
label.pack(pady=20)

#menu
my_menu = Menu(root)
root.config(menu=my_menu)

#create an options dropdown menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Reset Game', command=reset)
option_menu.add_separator()
option_menu.add_command(label='Exit Game', command=root.destroy)

root.mainloop()