# import tkinter as tk
#
# class ViewTk(tk.Tk):
#     def __init__(self, controller):
#         super().__init__()
#         self.title("Web Scraping App")
#         self.controller = controller
#
#         self.url_label = tk.Label(self, text="URL:")
#         self.url_entry = tk.Entry(self)
#         self.fetch_button = tk.Button(self, text="Fetch", command=self.controller.fetch_data_and_update_view)
#         self.data_label = tk.Label(self, text="Data:")
#         self.data_text = tk.Text(self, height=30, width=80)
#
#         self.url_label.grid(row=0, column=0)
#         self.url_entry.grid(row=0, column=1)
#         self.fetch_button.grid(row=0, column=2)
#         self.data_label.grid(row=1, column=0)
#         self.data_text.grid(row=2, column=0, columnspan=3)
#
#     def update_view(self, data):
#         self.data_text.delete("1.0", tk.END)
#         self.data_text.insert("1.0", data)

import tkinter as tk
from tkinter import ttk

class ViewTk:

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        self.window = tk.Tk()
        self.tree = None
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.window, columns=('Stock', 'Price'))
        self.tree.heading('#0', text='Stock')
        self.tree.heading('#1', text='Price')
        self.tree.column('#0', width=100, anchor='center')
        self.tree.column('#1', width=100, anchor='center')
        self.tree.pack()

        fetch_button = tk.Button(self.window, text='Fetch', command=lambda: self.controller.fetch_data_and_update_view('AAPL'))
        fetch_button.pack()

    def update_view(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for stock, price in data.items():
            self.tree.insert("", "end", values=(stock, price))

    def mainloop(self):
        self.window.mainloop()