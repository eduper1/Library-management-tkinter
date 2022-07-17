import tkinter as tk

# Set up the window
window = tk.Tk()
window.title("Book Classifier")
# Define geometry of the window
window.geometry("700x250")
window.resizable(width=False, height=False)

# function to delete temporary text when focusIn event is triggered
# def temp_text(event):
#    book_title.delete(0,"end")
#    subject.delete(0,"end")
#    author_Lname.delete(0,"end")
#    author_Other_name.delete(0,"end")


# Create the book entry frame with an Entry
#frm_entry = tk.Frame(master=window)
book_title_lbl = tk.Label(window, text = 'Title of the book:', font=('calibre',10, 'bold'))
book_title = tk.Entry(width=30)
# get_entry = book_title.get(tk.END)
# print(get_entry)
# book_title.insert(0, "Title of the book.")

subject_lbl = tk.Label(window, text = 'Subject of the book:', font=('calibre',10, 'bold'))
subject = tk.Entry(width=30)
# subject.insert(0, "Subject of the Book.")

author_Lname_lbl = tk.Label(window, text = "Author's Last Name:", font=('calibre',10, 'bold'))
author_Lname = tk.Entry(width=30)
# author_Lname.insert(0, "Author's Last Name")

author_Other_lbl = tk.Label(window, text = "Author's Other Name:", font=('calibre',10, 'bold'))
author_Other_name = tk.Entry(width=30)
# author_Other_name.insert(0, "Author's other name")

# widget and label in it
lbl_submit = tk.Button(text="Submit")
lbl_quit = tk.Button(text="Quit")

book_title_lbl.grid(row=0, column=0)
book_title.grid(row=0, column=1)

subject_lbl.grid(row=1, column=0)
subject.grid(row=1, column=1)

author_Lname_lbl.grid(row=2, column=0)
author_Lname.grid(row=2, column=1)

author_Other_lbl.grid(row=2, column=2)
author_Other_name.grid(row=2, column=3)
# subject.place(x=40, y= 20)

lbl_submit.grid(row=3, column=0, sticky="e")
lbl_quit.grid(row=3, column=1, sticky="w")

# run event
# book_title.bind("<FocusIn>", temp_text)
# subject.bind("<FocusIn>", temp_text)
# author_Lname.bind("<FocusIn>", temp_text)
# author_Other_name.bind("<FocusIn>", temp_text)

# Run the application
window.mainloop()