from pprint import pprint


class TestApi:
    def test_search(self, api):
        result = api.search('борщ')
        pprint(result)

        for recipe in result['materials']:
            assert 'борщ' in recipe['main_title'].casefold()
