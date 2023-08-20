"""
File selection menu, allows the user to select the options in the drop-down menu in the file button.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown

Builder.load_file("file_drop_down.kv")


class FileDropDown(DropDown):

    @staticmethod
    def file_open_click_handler():
        app = App.get_running_app()
        app.root.screen_manager.current = "fileOpenScreen"

