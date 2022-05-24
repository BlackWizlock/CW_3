from flask import Blueprint, render_template
from utils.utils import search_for_posts

tag_blueprint = Blueprint("tag", __name__, template_folder="templates")


@tag_blueprint.route("/<string:tag>")
def tag_page(tag: str):
	return render_template("tag.html", search_request=search_for_posts(tag), tag=tag)
