from abc import ABC, abstractmethod
import requests


class HandlerBase(ABC):

    @property
    def request_url(self):
        raise NotImplementedError

    @abstractmethod
    def create_post_data(self, ctx):
        raise NotImplementedError

    # FIXME better solution is to get user agent from set of different agents
    @classmethod
    def get_post_headers(cls):
        return {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36',
            'Content-Type': 'application/json'
        }

    def get_result_page(self, ctx):
        post_data = self.create_post_data(ctx)
        response = requests.post(self.request_url, data=post_data, headers=self.get_post_headers())
        assert response.status_code == 200
        return response.text
