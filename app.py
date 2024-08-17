#!/usr/bin/python3
""" flask app home view """
from datetime import datetime
from flask import Flask, render_template
import random


app = Flask(__name__)

class PageVisit:
    """ class to handle count of page visits """
    COUNT = 0

    def count(self):
        """ count function handling number of visits """
        PageVisit.COUNT += 1
        return PageVisit.COUNT

class BannerColors:
    """colors class. Stores all colors used """
    COLORS = [
        'lightcoral', 'salmon', 'red', 'firebrick', 'pink', 'gold', 'yellow',
        'khaki', 'darkkhaki', 'violet', 'blue', 'purple', 'indigo', 'lime',
        'greenyellow', 'green', 'olive', 'darkcyan', 'aqua', 'skyblue',
        'tan', 'sienna', 'gray', 'silver'
    ]
    def get_colors(self):
        """ gets a random color """
        return sample(BannerColors.COLORS, 5)

@app.route('/')
def home():
    """ home page view """
    banner_colors = BannerColors.get_colors()

    return render_template("index.html", data={
        "now": datetime.now(),
        "page_visit": PageVisit(),
        "banner_colors": {
            "display": banner_colors,
            "js": json.dumps(banner_colors)
        }
    })
