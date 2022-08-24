from tkinter import *
root = Tk()
root.title("FibonacciSUM")
root.geometry("400x400")

label1 = Label(root,text = "fibonacci series : ")
label2 = Label(root,text = "fibonacci sum : ")
enter_number = Entry(root)

def fibonacci():
    input_no = int(enter_number.get())
    first_no  = 0 
    second_no = 1
    sum1 = 0 
    sum2 = 0
    count = 1

    while(count <= input_no):
        label1["text"] +=str(sum1) + " "
        label2["text"] +=  " fibonacci sum :" + str (sum2)
        count = count + 1
        first_no = second_no
        second_no = sum1
        sum1 = first_no  + second_no
        sum2 = sum2 + sum1

enter_number.pack()  
    
btn = Button(root,text = "show fibonacci series", command = fibonacci)
btn.pack()
label1.pack()
label2.pack()
root.mainloop()
       
    