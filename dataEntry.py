import tkinter as tk

# Set up the window
window = tk.Tk()
window.title("Book Classifier")
# Define geometry of the window
window.geometry("700x250")
window.resizable(width=False, height=False)

# Create the book entry frame with an Entry
#frm_entry = tk.Frame(master=window)
book_title = tk.Entry(width=10)
author_Lname = tk.Entry(width=10)
author_Other_name = tk.Entry(width=10)
subject = tk.Entry(width=10)

# widget and label in it
lbl_submit = tk.Button(text="Submit")
lbl_quit = tk.Button(text="Quit")

book_title.grid(row=0, column=0)
author_Lname.grid(row=2, column=0)
author_Other_name.grid(row=2, column=1)
subject.grid(row=1, column=0)
# subject.place(x=40, y= 20)

lbl_submit.grid(row=3, column=0, sticky="e")
lbl_quit.grid(row=3, column=1, sticky="w")

# Run the application
window.mainloop()