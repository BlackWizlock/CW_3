from flask import Blueprint, render_template, request
from utils.utils import search_for_posts

search_blueprint = Blueprint("search", __name__, template_folder="templates")


@search_blueprint.route("/")
def search_page():
    s = request.args.get("s")
    if s:
        return render_template(
            "search_result.html", search_request=search_for_posts(s)[:9]
        )
    return render_template("search.html")
