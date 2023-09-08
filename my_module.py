from tkinter import *

#def press():
    #value1 = unos_imena.get()
    #value2 = unos_prezimena.get()
    #value3 = unos_mejla.get()
    #value4 = unos_poruke.get()
    #print("Ime: ", value1)
    #print("Prezime: ", value2)
    #print("E-mail: ", value3)
   # print("Poruka: ", value4)


#def restart():
 # name_entry.delete(0, END)
  #surname_entry.delete(0, END)
  #email_entry.delete(0, END)
  #message_entry.delete(0, END)

#def add_values():
    #POTREBNO JE DODATI SAMO IME, A KAD SE KLIKNE NA NJEGA, DA SE PRIKAZU I OSTALI PODACI
    #prikaz_imena = unos_imena.get()

   # lista_vrijednosti.insert(END, prikaz_imena)



#def delete_values():
 #   lista_vrijednosti.delete(0, END)

#def view_values():


def press():
    value1 = unos_imena.get()
    value2 = unos_prezimena.get()
    value3 = unos_mejla.get()
    value4 = unos_poruke.get()
    print("Ime: ", value1)
    print("Prezime: ", value2)
    print("E-mail: ", value3)
    print("Poruka: ", value4)

def restart():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    email_entry.delete(0, END)
    message_entry.delete(0, END)

def add_values():
    prikaz_imena = unos_imena.get()
    prikaz_prezimena = unos_prezimena.get()
    prikaz_mejla = unos_mejla.get()
    prikaz_poruke = unos_poruke.get()

    combined_value = f"Name: {prikaz_imena}\nSurname: {prikaz_prezimena}\nE-mail: {prikaz_mejla}\nMessage: {prikaz_poruke}"
    lista_vrijednosti.insert(END, prikaz_imena)
    saved_values[prikaz_imena] = combined_value  # sacuvaj kombinovanu vrijednost u dictionary

     # ocisti inpute
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    email_entry.delete(0, END)
    message_entry.delete(0, END)

def delete_values():
    selected_index = lista_vrijednosti.curselection()
    if selected_index:
        selected_value = lista_vrijednosti.get(selected_index[0])
        lista_vrijednosti.delete(selected_index[0])

        # remove sacuvanu vrijednost iz dictionary
    if selected_value in saved_values:
        del saved_values[selected_value]

def view_values():
    selected_index = lista_vrijednosti.curselection()
    if selected_index:
        selected_value = lista_vrijednosti.get(selected_index[0])
        if selected_value in saved_values:
            saved_value = saved_values[selected_value]
            values = saved_value.split('\n')
            for value in values:
                field, content = value.split(": ")
                if field == "Name":
                    name_entry.delete(0, END)
                    name_entry.insert(0, content)
                elif field == "Surname":
                    surname_entry.delete(0, END)
                    surname_entry.insert(0, content)
                elif field == "E-mail":
                    email_entry.delete(0, END)
                    email_entry.insert(0, content)
                elif field == "Message":
                    message_entry.delete(0, END)
                    message_entry.insert(0, content)


saved_values = {}


window = Tk()
window.geometry("1000x1000")

frame1 = Frame(window)
frame1.pack()

unos_imena = StringVar()
unos_prezimena = StringVar()
unos_mejla = StringVar()
unos_poruke = StringVar()



ime = Label(frame1, text="Name:", font=("Arial", 12))
ime.grid(row=0, column=0)
name_entry = Entry(frame1, textvariable=unos_imena, bg="white", width=20, borderwidth=3, font=("Arial", 12))
name_entry.grid(row=0, column=1)

prezime = Label(frame1, text="Surname:", font=("Arial", 12))
prezime.grid(row=1, column=0)
surname_entry = Entry(frame1, textvariable=unos_prezimena, bg="white", width=20, borderwidth=3,font=("Arial", 12) )
surname_entry.grid(row=1, column=1)

mejl = Label(frame1, text="E-mail:", font=("Arial", 12))
mejl.grid(row=2,column=0)
email_entry = Entry(frame1, textvariable=unos_mejla, bg="white", width=20, borderwidth=3, font=("Arial", 12))
email_entry.grid(row=2, column=1)

poruka = Label(frame1, text="Message:", font=("Arial", 12))
poruka.grid(row=3, column=0)
message_entry = Entry(frame1, textvariable=unos_poruke, bg="white", width=20, borderwidth=3, font=("Arial", 12))
message_entry.grid(row=3, column=1)


button = Button(window, text="Submit", command=lambda: press())
button.pack()

restart_button = Button(window, text="Restart", command=lambda: restart())
restart_button.pack()





prikaz_imena = StringVar()
prikaz_prezimena= StringVar()
prikaz_mejla = StringVar()
prikaz_poruke = StringVar()
display_frame = Frame(window,borderwidth=2,relief="solid")
display_frame.pack(padx=10, pady=10)
lista_vrijednosti = Listbox(display_frame)
lista_vrijednosti.pack()




add_button = Button(window, text = "Add", command=lambda:add_values())
add_button.pack()

delete_button = Button(window, text="Delete", command=lambda: delete_values())
delete_button.pack()

view_button = Button(window, text="View", command=lambda: view_values())
view_button.pack()




window.mainloop()



