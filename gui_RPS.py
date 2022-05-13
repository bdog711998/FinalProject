from tkinter import *
import random

outcomes = {
    "rock":{"rock":1,"paper":0,"scissors":2},
    "paper":{"rock":2,"paper":1,"scissors":0},
    "scissors":{"rock":0,"paper":2,"scissors":1}
}

computer_score = 0
player_score = 0

def str_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"

def outcome_choice(user_choice):
    global computer_score
    global player_score
    random_number = random.randint(1, 3)
    computer_choice = str_outcome(random_number)
    outcome = outcomes[user_choice][computer_choice]

    player_choice_label.config(fg="black", text="Player Choice : " + str(user_choice))
    computer_choice_label.config(fg="blue", text="Computer Choice : " + str(computer_choice))

    if outcome == 2:
        player_score = player_score + 2
        player_score_label.config(text="Player : " + str(player_score))
        outcome_label.config(fg="red", text="Outcome : Player Won")
    elif outcome == 0:
        computer_score = computer_score + 2
        computer_score_label.config(text="Computer : " + str(computer_score))
        outcome_label.config(fg="red", text="Outcome : Computer Won")
    elif outcome == 1:
        player_score = player_score + 1
        computer_score = computer_score + 1
        player_score_label.config(text="Player : " + str(player_score))
        computer_score_label.config(text="Computer : " + str(computer_score))
        outcome_label.config(fg="red", text="Outcome : Draw")


window = Tk()
window.resizable(False, False)
window.geometry("600x200")

Label(window,text="Rock, Paper, Scissors",font=("Calibri",16)).grid(row=0,sticky=N,pady=10,padx=200)
Label(window,text="Please select an option",font=("Calibri",12)).grid(row=1,sticky=N)
player_score_label = Label(window,text="Player : 0",font=("Calibri",12))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(window,text="Computer : 0",font=("Calibri",12))
computer_score_label.grid(row=2,sticky=E)
player_choice_label  = Label(window,font=("Calibri",12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label = Label(window,font=("Calibri",12))
computer_choice_label.grid(row=3,sticky=E)
outcome_label = Label(window,font=("Calibri",12))
outcome_label.grid(row=3,sticky=N)

Button(window,text="Rock",width=15,command=lambda:outcome_choice("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(window,text="Paper",width=15,command=lambda:outcome_choice("paper")).grid(row=4,sticky=N,pady=5)
Button(window,text="Scissors",width=15,command=lambda:outcome_choice("scissors")).grid(row=4,sticky=E,padx=5,pady=5)

Label(window).grid(row=5)



