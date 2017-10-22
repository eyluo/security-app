# TODO: render a table, implement a search function, add React components,
# spruce it up

from flask import Flask, flash, redirect, render_template, request, session, abort

from ip_manipulation import get_location_dict, get_coord_list, get_country_list

app = Flask(__name__)

@app.route("/")
def hello():
    phrase = "Hello world!"
    location_dict = get_location_dict()
    coord_list = get_coord_list(location_dict)
    country_list = get_country_list(location_dict)
    return render_template('layout.html',**locals())

@app.route("/goKnicks")
def goKnicks():
    return "also, go Knicks!"

@app.route("/name")
def name():
    return "Names: "

@app.route("/name/<string:name>")
def getName(name):
    return name

@app.route("/test")
def test():
    return str(get_location_dict())


if __name__ == "__main__":
    app.run()