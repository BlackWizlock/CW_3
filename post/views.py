from flask import Blueprint, render_template

post_blueprint = Blueprint("post", __name__, template_folder="templates")


@post_blueprint.route("/")
def post_page():
	return render_template("post.html")
