from collections import namedtuple

from django.shortcuts import render

from flask import Flask, render_template, request, redirect, url_for

import work_with_data as db

app = Flask(__name__)
db.init()

Message = namedtuple('Message', 'text')
messages = []

# curr_user = ()
curr_user_index = -1


@app.route("/", methods=["POST", "GET"])
def sign_in():
    global curr_user_index
    # global curr_user
    if request.method == 'POST':
        curr_user_index = db.find_user(request.form['name'], request.form['password'])
        print(curr_user_index)
        if curr_user_index != -1:
            # curr_user = db.user_data(curr_user_index)
            db.user_data(curr_user_index)
            return redirect(url_for('main_page'))

    return render_template('sign_in.html')


@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        if not db.check_user_in_base(request.form['username']):
            if request.form['password'] == request.form['repeat_password']:
                db.add_user(request.form['name'], request.form['surname'],
                            request.form['username'], request.form['password'])
                return redirect(url_for('sign_in'))

    return render_template('sign_up.html')


@app.route("/main_page")
def main_page():
    global curr_user_index
    # global curr_user

    if curr_user_index != -1:
        return render_template('main_page.html',
                               username=db.user_data(curr_user_index)[3],
                               messages=db.take_message(curr_user_index))


@app.route("/post_message", methods=['POST'])
def post_message():
    global curr_user_index

    text = request.form['text']
    db.add_message(curr_user_index, text)

    db.user_data(curr_user_index)

    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run(debug=True)
