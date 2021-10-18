from functions import get_posts, import_json, get_comments_by_post_id

from flask import Flask, render_template, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", posts_data=get_posts())


if __name__ == '__main__':
    app.run(debug=True)