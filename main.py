import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import time
import datetime
import settings
import utils

## TO-DO
# 1. REVIST ORDER OF CONDITION BTW QTY OF BOOKS & AUTHOR'S LAST NAME
# 2. validiate Blank space on spinBox and entry
# 3. time the speed change caused .split(), '',.join() in fThree function

# clear all widget children
def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()


# function to get the fast 3 letters of 
# the author's last name
def fThree (Lname):
    # if len(" ".join(Lname.split())) >= 3:
    if len(Lname) >= 3:
    # return " ".join(Lname.split())[:3]
        return Lname[:3]
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
    get_qty_entry = get_qty.get()
    get_quality = quality.get()
    get_extra = extraWord.get('1.0', 'end')
    get_time_entry = datetime.datetime.now()
    
    # author_Lname.config(highlightthickness=1, highlightcolor="black")
    # books_qty.config(foreground='black')

    if len(get_Lname_entry.strip()) == False:
        msg.set('value')
    elif len(get_Lname_entry) < 3:
        # msg.set(fThree(get_Lname_entry))
        msg.set("Author's Last name must be more then 2 letters")
        author_Lname.focus_set()
        # author_Lname.config(highlightthickness=2, highlightcolor="red")
    else:
        for key, value in capital_dict.items():
            if get_subject_entry.upper() == key:
                data_list = [get_book_entry, get_subject_entry, get_Lname_entry, get_Oname_entry, get_quality, get_extra]
                
                dewey_code = f'{value}-{fThree(get_Lname_entry.upper())}'
                
                data_list.append(dewey_code)
                data_list.append(get_time_entry)
                detail_msg = f'BOOK NAME:\t{get_book_entry.upper()}\nCLASSIFICATION:\t{dewey_code}\nQuantity:\t{get_qty_entry}'
                if get_qty_entry  > 0 :
                    utils.cal_qty(int(get_qty_entry), data_list)
                    msg.set(detail_msg)
                    # style.configure('S.TButton', font=('American typewriter', 11), background='green', foreground='white')
                    # time.sleep(1)
                    get_book_title.set("")
                    # get_book_subject.set("")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    get_author_Lname.set("")
                    get_author_Oname.set("")
                    quality.set('')
                    extraWord.delete('1.0', 'end')
                    book_title.focus_set() 

                else:
                    books_qty.focus_set()
                    books_qty.config(foreground='red')
                    msg.set('Quantity must be greater than 1')



# submit button to react on Return event 
def btn_submit_return(Event):
    return submit()

# Quit btn to react on return event
def btn_quit_return(Event):
    return window.quit()

# combobox selected
def combo(Event):
    subject.select_clear()

def del_text(event):
    extraWord.delete('1.0', 'end')

def no_tab(event):
    event.widget.tk_focusNext().focus()
    return 'break'

def frame1():
    clear_widgets(frame_search)
    frame_book.tkraise()
    frame_book.pack_propagate(False)
    global get_book_title, get_book_subject, get_author_Lname, get_author_Oname, get_qty, quality, msg
    global extraWord, capital_dict, book_title, author_Lname, mewa_logo, as_logo

    dewey_dict = {
        "Fiction":"FIC",
        "Computer science & general works":"000",
        "Philosophy & psychology":100,
        "religion":200,
        "Social sciences":300,
        "Language":400,
        "Science":500,
        "Technology":600,
        "Arts & recreation":700,
        "Literature":800,
        "History & geography":900
        }

    capital_dict = {k.upper(): v for k,v in dewey_dict.items()}


    # declaring string variable
    # for storing the entries value
    get_book_title = tk.StringVar()
    get_book_subject = tk.StringVar()
    get_author_Lname = tk.StringVar()
    get_author_Oname = tk.StringVar()
    get_qty = tk.IntVar(value=1)
    quality = tk.StringVar()
    msg = tk.StringVar()

    # american space logo
    as_logo = ImageTk.PhotoImage(Image.open('images/as.png').resize((100,100)))
    ttk.Label(frame_book,image=as_logo).grid(row=0, column=0, pady=10, padx=10, sticky='w')

    # header text
    ttk.Label(frame_book, text = "American Corner Mombasa", font=('Times',20, 'bold')).grid(row=0, column=1, columnspan=2, padx=10, ipady=10, sticky='ew')

    # mewa logo
    mewa_logo = ImageTk.PhotoImage(Image.open('images/mewa-logo-1.png').resize((100,100)))
    ttk.Label(frame_book,image=mewa_logo).grid(row=0, column=3, pady=10, padx=10, sticky='e')

    # Create the book entry frame with an Entry
    #frm_entry = tk.Frame(master=frame_book)
    book_title_lbl = ttk.Label(frame_book, text = 'Title of the book:', font=('Courier',12, 'bold'))
    book_title = ttk.Entry(frame_book,width=30, textvariable=get_book_title)
    book_title.focus_set()

    subject_lbl = ttk.Label(frame_book, text = 'Subject of the book:', font=('Courier',12, 'bold'))
    subject = ttk.Combobox(frame_book, width=23, textvariable=get_book_subject, font=("serif", 10, "bold"), foreground='black')
    subject['values'] = (
        'Fiction',
        'Computer science & general works',
        'Philosophy & psychology',
        'Religion',
        'Social sciences',
        'Language',
        'Science',
        'Technology',
        'Arts & recreation',
        'Literature',
        'History & geography'
    )
    subject.state(["readonly"])
    subject.current(0)
    subject.bind('<<ComboboxSelected>>', combo)

    books_qty_lbl = ttk.Label(frame_book, text = 'Quantity of the books:', font=('Courier',12, 'bold'))
    books_qty= ttk.Spinbox(frame_book, from_=1, to=100, textvariable=get_qty, width=7, justify='left')

    author_Lname_lbl = ttk.Label(frame_book, text = "Author's Last Name:", font=('Courier',12, 'bold'))
    author_Lname = ttk.Entry(frame_book,width=30, textvariable=get_author_Lname)

    author_Other_lbl = ttk.Label(frame_book, text = "Author's Other Name:", font=('Courier',12, 'bold'))
    author_Other_name = ttk.Entry(frame_book,width=30, textvariable=get_author_Oname)

    # radiobutton to check quality of the book
    state_lbl = ttk.Label(frame_book, text = "State of the book: ", font=('Courier',12, 'bold'))

    quality_values = (
        'New',
        'Used',
        'Old'
    )

    for value in quality_values:
        radioCheck = ttk.Radiobutton(
            frame_book,
            text=value,
            value=value,
            variable=quality
        )
        radioCheck.grid(row=4, column=(quality_values.index(value)+1), padx=10, ipady=4, pady= 10, sticky='w')

    # Text
    extra_lbl = ttk.Label(frame_book, text="Extra Observation:", font=('Courier',12, 'bold'))
    extraWord = tk.Text(frame_book, width=30, height=5)
    extraWord.insert('1.0', 'example co-author name, state or institution that published the book.')
    extraWord['wrap'] = 'word'
    extraWord.bind("<FocusIn>", del_text)
    extraWord.bind("<Tab>", no_tab)

    # Buttons
    btn_submit = ttk.Button(frame_book, text="Submit", command=submit, style='S.TButton')
    btn_submit.bind('<Return>', btn_submit_return)
    btn_quit = ttk.Button(frame_book, text="Quit", command=window.quit, style='Q.TButton')

    # feedback message
    book_detail_lbl = ttk.Label(frame_book, textvariable = msg)

    # GRIDS
    book_title_lbl.grid(row=1, column=0, padx=10, ipady=4, pady=10, sticky='w')
    book_title.grid(row=1, column=1, padx=10, ipady=4, pady=10, sticky='w')

    subject_lbl.grid(row=2, column=0, padx=10, ipady=4, pady=10, sticky='w')
    subject.grid(row=2, column=1, padx=10, ipady=4, pady=10, sticky='w')

    books_qty_lbl.grid(row=2, column=2, padx=10, ipady=4, pady=10, sticky='w')
    books_qty.grid(row=2, column=3, pady= 10, padx=10, sticky='w')

    author_Lname_lbl.grid(row=3, column=0, padx=10, ipady=4, pady=10, sticky='w')
    author_Lname.grid(row=3, column=1, padx=10, ipady=4, pady=10, sticky='w')

    author_Other_lbl.grid(row=3, column=2, ipady=4, pady=10, padx=10, sticky='w')
    author_Other_name.grid(row=3, column=3, padx=10, pady= 10, ipady=4, sticky='w')

    state_lbl.grid(row=4, column=0, padx=10, ipady=4, sticky='w')

    extra_lbl.grid(row=5, column=0, ipady=4, padx=10, pady= 10, sticky='w')
    extraWord.grid(row=5, column=1, columnspan=3, padx=4, ipady=4, pady= 10, sticky='w')

    btn_submit.grid(row=6, column=1, sticky="w", padx=10, ipady=4, pady= 10)
    btn_quit.grid(row=6, column=3, sticky="w", padx=10, ipady=4, pady= 10) 

    book_detail_lbl.grid(row=7, column=0, columnspan=4, pady=10)

def search_frame():
    global mewa_logo, as_logo
    clear_widgets(frame_book)
    frame_search.tkraise()

    # american space logo
    as_logo = ImageTk.PhotoImage(Image.open('images/as.png').resize((100,100)))
    ttk.Label(frame_search,image=as_logo).grid(row=0, column=0, pady=10, padx=10, sticky='w')

    # header text
    ttk.Label(frame_search, text = "American Corner Mombasa", justify="center", font=('Times',20, 'bold')).grid(row=0, column=1, columnspan=2, padx=10, ipady=10, sticky='ew')

    # mewa logo
    mewa_logo = ImageTk.PhotoImage(Image.open('images/mewa-logo-1.png').resize((100,100)))
    ttk.Label(frame_search,image=mewa_logo).grid(row=0, column=3, pady=10, padx=10, sticky='e')
    # print("hi")

    # Create search bar
    search_lbl = ttk.Label(frame_search, text="Search")
    search_lbl.grid(row=1, column=0, padx=10, ipady=10, sticky='w')
    
    search_entry = ttk.Entry(frame_search, text="Search", width=30)
    search_entry.grid(row=1, column=1, columnspan=2, padx=10, ipady=10, sticky='w')

    search_btn = ttk.Button(frame_search, text="Search")
    search_btn.grid(row=1, column=3, padx=10, ipady=10, sticky='w')


def navbar():
    frame_navbar.tkraise()
    # btn_names = (
    #     'Search',
    #     'Register a book',
    # )

    # for btn in btn_names:
    #     btns = ttk.Button(
    #         frame_navbar,
    #         text=btn,
    #         style="TButton"
    #     )
    #     btns.grid(row=(btn_names.index(btn)+1), column=0, padx=10, ipady=4, pady= 10, sticky='w')
    #     btns["command"]=search_frame
    btn_search = ttk.Button(frame_navbar, text="search", style="TButton", command=search_frame)
    btn_search.grid(row=0, column=0, padx=10, ipady=4, pady= 10, sticky='w')

    btn_reg = ttk.Button(frame_navbar, text="Register a book", style="TButton", command=frame1)
    btn_reg.grid(row=1, column=0, padx=10, ipady=4, pady= 10, sticky='w')

        

# Set up the window
window = tk.Tk()
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.title("Book Classifier")

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - settings.WIDTH / 2)
center_y = int(screen_height/2 - settings.HEIGHT / 2)

window.geometry(f'{settings.WIDTH}x{settings.HEIGHT}+{center_x}+{center_y}')
# window.resizable(width=False, height=False)

style = ttk.Style()

style.configure(
    'B.TFrame', background=settings.bg_color,
)

style.configure(
    'S.TFrame', background='orange',
)

style.configure(
    'N.TFrame', background='yellow',
)



frame_book = ttk.Frame(window, width=settings.WIDTH, height=settings.HEIGHT, style='B.TFrame')
frame_book.grid(row=0, column=1, sticky='nesw')
frame_book.pack_propagate(False)
# frame_book.columnconfigure(0, weight=1)
# frame_book.rowconfigure(0, weight=1)

# Navbar frame
frame_navbar = ttk.Frame(window, style='N.TFrame')
frame_navbar.grid(row=0, column=0, sticky='nesw')
# frame_navbar.columnconfigure(0, weight=1)
# frame_navbar.rowconfigure(0, weight=1)
frame_navbar.pack_propagate(False)

# search frame
frame_search = ttk.Frame(window,style='S.TFrame')
frame_search.grid(row=0, column=1, sticky='nesw')
# frame_search.columnconfigure(0, weight=1)
# frame_search.rowconfigure(0, weight=1)
frame_search.pack_propagate(False)


style.configure(
"TLabel",
background=settings.bg_color,
foreground='#ffffff',
# bordercolor='red',
# borderwidth = 4
)

style.configure(
    'TRadiobutton', 
    background='#34568b',
    foreground='#ffffff',
    # borderwidth=0
    # activebackground='red'
)
style.map('TRadiobutton',
        foreground=[('disabled', 'yellow'),
                    ('pressed', '#ffffff'),
                    ('active', '#ffffff')],
        background=[('active', '#6a8ec8'),
                    ('selected', '#152238'),],
                    indicatoron=('#4a6984'),
                    borderwidth='0',
                    )
                    
    
# style.theme_use('alt')
style.configure('TButton', background='#4572ba', foreground='white')
style.map('S.TButton', background=[('active', '#00ff00')])
style.map('Q.TButton', background=[('active', '#ff0000')])


# style.map('TButton', background=[('active', '#ff0000')])

# style.map("C.RadioButton",
#     foreground=[('pressed', 'red'), ('active', 'blue')],
#     background=[('pressed', '!disabled', 'black'), ('active', 'white')]
#     )
# style.map('TRadiobutton',
#         indicatoron=[('pressed', '#ececec'), ('selected', '#4a6984')])

# style.configure(
#     'TSpinbox', background=settings.bg_color,
#     foreground='#c7d5ea',
# )

# for child in frame_book.winfo_children():


frame1()
navbar()

# Run the application
window.mainloop()