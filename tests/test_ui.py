import pytest


class TestUI:
    def test_search(self, app):
        query = 'солянка'

        app.main_page.search(query)
        results = app.search_page.get_recipe_titles()

        assert all(query in title.lower() for title in results)

    # @pytest.mark.parametrize(
    #     'query,valid',
    #     (
    #             ('Рецепты', 'рецепт'),
    #             ('Продукты', 'продукт'),
    #             ('Статьи', 'статья')
    #     ))
    # def test_filter(self, app, query, valid):
    #     app.main_page.search('борщ')
    #
    #     app.search_page.add_filter(query)
    #
    #     for title in app.search_page.get_recipe_type():
    #         # casefold Более агресивный lower, и в отличие от него не дает ошибок.
    #         # Плюс является рекомендованным методом сравнения, от разработчиков Python
    #         assert title.casefold() == valid.casefold()
