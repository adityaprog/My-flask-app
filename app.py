from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Title shown in <title>
home_title = "Flask App"

# Path to templates folder
template_dir = os.path.join(app.root_path, 'templates')


@app.route('/')
def home_page():
    return render_template("index.html", flask_title=home_title)


@app.route('/<page>/')
def render_page(page):
    template_path = f"{page}/index.html"
    full_path = os.path.join(template_dir, template_path)

    if os.path.exists(full_path):
        return render_template(
            template_path,
            flask_title=f"{home_title} - {page.capitalize()}",
            heading=page
        )
    else:
        # Page doesn't exist, show custom 404
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404/index.html", flask_title="Page Not Found"), 404


if __name__ == '__main__':
    app.run()
