from model import Model

class Controller:
    def __init__(self, view, model):
        self.model = model
        self.view = view
        self.view.fetch_data_command = self.fetch_data_and_update_view

    def fetch_data_and_update_view(self, stock_code):
        self.model.fetch_data(stock_code)
        self.view.update_view(self.model.data)