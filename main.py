from tkinter import *
import faker

randomize = faker.Faker()
win = Tk()
win.configure(background="#171717")
win.resizable(False,False)
win.title("GuessIT")

cur_word = randomize.word()
global guess_cnt
guess_cnt = 0

def guess():
    global guess_cnt
    chars1 = []
    chars2 = []
    common = []
    if guess_cnt != 4:
        if len(ent.get()) == len(cur_word):
            for i in cur_word:
                chars1.append(i)
            for j in ent.get():
                chars2.append(j)
            for k in chars1:
                for l in chars2:
                    if k == l:
                        if not l in common:
                            common.append(k)
            input_text = ent.get()

            for char in input_text:
                for key, box in boxes.items():
                    if input_text[int(key.split()[0])] == cur_word[int(key.split()[0])] and int(key.split()[1]) == guess_cnt:
                        box.config(text= cur_word[int(key.split()[0])])
                    elif int(key.split()[1]) == guess_cnt and input_text[int(key.split()[0])] in common:
                        box.config(bg="yellow",text=input_text[int(key.split()[0])])
                    elif int(key.split()[1]) == guess_cnt:
                        box.config(bg="red")
            if input_text == cur_word:
                print("Winner winner chicken dinner.")
            guess_cnt += 1
        else:
            print("Character count mismatch.")
    else:
        print("You lose. The word was " + cur_word)
title = Label(win,text="GuessIT",fg="yellow",bg="#171717",font=("Poppins",20))
title.grid(column=0,row=0,columnspan=len(cur_word))

dec = Label(win,text="Guess the correct word.",fg="white",bg="#171717",font=("Poppins",12))
dec.grid(row=1,column=0,columnspan=len(cur_word))

boxes = {}
for j in range(4):
    for i in range(len(cur_word)):
        boxes[str(i) + " " + str(j)] = Button(win,relief=FLAT,height=2,width=3)
        boxes[str(i) + " " + str(j)]["state"]=DISABLED
        boxes[str(i) + " " + str(j)].grid(row=j+2,column=i,padx=1,pady=1)
ent = Entry(win)
ent.grid(row=7,column=0,columnspan=len(cur_word)-1,pady=1,padx=1)

but = Button(win,text="Guess",command=guess)
but.grid(row=7,column=len(cur_word)-1,columnspan=len(cur_word)-1,pady=1,padx=1)

win.mainloop()
