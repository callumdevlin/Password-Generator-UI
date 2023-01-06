import customtkinter as ctk
import random as rd
import time

#VARIABLES
LETTERS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_LOWER = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SYMBOLS = "~?!£$%^&*()"
LENGTH = 0

#Uses strength value to decide what to include in the password string
def generate_pass():
	STRENGTH = slider.get()
	ALL = ""
	match STRENGTH:
		case 0:
			LENGTH = 5
			ALL += LETTERS_LOWER
		case 1:
			LENGTH = 10
			ALL += LETTERS_LOWER
			ALL += NUMBERS
		case 2:
			LENGTH = 15
			ALL += LETTERS_LOWER
			ALL += NUMBERS
			ALL += LETTERS_UPPER
		case 3:
			LENGTH = 20
			ALL += LETTERS_LOWER
			ALL += NUMBERS
			ALL += LETTERS_UPPER
			ALL += SYMBOLS
		case 4:
			LENGTH = 30
			ALL += LETTERS_LOWER
			ALL += NUMBERS
			ALL += LETTERS_UPPER
			ALL += SYMBOLS

	password = "".join(rd.sample(ALL, LENGTH))
	print(password)
	
	#Sends password to tkinter label
	str_val.configure(text=password)

	#Clears users clipboard then copies the password to it
	root.clipboard_clear()
	root.clipboard_append(password)

###########################################################################


#Tkinter GUI
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x400")
root.title('Password Generator')
root.resizable(False, False)
root.config(padx=20, pady=20)


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

mainlabel = ctk.CTkLabel(master=frame, text="Password Generator")
mainlabel.pack(pady=20, padx=10, side=ctk.TOP)

label = ctk.CTkLabel(master=frame, text="Strength")
label.pack(pady=10)

slider = ctk.CTkSlider(master=frame, from_=0, to=4, number_of_steps=4)
slider.pack(padx=10)


str_val = ctk.CTkLabel(master=frame, text="...")
str_val.pack(pady=50)


button = ctk.CTkButton(master=frame, text="Generate", command=generate_pass)
button.pack(side=ctk.BOTTOM, pady=20)

root.mainloop()