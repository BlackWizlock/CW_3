from flask import Blueprint, render_template
from utils.utils import get_posts_all

index_blueprint = Blueprint("index", __name__, template_folder="templates")


@index_blueprint.route("/")
def index_page():
	database = get_posts_all()  # обновление прогрузки базы тк база могла обновиться
	return render_template("index.html", database=database)
