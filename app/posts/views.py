from flask import Blueprint, render_template, request, jsonify, redirect
from .dao.post_dao import PostDAO
from ..comments.dao.comment_dao import CommentsDAO
from ..bookmarks.dao.bookmarks_dao import BookmarksDao
import logging

logger_mine = logging.getLogger("logger")


index_blueprint = Blueprint('index', __name__, template_folder="templates")
search_blueprint = Blueprint('search', __name__, template_folder="templates")
post_blueprint = Blueprint('post', __name__, template_folder="templates")
user_blueprint = Blueprint("user", __name__, template_folder="templates")
api_blueprint = Blueprint("api", __name__, template_folder="templates")
tag_blueprint = Blueprint("tag", __name__, template_folder="templates")
bookmarks_blueprint = Blueprint("bookmarks", __name__, template_folder="templates")

posts = PostDAO("./data/data.json")
comments = CommentsDAO("./data/comments.json")
bookmarks = BookmarksDao("./data/bookmarks.json")


@index_blueprint.route('/')
def main_page():
    return render_template("index.html", database=posts.get_post_all(), bookmarks=len(bookmarks.get_bookmarks_all()))


@search_blueprint.route("/")
def search_page():
    s = request.args.get("s")
    if s:
        return render_template(
                "search_result.html", search_request=posts.search_for_posts(s)[:9]
        )
    return render_template("search.html")


@post_blueprint.route("/<int:pk>")
def post_page(pk: int):
    return render_template(
            "post.html",
            post=posts.get_post_by_pk(pk),
            pk=pk,
            comments=comments.get_comments_by_post_id(pk),
            content=posts.re_subbing(posts.get_post_by_pk(pk)["content"]),
    )


@user_blueprint.route("/<string:user_name>")
def user_page(user_name: str):
    return render_template("user.html", posts=posts.get_post_by_user(user_name))


@tag_blueprint.route("/<string:tag>")
def tag_page(tag: str):
    return render_template("tag.html", search_request=posts.search_for_posts(tag), tag=tag)


@bookmarks_blueprint.route("/")
def bookmarks_page():
    database = bookmarks.get_bookmarks_all()
    return render_template("bookmarks.html", database=database)


@bookmarks_blueprint.route("/add/<int:pk>")
def bookmarks_page_by_pk(pk):
    bookmarks.json_write(posts.get_post_by_pk(pk))
    return redirect("/", code=302)


@bookmarks_blueprint.route("/remove/<int:pk>")
def bookmarks_remove_page_by_pk(pk):
    bookmarks.json_pop_write(pk)
    return redirect("/bookmarks/", code=302)


@api_blueprint.route("/posts/")
@api_blueprint.route("/posts/<int:post_id>")
def api(post_id=None):
    if post_id:
        logger_mine.info(f"Запрос /api/posts/{post_id}")
        return jsonify(posts.get_post_by_pk(post_id))
    else:
        logger_mine.info(f"Запрос /api/posts/")
        return jsonify(posts.get_post_all())
