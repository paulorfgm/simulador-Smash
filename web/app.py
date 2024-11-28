from flask import Flask, render_template, request
import csv
import os
from matplotlib.colors import to_rgb
import numpy as np

csv_filename = '../data/saidas/saida3.csv'
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, csv_filename)

app = Flask(__name__)

def load_characters():
    characters = []
    with open(csv_file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            character = {
                "name": row["name"],
                "forca": float(row["forca"]),
                "percentage": float(row["percentage"]),
                "color": to_rgb(row['color'])
            }
            characters.append(row)
    return characters

@app.route("/", methods=["GET", "POST"])
def index():

    characters = load_characters()

    selected_character1 = None
    selected_character2 = None

    return render_template(
        "confrontos.html",
        characters=characters, 
        selected_character1=selected_character1, 
        selected_character2=selected_character2
    )

@app.route("/ranking")
def ranking():
    characters = load_characters()
    characters = sorted(characters, key=lambda x: x['percentage'], reverse=True)
    max_percentage = max(c["percentage"] for c in characters)
    return render_template("ranking.html", characters=characters, max_percentage=max_percentage)

if __name__ == "__main__":
    app.run(debug=True)
