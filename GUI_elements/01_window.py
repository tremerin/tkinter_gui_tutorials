"""
# Introduction to Creating Windows with Tkinter

Tkinter is the standard GUI library for Python, allowing developers to create graphical applications easily. 
In this tutorial, we cover the basics of creating and customizing a window using Tkinter.

## Features Demonstrated in This Tutorial:

1. **Creating a Window Instance**  
   - The `Tk()` function initializes a new window.

2. **Setting Window Size and Position**  
   - `geometry("420x420")` defines the window's width and height.
   - An alternative version (`geometry("420x420+200+500")`) also specifies the window's position on the screen.
   - `resizable(False, False)` prevents the user from resizing the window.

3. **Setting Window Title**  
   - `title("Testing window")` sets the title displayed on the window's title bar.

4. **Setting a Custom Window Icon**  
   - `iconphoto(True, icon)` changes the default Tkinter icon to a custom one.

5. **Setting the Background Color**  
   - `config(background="green")` applies a background color using a named color.
   - `config(background="#EED7B6")` applies a background color using a hexadecimal code.

6. **Getting Window and Screen Information**  
   - `winfo_width()` and `winfo_height()` retrieve the actual window dimensions.
   - `winfo_screenwidth()` and `winfo_screenheight()` get the screen's resolution.
   - `update_idletasks()` ensures that window properties are updated before fetching size values.

7. **Starting the Event Loop**  
   - `mainloop()` keeps the window open and listens for user interactions.

"""

import tkinter as tk

window = tk.Tk()

window.geometry("420x420")
#window.geometry("420x420+200+500")
window.resizable(False, False)

window.title("Testing window")

icon = tk.PhotoImage(file="./resources/logo42.png")
window.iconphoto(True, icon)

#window.config(background= "green")
window.config(background= "#EED7B6")

window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print(f"window: {width}x{height}, screen: {screen_width}x{screen_height}")


window.mainloop()