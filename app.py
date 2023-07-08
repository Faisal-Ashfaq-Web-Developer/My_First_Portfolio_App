# from flask import Flask, render_template, request
#
# app = Flask(__name__)
# app.config['STATIC_FOLDER'] = 'static'
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True, port=8000)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
