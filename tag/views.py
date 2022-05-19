from flask import Blueprint, render_template

tag_blueprint = Blueprint("tag", __name__, template_folder="templates")


@tag_blueprint.route("/")
def tag_page():
	return render_template("tag.html")
