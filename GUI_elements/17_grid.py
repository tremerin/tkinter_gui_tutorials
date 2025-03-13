import tkinter as tk

window = tk.Tk()

#first name
lbl_first_name = tk.Label(window, text= "First name", width= 15).grid(row= 0, column= 0)
entry_frist_name = tk.Entry(window).grid(row= 0, column= 1)
#last name
lbl_last_name = tk.Label(window, text= "Last name").grid(row= 1, column= 0)
entry_last_name = tk.Entry(window).grid(row= 1, column= 1)
#email
lbl_email = tk.Label(window, text= "Email").grid(row= 2, column=0 )
entry_email = tk.Entry(window).grid(row= 2, column= 1)

btn_submit = tk.Button(window, text= "Submit", height= 1, width= 10).grid(row= 4, column= 0, columnspan= 2)

window.mainloop()