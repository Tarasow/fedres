from abc import ABC, abstractmethod


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

    async def get_result_page(self, ctx, client):
        post_data = self.create_post_data(ctx)
        async with client.post(self.request_url, data=post_data, headers=self.get_post_headers()) as resp:
            assert resp.status == 200
            return await resp.text()
