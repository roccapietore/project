from functions import get_posts, get_comments_by_post_id, get_posts_by_post_id, get_posts_by_username, add_in_json, \
    content_modification, bookmarks_path, import_json

from flask import Flask, render_template, request, abort, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", posts_data=get_posts())


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    post = get_posts_by_post_id(post_id)
    if not post:
        abort(404)
    elif "#" in post["content"]:
        post["content"] = content_modification(post["content"])
        print(post["content"])
    return render_template("post.html", post=post, comments=get_comments_by_post_id(post_id))


@app.route('/search/')
def search_post():
    search_parameter = request.args.get("s")
    if not search_parameter:
        abort(400)
    search_list = []
    posts = get_posts()
    for post in posts:
        if len(search_list) == 10:
            break
        elif search_parameter.lower() in post["content"].lower():
            search_list.append(post)
    if search_list:
        return render_template("search.html", search_list=search_list, search_parameter=search_parameter)
    return abort(404)


@app.route('/users/<username>')
def get_user(username):
    posts = get_posts_by_username(username)
    if not posts:
        abort(404)
    return render_template("user-feed.html", posts=posts)


@app.route('/tag/<tag_name>')
def post_with_tags(tag_name):
    tags_posts = []
    posts = get_posts()
    for post in posts:
        if tag_name in post["content"]:
            tags_posts.append(post)
    return render_template("tag.html", posts=tags_posts, tag_name=tag_name)


@app.route('/bookmarks/add/<int:post_id>')
def bookmarks_add(post_id):
    posts = get_posts()
    for post in posts:
        if post_id == post["pk"]:
            add_in_json(bookmarks_path, post)
            return redirect("/", code=302)
        elif post_id != post["pk"]:
            abort(404)


@app.route('/bookmarks')
def get_bookmarks():
    return render_template("bookmarks.html", bookmarks=import_json(bookmarks_path))


if __name__ == '__main__':
    app.run(debug=True)
