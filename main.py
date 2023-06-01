from collections import namedtuple

from django.shortcuts import render

from flask import Flask, render_template, request, redirect, url_for

from User import User

app = Flask(__name__)

Message = namedtuple('Message', 'text')
messages = []

users = []
index = -1


def check_user_in_db(someone):
    for local_index in range(len(users)):
        if someone.form['name'] == users[local_index].get_name and \
                someone.form['password'] == users[local_index].get_password:
            return local_index
    return -1


def new_user(someone):
    global users
    users.append(User(someone.form['name'], someone.form['surname'],
                      someone.form['username'], someone.form['password'], []))
    print(users)


def name(requests):
    return render(requests, 'main_page.html', {'username': users[index].get_username})


@app.route("/", methods=["POST", "GET"])
def sign_in():
    global index
    global users
    if request.method == 'POST':
        print(request.form)
        print(users)

        for local_index in range(len(users)):
            print(request.form['name'], request.form['password'])
            print(users[local_index].get_username, users[local_index].get_password)
            if request.form['name'] == users[local_index].get_username and \
                    request.form['password'] == users[local_index].get_password:
                index = local_index
                print(index)
                return redirect(url_for('main_page'))

        # local_user_index = check_user_in_db(request)
        # if local_user_index != -1:
        #     print(request.form)
        #     index = local_user_index
        #     return redirect(url_for('main_page'))

    return render_template('sign_in.html')


@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        if request.form['password'] == request.form['repeat_password']:
            new_user(request)
            return redirect(url_for('sign_in'))

    return render_template('sign_up.html')


@app.route("/main_page")
def main_page():
    global index
    global users
    print(users)
    if index != -1:
        # print(messages)
        print(users[index].messages)
        return render_template('main_page.html', username=users[index].get_username, messages=users[index].messages)


@app.route("/post_message", methods=['POST'])
def post_message():
    global users
    text = request.form['text']
    print(text)
    users[index].messages.append(text)

    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run(debug=True)
