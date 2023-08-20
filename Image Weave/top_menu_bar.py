from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout

from file_drop_down import FileDropDown
from segmentation_drop_down import SegmentationDropDown
from edge_drop_down import EdgeDropDown
from enhancement_drop_down import EnhancementDropDown
from texture_recognition_drop_down import TextureRecognitionDropDown

Builder.load_file("top_menu_bar.kv")


class TopMenuBar(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown_file = FileDropDown()
        self.segmentation_dropdown = SegmentationDropDown()
        self.edge_dropdown = EdgeDropDown()
        self.enhancement_dropdown = EnhancementDropDown()
        self.texture_dropdown = TextureRecognitionDropDown()

    def file_button_click(self, widget):
        self.dropdown_file.open(widget)

    def segmentation_button_click(self, widget):
        self.segmentation_dropdown.open(widget)

    def edge_button_click(self, widget):
        self.edge_dropdown.open(widget)

    def enhancement_button_click(self, widget):
        self.enhancement_dropdown.open(widget)

    def texture_button_click(self, widget):
        self.texture_dropdown.open(widget)

    @staticmethod
    def customizing_image_click():
        app = App.get_running_app()
        app.root.screen_manager.current = "customizing image processing"
        app.root.screen_manager.ids.selectedImage.source = app.root.selected_image_path
        app.root.screen_manager.ids.Processing_Image.source = app.root.selected_image_path
