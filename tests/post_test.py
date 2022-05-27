class TestPost:

    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код """
        response = test_client.get('/post/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"

    def test_root_content(self, test_client):
        response = test_client.get('/post/1', follow_redirects=True)
        assert "<!DOCTYPE html>" in response.data.decode("utf-8"), "Контент страницы неверный"
