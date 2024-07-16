from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.ttk import Entry
from password_generator import PasswordGenerator
import pyperclip
import json

# Function to handle password generation
def password():
    # Inner function to retrieve user input, generate a password, and update the GUI
    def get_info():
        new_pass.nr_letters = int(nr_letters_entry.get())
        new_pass.nr_symbols = int(nr_symbols_entry.get())
        new_pass.nr_numbers = int(nr_numbers_entry.get())

        # Display the generated password in the entry field and copy it to clipboard
        final_pass = new_pass.pass_making()
        password_entry.insert(0, final_pass)
        pyperclip.copy(final_pass)
        new_window.destroy()

    # Create an instance of the PasswordGenerator class
    new_pass = PasswordGenerator()

    # Create a new Tkinter window for password input
    new_window = Tk()
    new_window.config(padx=10, pady=10)
    new_window.maxsize()
    new_window.title("Password Information")
    info_lable = Label(new_window, text="Please provide the following information:\n")
    info_lable.grid(column=0, row=0, columnspan=2)
    nr_letters_lable = Label(new_window, text="Number of letters:")
    nr_letters_lable.grid(column=0, row=1, sticky=W)
    nr_symbols_lable = Label(new_window, text="Number of symbols:")
    nr_symbols_lable.grid(column=0, row=2, sticky=W)
    nr_numbers_lable = Label(new_window, text="Number of digits:")
    nr_numbers_lable.grid(column=0, row=3, sticky=W)
    nr_letters_entry = Entry(new_window, width=11)
    nr_letters_entry.grid(column=1, row=1, sticky=W)
    nr_symbols_entry = Entry(new_window, width=11)
    nr_symbols_entry.grid(column=1, row=2, sticky=W)
    nr_numbers_entry = Entry(new_window, width=11)
    nr_numbers_entry.grid(column=1, row=3, sticky=W)
    get_pass_info = Button(new_window, text="Generate", command=get_info, width=32)
    get_pass_info.grid(column=0, row=4, columnspan=2, sticky=W)

# Function to handle saving of password details
def save():

    # Check if any required fields are empty
    if not website_entry.get() or not username_entry.get() or not password_entry.get():
        messagebox.showwarning(title="Error", message="Please fill All necessary the fields")

    # Confirm saving the details with the user
    else:
        ask_for_save = messagebox.askokcancel(title=website_entry.get(),
                                              message="Are you sure to save these information for this "
                                                      "website/application?")
        if ask_for_save:
            # Prepare new data to be added to the JSON file
            new_data = {
                website_entry.get(): {
                    "username": username_entry.get(),
                    "password": password_entry.get()}
            }
            try:
                with open("pass.json", "r") as data:
                    pass_file = json.load(data)

            except (FileNotFoundError,json.decoder.JSONDecodeError):
                with open("pass.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                pass_file.update(new_data)
                with open("pass.json", "w") as data:
                    json.dump(pass_file, data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# Function to handle searching for password details
def search():
    website = website_entry.get()
    try:
        with open("pass.json", "r") as data:
            pass_file = json.load(data)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title=website, message="Sorry, No Data File Found")
    else:
        if website in pass_file:
            messagebox.showinfo(title=website,message=f"Username:{pass_file[website]["username"],}\nPassword:{pass_file[website]["password"]}")
        else:
                messagebox.showinfo(title=website_entry.get(),message="There is no information for this website!")

# Main application window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
style = Style()
style.configure('Custom.TButton', background='blue', foreground='white', font=('Arial', 12))

# Frame for the logo

logo_frame = Frame(window)
logo_frame.grid(column=1, row=0)

image = PhotoImage(file="pass.png")
canvas = Canvas(logo_frame, width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

#Frame for inputs and buttons

input_frame = Frame(window)
input_frame.grid(column=0, row=1, columnspan=3)

###########Lables##############

website_lable = Label(input_frame, text="Website:")
website_lable.grid(column=0, row=0, sticky=W)
username_label = Label(input_frame, text="Email/Username:")
username_label.grid(column=0, row=1, sticky=W)
password_lable = Label(input_frame, text="Password:")
password_lable.grid(column=0, row=2, sticky=W)

###########Entries#################

website_entry: Entry = Entry(input_frame, width=24)
website_entry.grid(column=1, row=0, sticky=W)
website_entry.focus()
username_entry = Entry(input_frame, width=42)
username_entry.insert(0, "aminnekouei@gmail.com")
username_entry.grid(column=1, row=1, columnspan=2)
password_entry = Entry(input_frame, width=24)
password_entry.grid(column=1, row=2, sticky=W)

# ########Buttons###################

pss_generator_button = Button(input_frame, text="Generate Password", command=password)
pss_generator_button.grid(column=2, row=2, sticky=E)
add_button = Button(input_frame, text="Add")
add_button.config(width=42, command=save)
add_button.grid(row=3, column=1, columnspan=2)
search_button = Button(input_frame,text="Search",command=search,width=16)
search_button.grid(column=2, row=0, sticky=E)


window.mainloop()
