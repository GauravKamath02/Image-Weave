from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import imghdr

Builder.load_file("file_open.kv")


class FileOpen(BoxLayout):

    def selected_file(self, widget):
        # Checking if the file is an image and list is not empty
        if len(widget) > 0 and imghdr.what(widget[0]) is not None:
            path = widget[0]
            self.ids.my_image.source = path
            app = App.get_running_app()
            app.root.selected_image_path = widget[0]
