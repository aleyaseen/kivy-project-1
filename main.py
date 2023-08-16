from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

from Screen.screens import *

class WindowManager(ScreenManager):
    pass

class Scan_Raray(MDApp):
    CLASSES = {
        'welcome':'screens.welcome',
        'login':'screens.login',
        'signup':'screens.signup',
        'homescreen':'screens.homescreen',}
    AUTORELOADER_PATH = [
        ('.', {'recursive':True})
    ]
    KV_FILES = [
        'kv/welcome.kv',
        'kv/login.kv',
        'kv/signup.kv',
        'kv/homescreen.kv'
    ]
    def build_app(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name="welcome"),
            Login(name="login"),
            Signup(name="signup")
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == "__main__":
    LabelBase.register(name="BMontserrat", fn_regular="Resources/Fonts/Montserrat-Bold.ttf")
    LabelBase.register(name="MMontserrat", fn_regular="Resources/Fonts/Montserrat-Medium.ttf")
    Scan_Raray().run()