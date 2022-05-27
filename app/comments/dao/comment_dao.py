import json


class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id):
        """ Возвращает лист комментариев по id поста"""
        comments = self._load_data()
        output_data = []
        post_id_not_in_database = True
        for line in comments:
            if line["post_id"] == post_id:
                output_data.append(line)
                post_id_not_in_database = False
        if post_id_not_in_database:
            raise ValueError("ID не найден")
        return output_data
