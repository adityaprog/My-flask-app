from flask import Flask, render_template, url_for

app = Flask(__name__)

# Variables

home_title ="Flask App"


@app.route('/')
def home_page():
    return render_template("index.html", flask_title= home_title)


if __name__ == '__main__':
    app.run()