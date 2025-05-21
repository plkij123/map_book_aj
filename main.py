from tkinter import *

import tkintermapview

users:list = []


def add_user():
    zmienna_imie = Entry_name.get()
    zmienna_nazwisko = Entry_surname.get()
    zmienna_miejscowosc = Entry_location.get()
    zmienna_post = Entry_posts.get()
    user={'name':zmienna_imie, 'surname':zmienna_nazwisko, 'location':zmienna_miejscowosc, 'post':zmienna_miejscowosc}
    users.append(user)
    print(users)



    Entry_name.delete(0, END)
    Entry_surname.delete(0, END)
    Entry_location.delete(0, END)
    Entry_posts.delete(0, END)

    Entry_name.focus()

    show_users()


def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(users):
        listbox_lista_obiektow.insert(idx, user['name'])

def remove_user():
    i=listbox_lista_obiektow.index(ACTIVE)
    print()
    users.pop(i)
    show_users()

def edit_user():
    i=listbox_lista_obiektow.index(ACTIVE)
    name=users[i]['name']
    surname=users[i]['surname']
    location=users[i]['location']
    post=users[i]['post']

    Entry_name.insert(0,name)
    Entry_surname.insert(0,surname)
    Entry_location.insert(0,location)
    Entry_posts.insert(0,post)

    button_dodaj_obiekt.config(text='zapisz',command=lambda:print('aaa'))

def update_user(i):
    new_name=entry_name.get()
    new_surname=entry_surname.get()
    new_locaton=entry_location.get()
    new_posts=entry_posts.get()

    user(i)




    Entry_name.delete(0, END)
    Entry_surname.delete(0, END)
    Entry_location.delete(0, END)
    Entry_posts.delete(0, END)
    Entry_name.focus


    button_dodaj_obiekt.config(text='dodaj obiekt',command=add_user)
    show_users()


    def show_users():
        i=listbox_lista_obiektow.index(ACTIVE)
        name=users(i)
        surname=users(i)
        location=users(i)
        post=users[i]
        label_szczegoly_name_wartosc.config(text=name)
        label_szczegoly_surname_wartosc.config(text=surname)
        label_szczegoly_location_wartosc.config(text=location)
        label_szczegoly_posts_wartosc.config(text=post)

root = Tk()
root.geometry("1200x760")
root.title("Map Book DK")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)






#ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista użytkowników")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow=Listbox(ramka_lista_obiektow, width=50, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text ='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt',command=remove_user)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt',command=edit_user)
button_edytuj_obiekt.grid(row=2, column=2)

#ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Imię:")
label_name.grid(row=1, column=0, sticky=W)
label_surmane=Label(ramka_formularz, text="Nazwisko:")
label_surmane.grid(row=2, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=3, column=0, sticky=W)
label_posts=Label(ramka_formularz, text="Postów:")
label_posts.grid(row=4, column=0, sticky=W)

Entry_name=Entry(ramka_formularz)
Entry_name.grid(row=1, column=1)
Entry_surname=Entry(ramka_formularz)
Entry_surname.grid(row=2, column=1)
Entry_location=Entry(ramka_formularz)
Entry_location.grid(row=3, column=1)
Entry_posts=Entry(ramka_formularz)
Entry_posts.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text='Dodaj obiekt',command=add_user)
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

#ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegóły obiektu:")
label_szczegoly_obiektow.grid(row=0, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Imię:")
label_szczegoly_name.grid(row=1, column=0)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=1)
label_szczegoly_surname=Label(ramka_szczegoly_obiektow, text="Nazwisko:")
label_szczegoly_surname.grid(row=1, column=2)
label_szczegoly_surname_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_surname_wartosc.grid(row=1, column=3)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=4)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=5)
label_szczegoly_posts=Label(ramka_szczegoly_obiektow, text="Posty:")
label_szczegoly_posts.grid(row=1, column=6)
label_szczegoly_posts_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_posts_wartosc.grid(row=1, column=7)

#ramka_mapa
map_widget =tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.0)
map_widget.set_zoom(6)



root.mainloop()