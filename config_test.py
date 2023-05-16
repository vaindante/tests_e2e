import os


class Config:
    local_url = 'http://localhost:5001'
    server_url = 'https://server-for-traning.herokuapp.com/'
    user = os.getenv('TEST_USER')
    password = os.getenv('TEST_PASSWORD')
    local = os.getenv('LOCAL', '').lower() in ['1', 'true', 'yes']

    @property
    def url(self):
        return self.local and self.local_url or self.server_url


config = Config()
