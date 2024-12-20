import tkinter as tk

#create window
root = tk.Tk()
root.geometry("500x500")
root.title("Options Profit Calculator")

label = tk.Label(root, text= "hello", font = ('Arial', '18'))
label.pack(padx= 20, pady=20)
textbox = tk.Text(root, height = 3,font = ('Arial',16))
textbox.pack(padx=10, pady=10)

# myentry = tk.Entry(root)
# myentry.pack()

button = tk.Button(root, text="Click Me", font = ('Arial', 18))
button.pack(padx = 10, pady=10)

 

# drop_options = ['Long Call', 'Long Put', 'Short Call', 'Short Put']
# clicked = tk.StringVar()
# drop = tk.OptionMenu(root, clicked, drop_options)
# drop.pack()


# drop_button = tk.Button( root , text = "click Me").pack()
root.mainloop()

