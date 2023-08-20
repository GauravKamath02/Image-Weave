from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition

Builder.load_file("main_screen_manager.kv")


class MainScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition()

