from flask import Blueprint, render_template
from utils.utils import search_for_posts

search_blueprint = Blueprint("search", __name__, template_folder="templates")


@search_blueprint.route("/")
def search_page():
	return render_template("search.html")
