import json

POST_PATH = 'data/data.json'
COMMENTS_PATH = 'data/comments.json'


def import_json(path):
    with open(path, "r") as f:
        return json.load(f)


def get_comments_by_post_id(post_id):
    comments_list = []
    for comment in import_json(COMMENTS_PATH):
        if comment["post_id"] == post_id:
            comments_list.append(comment)
    return comments_list


def get_posts():
    results = []
    for post in import_json(POST_PATH):
        post["comments_count"] = len(get_comments_by_post_id(post['pk']))
        results.append(post)
    return results


def get_posts_by_post_id(post_id):
    post = {}
    for post in import_json(POST_PATH):
        if post["pk"] == post_id:
            return post


def get_posts_by_username(username):
    posts = []
    for post in import_json(POST_PATH):
        if post["poster_name"] == username:
            post["comments_count"] = len(get_comments_by_post_id(post['pk']))
            posts.append(post)
    return posts


