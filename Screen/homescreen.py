from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Homescreen(MDScreen):
    def __init__(self, **kw):
        Builder.load_file("kv/homescreen.kv")
        super().__init__(**kw)