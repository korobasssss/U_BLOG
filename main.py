from collections import namedtuple

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY DATABASE URI'] = 'postgres://postgres:123@localhost/py_sweater'
# db = SQLAlchemy(app)

Message = namedtuple('Message', 'text')
messages = []


@app.route("/", methods=["POST", "GET"])
def sign_in():
    if request.method == 'POST':
        print(request.form)

    return render_template('sign_in.html')


@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        print(request.form)

    return render_template('sign_up.html')


@app.route("/main_page")
def main_page():
    return render_template('main_page.html', messages=messages)


@app.route("/post_message", methods=['POST'])
def post_message():
    text = request.form['text']
    messages.append(Message(text))
    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run(debug=True)
