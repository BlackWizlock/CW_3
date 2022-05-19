from flask import Blueprint, render_template

search_blueprint = Blueprint("search", __name__, template_folder="templates")


@search_blueprint.route("/")
def search_page():
	return render_template("search.html")
