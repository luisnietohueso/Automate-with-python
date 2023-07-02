from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)
new = pd.read_csv('Recipes-All Recipes.csv')
choices = new['Name'].tolist()
print(choices)


@app.route('/')
def generate_menu():
    global choices
    # List of weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Dictionary to store the menu
    menu = {}

    # Generating a random menu for each day of the week
    for day in weekdays:
        menu[day] = random.choice(choices)
        choices.remove(menu[day])

    # Rendering the 'menu.html' template and passing the menu data
    return render_template('menu.html', menu=menu)


if __name__ == '__main__':
    app.run()
