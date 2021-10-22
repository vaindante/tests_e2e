from requests import Session
from xml.etree import ElementTree as ET


class Api(Session):
    base_url = 'http://localhost:2345/api'

    def get_users_json(self):
        content_type = 'application/json'
        response = self.get(f'{self.base_url}/users', headers={'Content-Type': content_type})
        assert response.status_code == 200
        return response.json()

    def get_users_xml(self):
        content_type = 'application/xml'
        response = self.get(f'{self.base_url}/users', headers={'Content-Type': content_type})
        assert response.status_code == 200
        return ET.parse(response.text)

    def get_user_json(self, name):
        ...

    def get_user_xml(self, name):
        ...

    def get_books_for_user_json(self, user_id):
        ...

    def get_books_for_user_xml(self, user_id):
        ...

    def create_user_json(self, json_data):
        ...

    def create_user_xml(self, xml_data):
        ...
ц
    def delete_user_json(self, users):
        ...

    def delete_user_xml(self, users):
        ...
