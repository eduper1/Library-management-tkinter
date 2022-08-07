# import widgets

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