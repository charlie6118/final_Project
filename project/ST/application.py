from Stock import Stock
from helper import *
import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
import time

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():

    return render_template("search.html")

@app.route("/search", methods=["GET", "POST"])
def search():

    """Get stock quote."""
    if request.method == "POST":

        stock_exist = check(request.form.get("month"), request.form.get("symbol"))
        if not stock_exist:

            return apology("Can't find it")


        stock = get(request.form.get("month"), request.form.get("symbol"))

        string = ''
        if stock.dic["5_days"] == stock.dic["20_days"] or stock.dic["5_days"] == stock.dic["60_days"] or stock.dic["20_days"] == stock.dic["60_days"]:
            string += 'True'
        else:
            string += 'False'

        return render_template("quoted.html", symbol = request.form.get("symbol"), line_5 = stock.dic["5_days"], line_20 = stock.dic["20_days"], line_60 = stock.dic["60_days"], intersection = string)

    else:
        return render_template("search.html")
