import os
from flask import Flask, request, redirect, render_template, url_for
port = int(os.environ.get("PORT",5000))

app = Flask(__name__)
app.secret_key = "secret key"

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to avoid caching the rendered page (max-age=0).
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/home')
def menu_home():
    return render_template('index.html')

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/landing')
def landing():
	return render_template('landing.html')

@app.route('/generic')
def generic():
	return render_template('generic.html')

@app.route('/elements')
def elements():
	return render_template('elements.html')

@app.errorhandler(404)
def file_not_found(error):
	return render_template('file_not_found.html')

if __name__ == "__main__":
    app.run(debug=True)
