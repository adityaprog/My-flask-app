from flask import Flask, render_template

app = Flask(__name__)

# Variables

home_title ="Flask App"


@app.route('/')
def hello():
    return render_template("index.html", flask_title= home_title)


if __name__ == '__main__':
    app.run()