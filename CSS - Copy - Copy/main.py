from tkinter import*

#window
window=Tk()
window.config(bg="orange")
window.title('CALC')
window.geometry("450x400")
#label:
l1=Label(window,text="Enter first No:",font=90)
l1.grid(row=0,column=0)
#create entry box for label 1
e1=Entry(window)
e1.grid(row=0,column=1)
#label2
l2=Label(window,text="Enter second No:",font=90)
l2.grid(row=1,column=0)
#create entry box for label 2
e2=Entry(window)
e2.grid(row=1,column=1)
#button of the sum of two numbers
b1_sum=Button(window,text="+",command=sum)
b1_sum.grid(row=2,column=1)

window.mainloop()


