from pprint import pprint

import pytest


@pytest.mark.api
class TestTheme7:

    def test_first_json(self, api):
        users = api.get_users_json()
        pprint(users)
        assert len(users) == 10
        """
        10 Юзеров
        [
            {
                'username': 'Joshua',
                'book_coounter': 10,
                'created': '2014-10-17'
            }
        ]
        """
        """
        1. Реализовать проверку что все пользователи упорядочены по дате создания
        2. Реализовать Проверку что у всех пользоватлей есть имя и количество книг
        """

    @pytest.mark.demo
    def test_diff(self, api):
        """
        Для демонстрации ответов
        """
        users_json = api.get_users_json()
        users_xml = api.get_users_xml()
        users_csv = api.get_users_csv()
        pprint(users_xml)
        pprint(users_json)
        print(users_csv)

    @pytest.mark.demo
    def test_diff_errors(self):
        pass

    def test_first_xml(self, api):
        users = api.get_users_xml()
        pprint(users)
        assert len(users) == 10
        ...

        """
        1. Реализовать проверку что все пользователи упорядочены по дате создания
        2. Реализовать Проверку что у всех пользоватлей есть имя и количество книг
        """

    def test_book_json(self, api):
        ...
        """
        1. Получить список книг пользоватлей
        2. Проверить что количество полученных книг совпадает с информацией полученной у пользовательская
        3. При нахожениее ошибок, они должны быть понятны и читаемы   
        """

    def test_book_xml(self, api):
        ...
        """
        1. Получить список книг пользоватлей
        2. Проверить что количество полученныъх книг совпадает с информацией полученной у пользовательская
        3. При нахожениее ошибок, они должны быть понятны и читаемы   
        """

    def test_create_delete(self, api):
        ...
        """
        1. Создать пользователя
        2. Проверить отдельный запросом, что пользователь создался
        3. Удалить пользовательская
        4. Проверить что пользователь удален.
        
        """
