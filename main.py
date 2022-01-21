from tkinter import *
from time import strftime

#Creating a TK GUI
base = Tk()
base.title("Relogio AM-PM")

#Defines font size, BG color, displayed number colors, and the fixation point.
label = Label(base, font=('Arial', 60), background='Black', foreground='red')
label.pack(anchor='center')

#Format the time according to the US or BRA pattern. After 1000ms delay, call the function again (Counting seconds passing)
def timer_usa():
    timer = strftime('%I:%M:%S %p')
    label.config(text=timer)
    label.after(1000, timer_usa)

def timer_br():
    timer = strftime('%Hh%Mm%Ss')
    label.config(text=timer)
    label.after(1000, timer_br)

#Main function. Chooses between the two patterns.
def main():
    form=int(input('''Choose the time format:\n1. Am-Pm (US Standard)\n2. 24-hours (BR Standard)\n>> '''))
    if form == 1:
        timer_usa()
        mainloop()
    elif form ==2:
        timer_br()
        mainloop()  
    else:
        print("Enter a valid option ")
        form = main()

if __name__=='__main__':
    main()