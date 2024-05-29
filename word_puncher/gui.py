import tkinter as tk
root = tk.Tk()
root.title('Word Puncher')
root.geometry('720x680+100+100')
title = tk.Label(root, text="Word Puncher", font=('Arial 16 bold')).grid(row=2, columnspan=2)
button = tk.Button(root, text="Add file").grid(row=2, column=1)
word_inp = tk.Checkbutton(root, text="Check")

root.mainloop()