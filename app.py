#!/usr/bin/env python
import os
import requests
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['url']
            r = requests.get(url)
            print(r.text)
        except:
            errors.append("Unable to get URL. Please make sure it's valid and try again.")

    return render_template('index.html', errors=errors, results=results)

#def index(request):
    #r = requests.get('http://httpbin.org/status/418')
    #print(r.text)
    #return HttpResponse('<pre>' + r.text + '</pre>')

if __name__ == "__main__":
    app.run()
