from flask import json, abort
from re import findall, sub
from json import JSONDecodeError

URL_TO_DATA = "data/data.json"
URL_TO_COMMENTS = "data/comments.json"


def get_comments_all(url: str = URL_TO_COMMENTS):
    """
    Возвращает комментарии - RAW база.
    :param url ссылка на БД
    """
    try:
        with open(url, "r", encoding="UTF-8") as f:
            return json.load(f)
    except JSONDecodeError:
        return abort(400)
    except FileNotFoundError:
        return abort(400)


def get_posts_all(url: str = URL_TO_DATA):
    """
    Возвращает посты - RAW база.
    :param url ссылка на БД
    """
    try:
        with open(url, "r", encoding="UTF-8") as f:
            return json.load(f)
    except JSONDecodeError:
        return abort(400)
    except FileNotFoundError:
        return abort(400)


def get_posts_by_user(user_name: str, database: list = get_posts_all()):
    """
    Возвращает посты определенного пользователя.
    Функция должна вызывать ошибку `ValueError` если такого пользователя нет
    и пустой список, если у пользователя нет постов.
    """
    output_data = []
    user_not_in_database = True
    for line in database:
        if line["poster_name"] == user_name:
            output_data.append(line)
            user_not_in_database = False
    if user_not_in_database:
        # raise ValueError() # По курсовой тут райз - он останавливает сервер, реализовал через abort на 404 Page Not Found
        abort(404)
    return output_data


def get_comments_by_post_id(post_id: int, database: list = get_comments_all()):
    """
    Возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError` если такого поста нет
    и пустой список, если у поста нет комментов.
    """
    output_data = []
    post_id_not_in_database = True
    for line in database:
        if line["post_id"] == post_id:
            output_data.append(line)
            post_id_not_in_database = False
    if post_id_not_in_database:
        # raise ValueError() # По курсовой тут райз - он останавливает сервер, реализовал через abort на 404 Page Not Found
        abort(404)
    return output_data


def search_for_posts(query: str, database: list = get_posts_all()):
    """
    Возвращает список постов по ключевому слову.
    """
    output_data = []
    for line in database:
        if query.lower() in findall(r"\w+", line["content"].lower()):
            output_data.append(line)
    return output_data


def get_post_by_pk(pk: int, database: list = get_posts_all()):
    """
    Возвращает один пост по его идентификатору.
    """
    for line in database:
        if line["pk"] == pk:
            return line
    raise abort(400)


def re_subbing(content: str) -> str:
    hashtags = findall(r"#\w+\s", content)
    for item in hashtags:
        content = sub(item, f'<a href="/tag/{item[1:-1]}" class="item__tag">{item}</a>', content)
    return content
