from flask import Flask, request, render_template, redirect, session

from waitress import serve
app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/form_completed', methods=['GET', "POST"])
def form_completed():
    if request.method == "POST":
        return "Hello from " + request.form["Name"] + " whose age is " + request.form["Age"]
    return render_template("form_completed.html", **locals())


@app.route('/form', methods=['GET', "POST"])
def form():
    if request.method == "POST":
        return str(request.form)
    return render_template("form.html", **locals())


@app.route('/till_if_n/<string:n>', methods=['GET', "POST"])
def till_if_n(n):
    n = int(n)
    return render_template("till_if_n.html", **locals())


@app.route('/till_n/<string:n>', methods=['GET', "POST"])
def till_n(n):
    n = int(n)
    return render_template("till_n.html", **locals())


@app.route('/pass_name_dynamic/<string:name>', methods=['GET', "POST"])
def pass_name_dynamic(name):
    return render_template("pass_name_dynamic.html", **locals())


@app.route('/pass_name', methods=['GET', "POST"])
def pass_name():
    name = "John"
    return render_template("pass_name.html", **locals())


@app.route('/template', methods=['GET', "POST"])
def template():
    return render_template("template.html", **locals())


@app.route('/plus_one/<string:s>', methods=['GET', "POST"])
def plus_one(s):
    n = int(s)
    n += 1
    return str(n)


@app.route('/home', methods=['GET', "POST"])
def home():
    return "Hello Home!"


@app.route('/', methods=['GET', "POST"])
def index():
    return "Hello World!"


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5002)
    #serve(app, host='127.0.0.1', port=5002)
    serve(app, host='0.0.0.0', port=80)