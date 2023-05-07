from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
