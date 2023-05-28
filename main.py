from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def sign_in():
    if request.method == 'POST':
        print(request.form)

    return render_template('sign_in.html')


@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    if request.method == 'POST':
        print(request.form)

    return render_template('sign_up.html')


if __name__ == "__main__":
    app.run(debug=True)
