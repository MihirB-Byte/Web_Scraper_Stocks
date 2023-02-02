import tkinter as tk
from model import Model
from view_tk import ViewTk
from controller import Controller

model = Model()
view = ViewTk(model=Model, controller= Controller)
controller = Controller(model=model, view=view)
view.controller = controller
view.mainloop()