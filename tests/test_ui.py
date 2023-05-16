class TestUI:
    def test_search(self, app):
        query = 'солянка'

        app.main_page.search(query)
        results = app.search_page.get_recipe_titles()

        assert all(query in title.lower() for title in results)
