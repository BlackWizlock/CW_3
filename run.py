from flask import Flask

from app.posts.views import (index_blueprint,
                             api_blueprint,
                             search_blueprint,
                             post_blueprint,
                             user_blueprint,
                             tag_blueprint,
                             bookmarks_blueprint)

import logging

logging.basicConfig(level=logging.INFO)
logger_mine = logging.getLogger("logger")
handler = logging.FileHandler("./logs/api.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger_mine.addHandler(handler)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(search_blueprint, url_prefix='/search')
app.register_blueprint(post_blueprint, url_prefix='/post')
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(tag_blueprint, url_prefix='/tag')
app.register_blueprint(bookmarks_blueprint, url_prefix="/bookmarks")


# Обработка ошибок


@app.errorhandler(404)
@post_blueprint.errorhandler(404)
@search_blueprint.errorhandler(404)
@bookmarks_blueprint.errorhandler(404)
@tag_blueprint.errorhandler(404)
@user_blueprint.errorhandler(404)
def page_not_found(error):
    return (
            f"<h1><center><font color='red'>Error 404</font><br>Something goes wrong! Page not found.</center></h1><hr>"
    )


@index_blueprint.errorhandler(400)
@user_blueprint.errorhandler(400)
def database_not_found(error):
    return (
            f"<h1><center><font color='red'>Error 400</font>"
            f"<br>Database - problem</center></h1><hr>"
    )


@app.errorhandler(500)
def server_error(error):
    return (
            f"<h1><center><font color='red'>Server error 500</font></center></h1><hr>"
    )


if __name__ == '__main__':
    app.run(debug=True)
