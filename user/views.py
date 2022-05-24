from flask import Blueprint, render_template
from utils.utils import get_posts_by_user

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@user_blueprint.route("/<string:user_name>")
def user_page(user_name: str):
    posts = get_posts_by_user(user_name)
    return render_template("user.html", posts=posts)
