"""
Aidan Wong
Clueless
SoftDev
K09 - Exploring Flask
2024-09-23
time spent: 1.0
"""

import random

from flask import Flask
app = Flask(__name__)

def createTable(x):
    returnable = ""
    for _ in range(len(x)):
        returnable += f"""
        <tr>
            <td> {list(x.keys())[_]} </td>
            <td> {list(x.values())[_]} </td>
        </tr>
        """
    return returnable

@app.route("/")
def printRand():
    with open("occupations.csv") as file: # Open file with this method so it closes by itself
        data = file.read().strip().split("\n")

        occupation = {}
        weights = []

        for i in range(1, len(data)-1):
            splitted = data[i].rsplit(",", 1) # Split by first comma from the right
            splitted[0] = splitted[0].replace('"', "") # Remove quotes if present
            occupation[splitted[0]] = splitted[1] # Add to dictionary
            weights.append(float(splitted[1])) # Append weight value to weight list

        randO = random.choices(list(occupation), weights, k=1)

        # fstring to make things look nicer and clean up code, double braces are for fstring formatting
        return f"""
        <head>
            <style>
                table {{  
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 8px;
                }}
                td:nth-child(2) {{
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <h1>Clueless: Aidan Wong, Qianjun Zhou, Eva Black</h1>
            <p>Your future occupation is: {str(randO[0])} (Rarity: {occupation[str(randO[0])]}%)</p>
            <table>
                <tr>
                    <th>Occupations</th>
                    <th>Weights (%)</th>
                </tr>
                {createTable(occupation)}
            </table>
        </body>
        """

# app.debug = True
app.run()
