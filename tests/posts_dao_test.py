from app.posts.dao.post_dao import PostDAO

import pytest


# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится только один раз, поэтому выносить в conftest не будем
@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostDAO("./data/data.json")
    return posts_dao_instance


# Задаем, какие ключи ожидаем получать у кандидата
keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestPostDao:

    def test_get_post_all(self, posts_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = posts_dao.get_post_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_post_by_pk(self, posts_dao):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        posts = posts_dao.get_post_by_pk(1)
        assert (posts["pk"] == 1), "возвращается неправильный пост"
        assert set(posts.keys()) == keys_should_be, "неверный список ключей"

    def test_get_post_by_user(self, posts_dao):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        posts = posts_dao.get_post_by_user("leo")
        assert (posts[0]["poster_name"] == "leo"), "возвращается неправильный пользователь"
        assert (posts[0]["poster_name"] != "slonik"), "Пользователь не найден"
