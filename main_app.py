# TODO: render a table, implement a search function, add React components,
# spruce it up

from flask import Flask, flash, redirect, render_template, request, session, abort

from ip_manipulation import get_location_dict, get_coord_list, get_country_list

app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    phrase = "Hello world!"
    location_dict = get_location_dict()
    coord_list = get_coord_list(location_dict)
    country_list = get_country_list(location_dict)
    return render_template('layout.html',**locals())

@app.route("/table")
def render_table():
    return render_template('table.js', **locals())

@app.route("/test")
def test():
    return str(get_location_dict())

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('', path)


if __name__ == "__main__":
    app.run()