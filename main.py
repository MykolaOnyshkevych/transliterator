from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ukrainian", methods=['POST', 'GET'])
def ukrainian():
    if request.method == 'POST' and "message" in request.form:
        message = str(request.form.get("message"))
        answer = ukrainizator(message)
    return render_template("index.html", answer=answer)


@app.route("/english", methods=['POST', 'GET'])
def english():
    if request.method == 'POST' and "message" in request.form:
        message = str(request.form.get("message"))
        answer = englishyzator(message)
    return render_template("index.html", answer=answer)


@app.route("/both", methods=['POST', 'GET'])
def both():
    if request.method == 'POST' and "message" in request.form:
        message = str(request.form.get("message"))
        answer = both(message)
    return render_template("index.html", answer=answer)


english = list("&qwertyuiop[]asdfghjkl;zxcvbnm,.'")
ukrainian = list("?йцукенгшщзхїфівапролджячсмитьбює")


def match(message, alphabet):
    return not alphabet.isdisjoint(message.lower())


def ukrainizator(message):
    x = english.__str__()
    y = ukrainian.__str__()
    my_table = message.maketrans(y, x)
    return message.translate(my_table)


def englishyzator(message):
    x = english.__str__()
    y = ukrainian.__str__()
    my_table = message.maketrans(x, y)
    return message.translate(my_table)


def both(message):
    x = english.__str__()
    y = ukrainian.__str__()
    new_mess = ""
    for i in message:
        if match(i, set(ukrainian)):
            my_table = i.maketrans(y, x)
            o = i.translate(my_table)
            new_mess = new_mess + o
        else:
            my_table = i.maketrans(x, y)
            o = i.translate(my_table)
            new_mess = new_mess + o
    return new_mess


if __name__ == '__main__':
    app.run(debug=False)
