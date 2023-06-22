
"""
Description: In this project, we will use the pandas and tkinter libraries to program a simple program that allows us to easily and conveniently spell words, especially if you have dyslexia like me.

Code author: Luis Nieto Hueso

References: Pandas documentation: https://pandas.pydata.org/docs/ and tkinter: https://docs.python.org/3/library/tk.html
"""

import pandas as pd
from tkinter import *
from tkinter import messagebox

# data extraction
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# how to generate the phonetic
def generate_phonetic():
    word = enter_web.get().upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as e:
        print(e)  # Print the letter that caused the KeyError
        messagebox.showinfo(title='Oops', message="You can only use letters")
        return
    else:
        enter_result.delete("1.0", END)  # Clear any existing content
        enter_result.insert(END, ' '.join(output_list))  # Insert the phonetic representation at the end


# ---------------------------- UI SETUP ------------------------------- #
# That is the main screen for the program
window = Tk()

window.title('Generator of phonetic')
window.config(pady=50, padx=50)

# this is all the labels that I need for the interface
label_phonetic = Label(text='Enter a word: ')
label_phonetic.grid(row=1, column=0)

# these are the Entries that I need for the program

enter_web = Entry(width=35)
enter_web.grid(row=1, column=1, columnspan=2)
enter_web.focus()

enter_result = Text(height=5, width=30)
enter_result.grid(row=3, column=2, padx=0, pady=0)

# These are the buttons I will need for the program

button_pass = Button(text='Submit', command=generate_phonetic)
button_pass.grid(row=4, column=2, padx=0, pady=0)

window.mainloop()
