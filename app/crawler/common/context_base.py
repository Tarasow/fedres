from abc import ABC


class ContextBase(ABC):

    def __init__(self, batch_size):
        self.current_index = 0
        self.batch_size = batch_size

    def update_for_next_page(self):
        self.current_index = self.current_index + self.batch_size
