import csv
from dataclasses import dataclass

import xmltodict

from api.base_api import BaseAPI


@dataclass
class Api(BaseAPI):
    base_url: str = 'http://localhost:5000'

    def get(self, endpoint, *params, type_=None, **kwargs):
        if type_:
            kwargs['headers'] = self.prepare_kwargs(type_, kwargs.get('headers'))
        return self.session.get(
            # Concatenate endpoint with url
            (self.furl / endpoint).url,
            # Add query parameters
            params=params,
            # Add Any requests params_
            **kwargs
        )

    def get_users_json(self):
        response = self.get('users', type_='json')
        print(response)
        assert response.status_code == 200
        return response.json()

    def get_users_xml(self):
        response = self.get('users', type_='xml')
        assert response.status_code == 200
        print(response.text)
        return xmltodict.parse(response.text, xml_attribs=False)

    def get_users_csv(self):
        response = self.get('users', headers={'Accept': 'text/csv'})
        assert response.status_code == 200
        print(response.text)
        result = list(csv.DictReader(response.text.splitlines(), dialect='excel'))
        return result

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

    def delete_user_json(self, users):
        ...

    def delete_user_xml(self, users):
        ...
