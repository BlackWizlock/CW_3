from flask import Blueprint, render_template, redirect
from utils.utils import json_write, get_post_by_pk, get_bookmarks_all, json_pop_write

bookmarks_blueprint = Blueprint("bookmarks", __name__, template_folder="templates")


@bookmarks_blueprint.route("/")
def bookmarks_page():
    database = get_bookmarks_all()
    return render_template("bookmarks.html", database=database)


@bookmarks_blueprint.route("/add/<int:pk>")
def bookmarks_page_by_pk(pk):
    json_write(get_post_by_pk(pk))
    return redirect("/", code=302)


@bookmarks_blueprint.route("/remove/<int:pk>")
def bookmarks_remove_page_by_pk(pk):
    json_pop_write(pk)
    return redirect("/bookmarks/", code=302)
