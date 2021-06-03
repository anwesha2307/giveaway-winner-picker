import random
from tkinter import *
root=Tk()
root.title("Winner generator")
Bg=PhotoImage(file="D:\\PICS\\PICTURES\\Art\\art contest and giveaway\\random winner picker\\bgimg.png")
label1= Label(root,image=Bg)
label1.place(x=0,y=0)
#root.configure(bg='#fcdfff')
lop=[]
wl=[]
participants=[]
n=int(input("Enter no. of participants-"))
m=int(input("Enter no. of winners to be selected-"))
def onClick():
    for entries in lop:
        participants.append(str(entries.get()))
    for i in range(m):
        winner=random.randint(0,n-1)
        label=Label(root, text="The winners of the giveaway are-" , bg="yellow")
        label.grid(row=30, column=0)
        if winner not in wl:
            l=Label(root, text=participants[winner])
            l.grid(row=i+31, column=2)
            wl.append(winner)
            print ("win",winner)
        else:
            i-=1
            continue
for i in range(n):
        e=Entry(root, width=20)
        e.grid(row=i+5, column=5, padx=10, pady=10)
        l1=Label(root, text="participant " + str(i+1) + "-", bg="ivory2")
        l1.grid(row=i+5, column=2)
        lop.append(e)

button=Button(root, text="generate winner", command=onClick, bg="ivory2")
button.grid(row=24,column=5)

root.mainloop()
#this code is written by anwesha singh

