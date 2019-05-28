from app.crawler.common.context_base import ContextBase


class SearchContext(ContextBase):
    def __init__(self, batch_size, query):
        super().__init__(batch_size)
        self.query = query
