import ui.steps as steps


def test_first_ui(wd):
    steps.search(wd, 'солянка')
    results = steps.get_titles_recipe(wd)

    for title in results:
        assert 'солянка' in title
