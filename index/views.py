from flask import Blueprint, render_template
from utils.utils import get_posts_all

index_blueprint = Blueprint("index", __name__, template_folder="templates")

DATABASE_POSTS = get_posts_all()


@index_blueprint.route("/")
def index_page():
	return render_template("index.html", database=DATABASE_POSTS)
