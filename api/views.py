from flask import Blueprint, jsonify
from utils.utils import get_posts_all, get_post_by_pk
import logging

logging.basicConfig(level=logging.INFO, style="{")

logger_mine = logging.getLogger("logger")
handler = logging.FileHandler("logs/api.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger_mine.addHandler(handler)

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route('/posts')
@api_blueprint.route('/posts/<int:post_id>')
def api(post_id=None):
    if post_id:
        logger_mine.info(f"Запрос /api/posts/{post_id}")
        return jsonify(get_post_by_pk(post_id))
    else:
        logger_mine.info(f"Запрос /api/posts/")
        return jsonify(get_posts_all())
