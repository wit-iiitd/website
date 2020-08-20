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

@app.route('/updates')
def updates():
    return render_template('updates.html')

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/opportunities')
def opportunities():
    return render_template('opportunities.html')

@app.route('/opportunities/scholarships')
def scholarships():
    return render_template('scholarships.html')

@app.route('/opportunities/internships')
def internships():
    return render_template('internships.html')

@app.route('/opportunities/competitive-programming')
def cp():
    return render_template('cp.html')

@app.route('/opportunities/dev-clubs')
def devclubs():
    return render_template('devclubs.html')

@app.route('/opportunities/opensource')
def opensource():
    return render_template('opensource.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/resources/sde-interview')
def resourcesSde():
    return render_template('resources-sde.html')

@app.route('/resources/pm-interview')
def resourcesPM():
    return render_template('resources-pm.html')

@app.route('/resources/design')
def design():
    return render_template('resources-design.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/landing')
# def landing():
# 	return render_template('landing.html')

# @app.route('/generic')
# def generic():
# 	return render_template('generic.html')

# @app.route('/elements')
# def elements():
# 	return render_template('elements.html')

@app.errorhandler(404)
def file_not_found(error):
	return render_template('file_not_found.html')

if __name__ == "__main__":
    app.run(debug=True)
