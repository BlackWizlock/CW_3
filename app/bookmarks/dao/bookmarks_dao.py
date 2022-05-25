import json


class BookmarksDao:
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_bookmarks_all(self):
        """ Возвращает список со всеми данными"""
        posts = self._load_data()
        return posts

    def json_write(self, data_to_write):
        """
        Запись в json БД Bookmarks с проверкой уникальности записи, реализация через флаг possibility_to_add_data
        """
        bookmarks_database = self.get_bookmarks_all()
        possibility_to_add_data = True
        for line in bookmarks_database:
            if line["pk"] == data_to_write["pk"]:
                possibility_to_add_data = False
        if possibility_to_add_data:
            bookmarks_database.append(data_to_write)
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(bookmarks_database, f, ensure_ascii=False, indent=4)

    def json_pop_write(self, pk):
        """
        Pop в json БД Bookmarks
        """
        data = self.get_bookmarks_all()
        for i in range(len(data)):
            if data[i]["pk"] == pk:
                data.pop(i)
                break
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
