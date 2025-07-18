from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''<h1>Hello!</h1>
            <p>From Aditya to Siddharth and all my dear users.</p>
            <p>Welcome to my Flask app.</p>'''


if __name__ == '__main__':
    app.run()