from functions import get_posts, get_comments_by_post_id, get_posts_by_post_id, get_posts_by_username

from flask import Flask, render_template, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", posts_data=get_posts())


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    post = get_posts_by_post_id(post_id)
    if not post:
        abort(404)
    return render_template("post.html", post=post, comments=get_comments_by_post_id(post_id))


if __name__ == '__main__':
    app.run(debug=True)