from dataclasses import dataclass, field

from furl import furl
from requests import Session

contents_types = {
    'json': 'application/json',
    'xml': 'application/xml',
}


@dataclass
class BaseAPI:
    base_url: str
    session: Session = field(default_factory=Session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    @property
    def furl(self):
        return furl(self.base_url)

    @staticmethod
    def prepare_kwargs(type_, headers=None):
        headers = headers or {}
        headers['Accept'] = headers.get('Accept', contents_types[type_])
        return headers

    def get(self, endpoint, *params, type_=None, **kwargs):
        if type_:
            kwargs['headers'] = self.prepare_kwargs(type_, kwargs.get('headers'))
        return self.session.get(
            # Concatenate endpoint with url
            (self.furl / endpoint).url,
            # Add query parameters
            params=params,
            # Add Any requests params
            **kwargs
        )

    def post(self, endpoint, *params, type_, **kwargs):
        if type_:
            kwargs['headers'] = self.prepare_kwargs(type_, kwargs.get('headers'))
        return self.session.post(
            (self.furl / endpoint).url,
            params=params,
            **kwargs
        )
