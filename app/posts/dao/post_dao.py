import json
from re import findall, sub


class PostDAO:
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_post_all(self):
        """ Возвращает список со всеми данными"""
        posts = self._load_data()
        return posts

    def get_post_by_pk(self, pk):
        """ Возвращает один пост по его номеру"""
        posts = self._load_data()
        for post in posts:
            if post["pk"] == pk:
                return post

    def get_post_by_user(self, user_name):
        """ Возвращает лист сообщений по имени отправителя"""
        posts = self._load_data()
        output_data = []
        user_in_database = False
        for post in posts:
            if post["poster_name"].lower() == user_name.lower():
                output_data.append(post)
                user_in_database = True
        if not user_in_database:
            raise ValueError("Пользователь не найден")
        return output_data

    def search_for_posts(self, query):
        """ Возвращает список постов по ключевому слову"""
        posts = self._load_data()
        output_data = []
        for post in posts:
            if query.lower() in findall(r"\w+", post["content"].lower()):
                output_data.append(post)
        return output_data

    def re_subbing(self, content: str) -> str:
        """
        Построение наполнения поста с хэштегом и ссылкой на хэштег. Для поиска применен модуль re и паттерн замены sub
        :param content: пост для поиска хэштега
        :return: преобразованный пост со ссылками
        """
        hashtags = findall(r"#\w+\s", content)
        for item in hashtags:
            content = sub(
                    item, f'<a href="/tag/{item[1:-1]}" class="item__tag">{item}</a>', content
            )
        return content
