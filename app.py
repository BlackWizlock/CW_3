from flask import Flask

from user.views import user_blueprint
from tag.views import tag_blueprint
from search.views import search_blueprint
from post.views import post_blueprint
from index.views import index_blueprint
from bookmarks.views import bookmarks_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix="/user/")
app.register_blueprint(tag_blueprint, url_prefix="/tag/")
app.register_blueprint(search_blueprint, url_prefix="/search/")
app.register_blueprint(post_blueprint, url_prefix="/post/")
app.register_blueprint(index_blueprint, url_prefix="/")
app.register_blueprint(bookmarks_blueprint, url_prefix="/bookmarks/")

if __name__ == "__main__":
	app.run(debug=True)
