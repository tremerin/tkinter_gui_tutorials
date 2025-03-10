import tkinter as tk

window = tk.Tk()

listbox = tk.Listbox(window,
                    font= ("Constantia", 25),
                    width= 15,
                    bg= "#9329af",
                    selectmode="multiple"
                    )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "taco")
listbox.insert(3, "burger")
listbox.config(height= listbox.size())

def submit():
    #print(listbox.get(listbox.curselection()))
    for food in listbox.curselection():
        print(listbox.get(food))

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height= listbox.size())

def delete():
    #listbox.delete(listbox.curselection())
    for food in reversed(listbox.curselection()):
        listbox.delete(food)
    listbox.config(height= listbox.size())

#Buttons
submit_button = tk.Button(window, text= "submit", command= submit)
submit_button.pack()

add_button = tk.Button(window, text= "add", command= add)
add_button.pack()

delete_button = tk.Button(window, text= "delete", command= delete)
delete_button.pack()

entryBox = tk.Entry(window)
entryBox.pack()

window.mainloop()