from flask import Blueprint, render_template
from utils.utils import get_post_by_pk, get_comments_by_post_id, re_subbing
from re import findall, sub

post_blueprint = Blueprint("post", __name__, template_folder="templates")


@post_blueprint.route("/<int:pk>")
def post_page(pk: int):
	post = get_post_by_pk(pk)
	comments = get_comments_by_post_id(pk)
	return render_template("post.html", post=post, pk=pk, comments=comments, content=re_subbing(post["content"]))
	