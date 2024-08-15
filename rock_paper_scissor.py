from tkinter import *

import random

def name():
    username = entry.get()
    entry.config(state=DISABLED)

    def clickme():
        root = Toplevel(windows1)
        sss = PhotoImage(file='ss.png')
        root.geometry("500x600+500+120")
        root.title("rules")
        bckgrdrul = Label(root, i=sss)
        bckgrdrul.place(x=0, y=0)
        root.mainloop()

    def player_vs_player():
        windows3rd = Toplevel(windows1)

        player1 = ""
        player2 = ""

        def inp1():
            nonlocal player1
            player1 = 'rock'

        def inp2():
            nonlocal player1
            player1 = 'paper'

        def inp3():
            nonlocal player1
            player1 = 'scissor'

        def inp4():
            nonlocal player2
            player2 = 'rock'

        def inp5():
            nonlocal player2
            player2 = 'paper'

        def inp6():
            nonlocal player2
            player2 = 'scissor'


        def result():

            def playagain():
                windows1.destroy()
                windows3rd.destroy()
                windows4th.destroy()
                name()

            def exit():
                windows.destroy()
                '''windows1.destroy()
                windows3rd.destroy()
                windows4th.destroy()'''

            won1 = False
            won2 = False

            if player1 == player2:
                won1 = True
                won2 = True
            elif player1 == 'rock':
                if player2 == 'paper':
                    won2 = True
                    won1 = False
                else:
                    won1 = True
                    won2 = False
            elif player1 == 'paper':
                if player2 == 'rock':
                    won1 = True
                    won2 = False
                else:
                    won2 = True
                    won1 = False
            elif player1 == 'scissor':
                if player2 == 'rock':
                    won2 = True
                    won1 = False
                else:
                    won1 = True
                    won2 = False

            windows4th = Toplevel(windows3rd)

            if won1 == won2:
                text1 = "It's a tie"
                res = 'Better luck next time'
                won = PhotoImage(file='mission12.png')
            elif won1 == True:
                text1 = 'congratulations,'
                res = 'player 1 won'
                won = PhotoImage(file='mission12.png')
            else:
                text1 = 'congratulations,'
                res = 'player 2 won'
                won = PhotoImage(file='wasted.png')

            windows4th.geometry("1200x640+170+90")
            windows4th.title("player vs computer")

            icon1 = PhotoImage(file='joystick1.png')
            windows4th.iconphoto(True, icon1)

            bckgrd = PhotoImage(file='fin.png')

            bckimg = Label(windows4th, i=bckgrd)
            bckimg.pack()

            button1 = Button(windows4th,
                             text='play again',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             command = playagain,
                             relief=RAISED,
                             bd=25,
                             padx=20,
                             pady=4,
                             compound='top')
            button1.place(x=0, y=530)

            button2 = Button(windows4th,
                             text='exit',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             relief=RAISED,
                             command=exit,
                             bd=25,
                             padx=30,
                             pady=4,
                             compound='top')
            button2.place(x=1020, y=530)

            label1 = Label(windows4th,
                           text=text1,
                           font=('Arial', 15, 'bold'),
                           fg='#00FF00',
                           bg='white',
                           bd=6,
                           padx=34,
                           pady=18,
                           compound='left')
            label1.place(x=890, y=20)

            label2 = Label(windows4th,
                           text=res,
                           font=('Arial', 15, 'bold'),
                           fg='#00FF00',
                           bg='white',
                           bd=6,
                           padx=34,
                           pady=18,
                           compound='left')
            label2.place(x=890, y=100)

            won = PhotoImage(file='mission12.png')
            label3 = Label(windows4th,
                           text='Player 2',
                           font=('Arial', 15, 'bold'),
                           fg='#00FF00',
                           bg='white',
                           bd=6,
                           padx=34,
                           pady=18,
                           image=won)
            label3.place(x=750, y=210)

            windows4th.mainloop()

        windows3rd.geometry("1200x640+170+90")
        windows3rd.title("player vs player")

        icon1 = PhotoImage(file='joystick1.png')
        windows3rd.iconphoto(True, icon1)

        bckgrd = PhotoImage(file='win3.png')

        bckimg = Label(windows3rd, i=bckgrd)
        bckimg.pack()

        buttonrock1 = Button(windows3rd,
                             text='rock',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             relief=RAISED,
                             bd=25,
                             padx=50,
                             pady=18,
                             command=inp1,
                             compound='top')
        buttonrock1.place(x=100, y=140)

        buttonpaper1 = Button(windows3rd,
                              text='paper',
                              font=('Arial', 20, 'bold'),
                              fg='#00FF00',
                              bg='black',
                              relief=RAISED,
                              command=inp2,
                              bd=25,
                              padx=43,
                              pady=18,
                              compound='top')
        buttonpaper1.place(x=100, y=280)

        buttonscissor1 = Button(windows3rd,
                                text='scissor',
                                font=('Arial', 20, 'bold'),
                                fg='#00FF00',
                                bg='black',
                                relief=RAISED,
                                command=inp3,
                                bd=25,
                                padx=34,
                                pady=18,
                                compound='top')
        buttonscissor1.place(x=100, y=420)

        buttonrock2 = Button(windows3rd,
                             text='rock',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='white',
                             relief=RAISED,
                             command=inp4,
                             bd=25,
                             padx=50,
                             pady=18,
                             compound='top')
        buttonrock2.place(x=890, y=140)

        buttonpaper2 = Button(windows3rd,
                              text='paper',
                              font=('Arial', 20, 'bold'),
                              fg='#00FF00',
                              bg='white',
                              relief=RAISED,
                              command=inp5,
                              bd=25,
                              padx=43,
                              pady=18,
                              compound='top')
        buttonpaper2.place(x=890, y=280)

        buttonscissor2 = Button(windows3rd,
                                text='scissor',
                                font=('Arial', 20, 'bold'),
                                fg='#00FF00',
                                bg='white',
                                relief=RAISED,
                                command=inp6,
                                bd=25,
                                padx=34,
                                pady=18,
                                compound='top')
        buttonscissor2.place(x=890, y=420)

        profile1 = PhotoImage(file='e13.png')
        profile2 = PhotoImage(file='devil3.png')

        labelplayer1 = Label(windows3rd,
                             text='Player 1',
                             font=('Arial', 15, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             bd=6,
                             padx=34,
                             pady=18,
                             image=profile1,
                             compound='left')
        labelplayer1.place(x=100, y=20)

        labelplayer2 = Label(windows3rd,
                             text='Player 2',
                             font=('Arial', 15, 'bold'),
                             fg='#00FF00',
                             bg='white',
                             bd=6,
                             padx=34,
                             pady=18,
                             image=profile2,
                             compound='left')
        labelplayer2.place(x=890, y=20)

        buttonsub = Button(windows3rd,
                           text="submit",
                           command=result,
                           font=('Comic Sans', 34),
                           fg='black',
                           bg='white',
                           activebackground='white',
                           activeforeground='black',
                           state=ACTIVE,
                           )
        buttonsub.place(x=500, y=550)

        windows3rd.mainloop()

    def player_vs_comp():

        player1 = ""
        player2 = random.choice(["rock","paper","scissor"])

        def inp1():
            nonlocal player1
            player1 = 'rock'

        def inp2():
            nonlocal player1
            player1 = 'paper'

        def inp3():
            nonlocal player1
            player1 = 'scissor'

        def result2():

            def playagain():
                windows1.destroy()
                windows4bth.destroy()
                windows5th.destroy()
                name()

            def exit():
                windows.destroy()
                '''windows1.destroy()
                windows4bth.destroy()
                windows5th.destroy()'''

            won1 = False
            won2 = False

            if player1 == player2:
                won1 = True
                won2 = True
            elif player1 == 'rock':
                if player2 == 'paper':
                    won2 = True
                    won1 = False
                else:
                    won1 = True
                    won2 = False
            elif player1 == 'paper':
                if player2 == 'rock':
                    won1 = True
                    won2 = False
                else:
                    won2 = True
                    won1 = False
            elif player1 == 'scissor':
                if player2 == 'rock':
                    won2 = True
                    won1 = False
                else:
                    won1 = True
                    won2 = False
            print(won1)

            windows5th = Toplevel(windows4bth)

            if won1 == won2:
                text1 = "It's a tie"
                res = 'Better luck next time'
                won = PhotoImage(file='mission12.png')
            elif won1 == True:
                text1 = 'congratulations,'
                res = 'you won'
                won = PhotoImage(file='mission12.png')
            else:
                text1 = 'sorry to see,'
                res = 'you lost'
                won = PhotoImage(file='wasted.png')

            windows5th.geometry("1200x640+170+90")
            windows5th.title("player vs computer")

            icon1 = PhotoImage(file='joystick1.png')
            windows5th.iconphoto(True, icon1)

            bckgrd = PhotoImage(file='fin2.png')

            bckimg = Label(windows5th, i=bckgrd)
            bckimg.pack()

            button1 = Button(windows5th,
                             text='play again',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             relief=RAISED,
                             command= playagain,
                             bd=25,
                             padx=20,
                             pady=4,
                             compound='top')
            button1.place(x=0, y=530)

            button2 = Button(windows5th,
                             text='exit',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             relief=RAISED,
                             command = exit,
                             bd=25,
                             padx=30,
                             pady=4,
                             compound='top')
            button2.place(x=1020, y=530)

            label1 = Label(windows5th,
                           text=text1,
                           font=('Arial', 15, 'bold'),
                           fg='#00FF00',
                           bg='white',
                           bd=6,
                           padx=34,
                           pady=18,
                           compound='left')
            label1.place(x=890, y=20)

            label2 = Label(windows5th,
                           text=res,
                           font=('Arial', 15, 'bold'),
                           fg='#00FF00',
                           bg='white',
                           bd=6,
                           padx=34,
                           pady=18,
                           compound='left')
            label2.place(x=890, y=100)

            label3 = Label(windows5th,
                           text='Player 2',
                           font=('Arial', 15, 'bold'),
                           fg='#00FF00',
                           bg='white',
                           bd=6,
                           padx=34,
                           pady=18,
                           image=won)
            label3.place(x=750, y=210)

            windows5th.mainloop()

        windows4bth = Toplevel(windows1)

        windows4bth.geometry("1200x640+170+90")
        windows4bth.title("player vs computer")

        icon1 = PhotoImage(file='joystick1.png')
        windows4bth.iconphoto(True, icon1)

        bckgrd = PhotoImage(file='win4.png')

        bckimg = Label(windows4bth, i=bckgrd)
        bckimg.pack()

        buttonrock1 = Button(windows4bth,
                             text='rock',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             relief=RAISED,
                             command=inp1,
                             bd=25,
                             padx=50,
                             pady=18,
                             compound='top')
        buttonrock1.place(x=100, y=140)

        buttonpaper1 = Button(windows4bth,
                              text='paper',
                              font=('Arial', 20, 'bold'),
                              fg='#00FF00',
                              bg='black',
                              relief=RAISED,
                              command=inp2,
                              bd=25,
                              padx=43,
                              pady=18,
                              compound='top')
        buttonpaper1.place(x=100, y=280)

        buttonscissor1 = Button(windows4bth,
                                text='scissor',
                                font=('Arial', 20, 'bold'),
                                fg='#00FF00',
                                bg='black',
                                relief=RAISED,
                                command=inp3,
                                bd=25,
                                padx=34,
                                pady=18,
                                compound='top')
        buttonscissor1.place(x=100, y=420)

        buttonrock2 = Button(windows4bth,
                             text='rock',
                             font=('Arial', 20, 'bold'),
                             fg='#00FF00',
                             bg='white',
                             relief=RAISED,
                             state=DISABLED,
                             bd=25,
                             padx=50,
                             pady=18,
                             compound='top')
        buttonrock2.place(x=890, y=140)

        buttonpaper2 = Button(windows4bth,
                              text='paper',
                              font=('Arial', 20, 'bold'),
                              fg='#00FF00',
                              bg='white',
                              relief=RAISED,
                              state=DISABLED,
                              bd=25,
                              padx=43,
                              pady=18,
                              compound='top')
        buttonpaper2.place(x=890, y=280)

        buttonscissor2 = Button(windows4bth,
                                text='scissor',
                                font=('Arial', 20, 'bold'),
                                fg='#00FF00',
                                bg='white',
                                relief=RAISED,
                                state=DISABLED,
                                bd=25,
                                padx=34,
                                pady=18,
                                compound='top')
        buttonscissor2.place(x=890, y=420)

        profile1 = PhotoImage(file='e13.png')
        profile2 = PhotoImage(file='comp.png')

        labelplayer1 = Label(windows4bth,
                             text='Player 1',
                             font=('Arial', 15, 'bold'),
                             fg='#00FF00',
                             bg='black',
                             bd=6,
                             padx=34,
                             pady=18,
                             image=profile1,
                             compound='left')
        labelplayer1.place(x=100, y=20)

        labelplayer2 = Label(windows4bth,
                             text='computer',
                             font=('Arial', 15, 'bold'),
                             fg='#00FF00',
                             bg='white',
                             bd=6,
                             padx=34,
                             pady=18,
                             image=profile2,
                             compound='left')
        labelplayer2.place(x=890, y=20)

        buttonsub = Button(windows4bth,
                           text="submit",
                           command=result2,
                           font=('Comic Sans', 34),
                           fg='black',
                           bg='white',
                           activebackground='white',
                           activeforeground='black',
                           state=ACTIVE,
                           )
        buttonsub.place(x=500, y=550)

        windows4bth.mainloop()

    windows1 = Toplevel(windows)

    windows1.geometry("1200x640+170+90")
    windows1.title("Rock paper scissor")

    icon1 = PhotoImage(file='joystick1.png')
    windows1.iconphoto(True, icon1)

    bckgrd = PhotoImage(file='win2.png')

    bckimg = Label(windows1, i=bckgrd)
    bckimg.pack()

    labelwin2 = Label(windows1,
                      text='hello !\n' + username + '\n' + 'welcome to our game',
                      font=('Arial', 20, 'bold'),
                      fg='#C815F0',
                      bg='black',
                      # relief=RAISED,
                      # bd=25,
                      padx=22,
                      pady=10,
                      # compound='top'
                      )
    labelwin2.place(x=440, y=0)

    labelwin2b = Label(windows1,
                       text='rock',
                       font=('Arial', 18, 'bold'),
                       fg='#C815F0',
                       bg='black',
                       # relief=RAISED,
                       # bd=25,
                       padx=18,
                       pady=10,
                       # compound='top'
                       )
    labelwin2b.place(x=550, y=200)

    labelwin2c = Label(windows1,
                       text='paper',
                       font=('Arial', 18, 'bold'),
                       fg='#C815F0',
                       bg='black',
                       # relief=RAISED,
                       # bd=25,
                       padx=18,
                       pady=10,
                       # compound='top'
                       )
    labelwin2c.place(x=540, y=260)

    labelwin2d = Label(windows1,
                       text='scissor',
                       font=('Arial', 18, 'bold'),
                       fg='#C815F0',
                       bg='black',
                       # relief=RAISED,
                       # bd=25,
                       padx=18,
                       pady=10,
                       # compound='top'
                       )
    labelwin2d.place(x=535, y=320)

    # state=DISABLED
    button1 = Button(windows1,
                     text="rules",
                     command=clickme,
                     font=('Comic Sans', 34),
                     fg='black',
                     bg='white',
                     activebackground='white',
                     activeforeground='black',
                     state=ACTIVE,
                     )
    button1.place(x=100, y=100)

    labelcred = Label(windows1,
                      text='credits :',
                      font=('Arial', 14, 'bold'),
                      fg='#C815F0',
                      bg='black',
                      # relief=RAISED,
                      # bd=25,
                      padx=12,
                      pady=1,
                      # compound='top'
                      )
    labelcred.place(x=1080, y=540)

    labelname = Label(windows1,
                      text='Nandakumar T\nIndrakumar D\nNagathejas M S',
                      font=('Arial', 10, 'bold'),
                      fg='#C815F0',
                      bg='black',
                      # relief=RAISED,
                      # bd=25,
                      padx=2,
                      pady=1,
                      # compound='top'
                      )
    labelname.place(x=1080, y=570)

    button2 = Button(windows1,
                     text="player vs player",
                     command=player_vs_player,
                     font=('Comic Sans', 20),
                     fg='black',
                     bg='white',
                     activebackground='white',
                     activeforeground='black',
                     state=ACTIVE,
                     padx=2,
                     pady=1,
                     )
    button2.place(x=350, y=500)

    button3 = Button(windows1,
                     text="player vs computer",
                     command = player_vs_comp,
                     font=('Comic Sans', 20),
                     fg='black',
                     bg='white',
                     activebackground='white',
                     activeforeground='black',
                     state=ACTIVE,
                     padx=2,
                     pady=1,
                     )
    button3.place(x=600, y=500)
    windows1.mainloop()

def deleteit():
    entry.delete(0,END)

def bsit():
    entry.delete(len(entry.get())-1,END)

windows = Tk()

windows.geometry("1200x640+170+90")
windows.title("Rock paper scissor")

icon1 = PhotoImage(file='joystick1.png')
windows.iconphoto(True,icon1)

bckgrd = PhotoImage(file='intro.png')

bckimg = Label(windows,i=bckgrd)
bckimg.pack()

labelintro = Label(windows,
              text = 'hello ! welcome to our game',
              font=('Arial',20,'bold'),
              fg='#C815F0',
              bg="black",
              #relief=RAISED,
              #bd=25,
              padx=22,
              pady=10,
              #compound='top'
                   )
labelintro.place(x=5,y=390)

entry = Entry(windows,
              font=('Arial',38),
              bg='black',
              fg='green'
              )
entry.place(x=20,y=450)

submit_button = Button(windows,
                text='submit',
                command=name)
submit_button.place(x=420,y=450)

delete_button = Button(windows,
                text='delete',
                command=deleteit)
delete_button.place(x=472,y=450)

backspace_button = Button(windows,
                text='backspace',
                command=bsit)
backspace_button.place(x=518,y=450)

windows.mainloop()