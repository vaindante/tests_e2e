import dataclasses
from typing import List

from furl import furl

from api.base import BaseAPI


@dataclasses.dataclass
class ClientApi(BaseAPI):
    base_url: furl = 'https://api.food.ru/content/v2'

    def __post_init__(self):
        if isinstance(self.base_url, str):
            self.base_url = furl(self.base_url)

    def search(self, query, params: dict = None, materials: str | List[str] = None):
        response = self.get(
            'search',
            params={
                'query': query,
                'format': 'json',
                'page': 1,
                'max_per_page': 20,
                'material': materials or ['recipe', 'product', 'news'],
                **(params if params is not None else {})
            },
        )

        assert response.status_code == 200

        return response.json()
