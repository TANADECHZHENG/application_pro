from tkinter import *
import tkinter.messagebox
#สร้างหน้าต่างหน้าเกม
window = Tk() 
window.title("THE GUI")
window.geometry("340x400")
#ฟังก์ชันเข้าเกม ออกเกม
def startgame():
    window.destroy()
    question = Tk()
    question.title("QUEST")
    question.geometry("700x840+0+0")
    Label(question, text="waiting for question...", font=("Arial", 30)).pack(pady=40)

def exitgame():
    confirm = tkinter.messagebox.askquestion("confirm", "want to exit the game?")
    if confirm == "yes":
        window.destroy()

welcome = Label(window, text="Welcome to the game", bg="green", font=100).pack(pady=20)
start = Button(window, text="start game", command=startgame).pack(pady=10)
door_exit = Button(window, text="exit game", command=exitgame).pack(pady=10)
window.mainloop()
