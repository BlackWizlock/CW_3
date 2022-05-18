from flask import json

URL_TO_DATA = '../data/data.json'
URL_TO_COMMENTS = "../data/comments.json"


def get_posts_all(url: str = URL_TO_DATA):
	"""
	Возвращает посты.
	"""
	with open(url, 'r', encoding='UTF-8') as f:
		return json.load(f)


def get_posts_by_user(user_name):
	"""
	Возвращает посты определенного пользователя.
	Функция должна вызывать ошибку `ValueError` если такого пользователя нет
	и пустой список, если у пользователя нет постов.
	"""
	pass


def get_comments_by_post_id(post_id):
	"""
	Возвращает комментарии определенного поста.
	Функция должна вызывать ошибку `ValueError` если такого поста нет
	и пустой список, если у поста нет комментов.
	"""
	pass


def search_for_posts(query):
	"""
	Возвращает список постов по ключевому слову.
	"""
	pass


def get_post_by_pk(pk):
	"""
	Возвращает один пост по его идентификатору.
	"""
	pass
