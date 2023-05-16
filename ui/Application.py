from furl import furl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.MainPage import MainPage
from ui.SearchPage import SearchPage


class Application:
    # auth_page: 'AuthPage'
    search_page: 'SearchPage'
    main_page: 'MainPage'

    def __init__(self, url):
        self.base_url = furl(url)

        self.wd = webdriver.Chrome(ChromeDriverManager().install())

        self.search_page = SearchPage(self.wd, self)
        self.main_page = MainPage(self.wd, self)

        self.main_page.open('/')

    def close(self):
        self.wd.close()
