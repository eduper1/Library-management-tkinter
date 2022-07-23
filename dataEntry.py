import tkinter as tk
from openpyxl import workbook, load_workbook



# Set up the window
window = tk.Tk()
window.title("Book Classifier")
# Define geometry of the window
window.geometry("700x250")
window.resizable(width=False, height=False)

# open active excel workbook
wb = load_workbook('books.xlsx')
# open the active work sheet
ws = wb.active
# function to delete temporary text when focusIn event is triggered
# def temp_text(event):
#    book_title.delete(0,"end")
#    subject.delete(0,"end")
#    author_Lname.delete(0,"end")
#    author_Other_name.delete(0,"end")

# declaring string variable
# for storing the entries value
get_book_title = tk.StringVar()
get_book_subject = tk.StringVar()
get_author_Lname = tk.StringVar()
get_author_Oname = tk.StringVar()

dewey_dict = {
    "generalities":000,
    "philosophy":100,
    "religion":200,
    "social science":300,
    "language":400,
    "natural science":500,
    "technology":600,
    "arts":700,
    "literature":800,
    "geography":900
    }
print(dewey_dict.values())

capital_dict = {k.upper(): v for k,v in dewey_dict.items()}
print(capital_dict.keys())
 
# function to get the fast 3 letters of 
# the author's last name
def fThree (Lname):
    if len(Lname) >= 3:
        return Lname[0:3]
    else:
        return f"Author's Last name must be more then 2 letters"
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    get_book_entry = get_book_title.get()
    get_subject_entry = get_book_subject.get()
    get_Lname_entry = get_author_Lname.get()
    get_Oname_entry = get_author_Oname.get()
     
    print("Title of the book: " + get_book_entry)
    print("Subject of the book:  " + get_subject_entry)
    print("Author's last name: " + get_Lname_entry)
    print("Author's other names: " + get_Oname_entry)
    if get_Lname_entry == "":
        print("Now Dewey code generated")
    elif len(get_Lname_entry) < 3:
        print(fThree(get_Lname_entry))
    else:
        for key, value in capital_dict.items():
            if get_subject_entry.upper() == key:
                data_list = [get_book_entry, get_subject_entry, get_Lname_entry, get_Oname_entry]
                dewey_code = f'{value} - {fThree(get_Lname_entry)}'
                print(dewey_code)
                data_list.append(dewey_code)
                print(data_list)
                # print("Dewey code is: ", value, "-", fThree(get_Lname_entry))
                ws.append(data_list)
                # save the workbook
                wb.save('books.xlsx')
                
                
                # print(True)
        print("The subject is not found")
        print(False)
    
    get_book_title.set("")
    get_book_subject.set("")
    get_author_Lname.set("")
    get_author_Oname.set("")
    

# Create the book entry frame with an Entry
#frm_entry = tk.Frame(master=window)
book_title_lbl = tk.Label(window, text = 'Title of the book:', font=('calibre',10, 'bold'))
book_title = tk.Entry(width=30, textvariable=get_book_title)
book_title.focus_set()
# get_entry = book_title.get(tk.END)
# print(get_entry)
# book_title.insert(0, "Title of the book.")

subject_lbl = tk.Label(window, text = 'Subject of the book:', font=('calibre',10, 'bold'))
subject = tk.Entry(width=30, textvariable=get_book_subject)
# subject.insert(0, "Subject of the Book.")

author_Lname_lbl = tk.Label(window, text = "Author's Last Name:", font=('calibre',10, 'bold'))
author_Lname = tk.Entry(width=30, textvariable=get_author_Lname)
# author_Lname.insert(0, "Author's Last Name")

author_Other_lbl = tk.Label(window, text = "Author's Other Name:", font=('calibre',10, 'bold'))
author_Other_name = tk.Entry(width=30, textvariable=get_author_Oname)
# author_Other_name.insert(0, "Author's other name")

# submit button to react on Return event 
def btn_submit_return(Event):
    return submit()

# Quit btn to react on return event
def btn_quit_return(Event):
    return window.quit()

# widget and label in it
btn_submit = tk.Button(window, text="Submit", command=submit)
btn_submit.bind('<Return>', btn_submit_return)
btn_quit = tk.Button(window, text="Quit", command=window.quit)
btn_quit.bind('<Return>', btn_quit_return)

book_title_lbl.grid(row=0, column=0)
book_title.grid(row=0, column=1)

subject_lbl.grid(row=1, column=0)
subject.grid(row=1, column=1)

author_Lname_lbl.grid(row=2, column=0)
author_Lname.grid(row=2, column=1)

author_Other_lbl.grid(row=2, column=2)
author_Other_name.grid(row=2, column=3)
# subject.place(x=40, y= 20)

btn_submit.grid(row=3, column=0, sticky="e")
btn_quit.grid(row=3, column=1, sticky="w")

# run event
# book_title.bind("<FocusIn>", temp_text)
# subject.bind("<FocusIn>", temp_text)
# author_Lname.bind("<FocusIn>", temp_text)
# author_Other_name.bind("<FocusIn>", temp_text)


# Run the application
window.mainloop()