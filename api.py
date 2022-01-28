import csv
import logging
from dataclasses import dataclass, field
from functools import wraps

import xmltodict
from furl import furl
from requests import Session

contents_types = {
    'json': 'application/json',
    'xml': 'application/xml',
}
logging.basicConfig(level='DEBUG')

def prepare_kwargs(method):
    # TODO: Упростить
    @wraps(method)
    def wrapper(self, endpoint=None, content_type='json', *params, **kwargs):
        headers = kwargs.get('headers', {})
        headers['Accept'] = headers.get('Accept', contents_types[content_type])
        kwargs['headers'] = headers
        return method(self, endpoint=endpoint, *params, **kwargs)

    return wrapper


@dataclass
class Api:
    base_url: str = 'http://localhost:5000'
    session: Session = field(default_factory=Session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    @property
    def furl(self):
        return furl(self.base_url)

    @prepare_kwargs
    def get(self, endpoint, *params, **kwargs):
        return self.session.get(
            # Concatenate endpoint with url
            (self.furl / endpoint).url,
            # Add query parameters
            params=params,
            # Add Any requests params
            **kwargs
        )

    @prepare_kwargs
    def post(self, endpoint, *params, **kwargs):
        return self.session.post(
            (self.furl / endpoint).url,
            params=params,
            **kwargs
        )

    def get_users_json(self):
        response = self.get('users', content_type='json')
        assert response.status_code == 200
        return response.json()

    def get_users_xml(self):
        response = self.get(f'users', content_type='xml')
        assert response.status_code == 200
        print(response.text)
        return xmltodict.parse(response.text, xml_attribs=False)

    def get_users_csv(self):
        response = self.get(f'users', headers={'Accept': 'text/csv'})
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
