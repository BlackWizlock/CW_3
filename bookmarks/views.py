from flask import Blueprint, render_template

bookmarks_blueprint = Blueprint("bookmarks", __name__, template_folder="templates")


@bookmarks_blueprint.route("/")
def bookmarks_page():
	return render_template("bookmarks.html")
