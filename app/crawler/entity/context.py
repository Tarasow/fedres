from app.crawler.common.context_base import ContextBase


class EntityContext(ContextBase):
    def __init__(self, batch_size, guid):
        super().__init__(batch_size)
        self.guid = guid
