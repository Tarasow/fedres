class SearchContext:
    def __init__(self, batch_size, query):
        self.current_index = 0
        self.batch_size = batch_size
        self.query = query

    def update_for_next_page(self):
        self.current_index = self.current_index + self.batch_size
