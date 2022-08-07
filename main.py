import tkinter as tk
from openpyxl import workbook, load_workbook
from PIL import ImageTk
from PIL import Image
import settings
# import utils
# import widgets


# Set up the window
window = tk.Tk()
window.title("Book Classifier")

# Define geometry of the window
window.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')       

# open active excel workbook
wb = load_workbook('books.xlsx')
# open the active work sheet
ws = wb.active

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
    
    author_Lname.config(highlightthickness=1, highlightcolor="black")
    
    # print("Title of the book: " + get_book_entry)
    # print("Subject of the book:  " + get_subject_entry)
    # print("Author's last name: " + get_Lname_entry)
    # print("Author's other names: " + get_Oname_entry)
    if get_Lname_entry == "":
        # book_detail_lbl.grid(row=4, column=0)
        # book_detail_lbl['text']= ""
        msg.set('value')
        
        print("Now Dewey code generated")
    elif len(get_Lname_entry) < 3:
        msg.set(fThree(get_Lname_entry))
        author_Lname.focus_set()
        author_Lname.config(highlightthickness=2, highlightcolor="red")
        # print(fThree(get_Lname_entry))
    else:
        # print('msg is resetting')
        # msg.set('')
        for key, value in capital_dict.items():
            if get_subject_entry.upper() == key:
                data_list = [get_book_entry, get_subject_entry, get_Lname_entry, get_Oname_entry]
                dewey_code = f'{value} - {fThree(get_Lname_entry)}'
                # print(dewey_code)
                data_list.append(dewey_code)
                # print(data_list)
                detail_msg = f'BOOK NAME:\t{get_book_entry}\nCLASSIFICATION:\t{dewey_code}'
                # print("Dewey code is: ", value, "-", fThree(get_Lname_entry))
                ws.append(data_list)
                # save the workbook
                wb.save('books.xlsx')
                # book_detail_lbl = tk.Label(window, text = detail_msg, font=('calibre',10, 'bold'))
                # book_detail_lbl['text']= ""
                # book_detail_lbl['text']= detail_msg
                # print('msg ')
                msg.set(detail_msg)
                # print(True)
                # print("The subject is not found")
                # print(False)
                get_book_title.set("")
                get_book_subject.set("")
                get_author_Lname.set("")
                get_author_Oname.set("")
                book_title.focus_set()
    # print(msg)
    # print('msg is resetting')
    # msg.set('')

# submit button to react on Return event 
def btn_submit_return(Event):
    return submit()

# Quit btn to react on return event
def btn_quit_return(Event):
    return window.quit()

# declaring string variable
# for storing the entries value
get_book_title = tk.StringVar()
get_book_subject = tk.StringVar()
get_author_Lname = tk.StringVar()
get_author_Oname = tk.StringVar()
msg = tk.StringVar()

# american space logo
as_logo = ImageTk.PhotoImage(Image.open('images/as.png').resize((100,100)))
tk.Label(image=as_logo).grid(row=0, column=0, pady=10, ipadx=10, sticky='w')

# header text
tk.Label(window, text = "American Corner Mombasa", font=('Times',20, 'bold')).grid(row=0, column=1, columnspan=2, ipady=10, sticky='ew')

# mewa logo
mewa_logo = ImageTk.PhotoImage(Image.open('images/mewa-logo-1.png').resize((100,100)))
tk.Label(image=mewa_logo).grid(row=0, column=3, pady=10, ipadx=10, sticky='e')

# Create the book entry frame with an Entry
#frm_entry = tk.Frame(master=window)
book_title_lbl = tk.Label(window, text = 'Title of the book:', font=('Courier',12, 'bold'))
book_title = tk.Entry(width=30, textvariable=get_book_title)
book_title.focus_set()

subject_lbl = tk.Label(window, text = 'Subject of the book:', font=('Courier',12, 'bold'))
subject = tk.Entry(width=30, textvariable=get_book_subject)
# subject.insert(0, "Subject of the Book.")

author_Lname_lbl = tk.Label(window, text = "Author's Last Name:", font=('Courier',12, 'bold'))
author_Lname = tk.Entry(width=30, textvariable=get_author_Lname)

author_Other_lbl = tk.Label(window, text = "Author's Other Name:", font=('Courier',12, 'bold'))
author_Other_name = tk.Entry(width=30, textvariable=get_author_Oname)
# author_Other_name.insert(0, "Author's other name")

# widget and label in it
btn_submit = tk.Button(window, text="Submit", command=submit, font=('Courier',12, 'bold'))
btn_submit.bind('<Return>', btn_submit_return)
btn_quit = tk.Button(window, text="Quit", command=window.quit, font=('Courier',12, 'bold'))

# feedback message
book_detail_lbl = tk.Label(window, textvariable = msg, font=('Courier',12, 'bold'))

# GRIDS
book_title_lbl.grid(row=1, column=0, ipadx=10, ipady=4, pady=10, sticky='w')
book_title.grid(row=1, column=1, ipadx=10, ipady=4, pady=10, sticky='w')

subject_lbl.grid(row=2, column=0, ipadx=10, ipady=4, pady=10, sticky='w')
subject.grid(row=2, column=1, ipadx=10, ipady=4, pady=10, sticky='w')

author_Lname_lbl.grid(row=3, column=0, ipadx=10, ipady=4, pady=10, sticky='w')
author_Lname.grid(row=3, column=1, ipadx=10, ipady=4, pady=10, sticky='w')

author_Other_lbl.grid(row=3, column=2, ipadx=10, ipady=4, pady=10)
author_Other_name.grid(row=3, column=3, ipadx=10, ipady=4, pady= 10, sticky='w')
# subject.place(x=40, y= 20)

btn_submit.grid(row=4, column=1, sticky="w", ipadx=10, ipady=4)
btn_quit.grid(row=4, column=3, sticky="w", ipadx=10, ipady=4) 

book_detail_lbl.grid(row=5, column=0, columnspan=4, pady=10)


# Run the application
window.mainloop()