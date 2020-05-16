from tkinter import *
screen=Tk()
screen.title("MyCalculator")
screen.configure(bg="blue")
screen.maxsize(width=360,height=480)
screen.minsize(width=360,height=470)
def click(number):
    global  operator
    operator+=str(number)
    tex.set(operator)

def clear():
    global operator
    operator=''
    tex.set(operator)

def eqaul():# eval(1+2*3)=9
    global operator
    result=eval(operator)
    operator=str(result)
    tex.set(result)
########Binding function
def on_enter7(e):
    btn7.configure(bg='red')

def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter7(e):
    btn7.configure(bg='red')

def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter8(e):
    btn8.configure(bg='red')

def on_leave8(e):
    btn8.configure(bg='powder blue')

def on_enter9(e):
    btn9.configure(bg='red')

def on_leave9(e):
    btn9.configure(bg='powder blue')

def on_enter4(e):
    btn4.configure(bg='red')

def on_leave4(e):
    btn4.configure(bg='powder blue')

def on_enter5(e):
    btn5.configure(bg='red')

def on_leave5(e):
    btn5.configure(bg='powder blue')

def on_enter6(e):
    btn6.configure(bg='red')

def on_leave6(e):
    btn6.configure(bg='powder blue')

def on_enter1(e):
    btn1.configure(bg='red')

def on_leave1(e):
    btn1.configure(bg='powder blue')

def on_enter2(e):
    btn2.configure(bg='red')

def on_leave2(e):
    btn2.configure(bg='powder blue')

def on_enter3(e):
    btn3.configure(bg='red')

def on_leave3(e):
    btn3.configure(bg='powder blue')

def on_enter0(e):
    btn0.configure(bg='red')

def on_leave0(e):
    btn0.configure(bg='powder blue')

def on_enteradd(e):
    btnadd.configure(bg='red')

def on_leaveadd(e):
    btnadd.configure(bg='powder blue')

def on_entermul(e):
    btnmul.configure(bg='red')

def on_leavemul(e):
    btnmul.configure(bg='powder blue')

def on_enterdiv(e):
    btndiv.configure(bg='red')

def on_leavediv(e):
    btndiv.configure(bg='powder blue')

def on_entereqaul(e):
    btneqaul.configure(bg='red')

def on_leaveeqaul(e):
    btneqaul.configure(bg='powder blue')

def on_enterclr(e):
    btnclr.configure(bg='red')

def on_leaveclr(e):
    btnclr.configure(bg='powder blue')

def on_entersub(e):
    btnsub.configure(bg='red')

def on_leavesub(e):
    btnsub.configure(bg='powder blue')

def on_entryenter(e):
    entry1.configure(bg='red',fg='white')

def on_entryleave(e):
    entry1.configure(bg='orange',fg='black')


tex=StringVar()
operator=''

entry1=Entry(screen,bg='white',font=('arial',20,'italic bold'),bd='30',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)
#frist row
btn7=Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),activebackground='green',activeforeground='white',bg='powder blue')
btn7.grid(row=1,column=0)

btn8=Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),activebackground='green',activeforeground='white',bg='powder blue')
btn8.grid(row=1,column=1)

btn9=Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),activebackground='green',activeforeground='white',bg='powder blue')
btn9.grid(row=1,column=2)

btnadd=Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),activebackground='green',activeforeground='white',bg='powder blue')
btnadd.grid(row=1,column=3)


#second row
btn4=Button(screen,text='4',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),activebackground='green',activeforeground='white',bg='powder blue')
btn4.grid(row=2,column=0)

btn5=Button(screen,text='5',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),activebackground='green',activeforeground='white',bg='powder blue')
btn5.grid(row=2,column=1)

btn6=Button(screen,text='6',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),activebackground='green',activeforeground='white',bg='powder blue')
btn6.grid(row=2,column=2)

btnsub=Button(screen,text='-',font=('arial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('-'),activebackground='green',activeforeground='white',bg='powder blue')
btnsub.grid(row=2,column=3)

#third row
btn1=Button(screen,text='1',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),activebackground='green',activeforeground='white',bg='powder blue')
btn1.grid(row=3,column=0)

btn2=Button(screen,text='2',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),activebackground='green',activeforeground='white',bg='powder blue')
btn2.grid(row=3,column=1)

btn3=Button(screen,text='3',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),activebackground='green',activeforeground='white',bg='powder blue')
btn3.grid(row=3,column=2)

btnmul=Button(screen,text='*',font=('arial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('*'),activebackground='green',activeforeground='white',bg='powder blue')
btnmul.grid(row=3,column=3)

#fourth row
btn0=Button(screen,text='0',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),activebackground='green',activeforeground='white',bg='powder blue')
btn0.grid(row=4,column=0)

btnclr=Button(screen,text='C',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=clear,activebackground='green',activeforeground='white',bg='powder blue')
btnclr.grid(row=4,column=1)

btneqaul=Button(screen,text='=',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=eqaul,activebackground='green',activeforeground='white',bg='powder blue')
btneqaul.grid(row=4,column=2)

btndiv=Button(screen,text='/',font=('arial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('/'),activebackground='green',activeforeground='white',bg='powder blue')
btndiv.grid(row=4,column=3)

#Binding Enter leave

entry1.bind('<Enter>',on_entryenter)
entry1.bind('<Leave>',on_entryleave)
btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnclr.bind('<Enter>',on_enterclr)
btnclr.bind('<Leave>',on_leaveclr)

btneqaul.bind('<Enter>',on_entereqaul)
btneqaul.bind('<Leave>',on_leaveeqaul)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)








screen.mainloop()
