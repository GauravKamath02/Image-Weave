from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.core.window import Window

from segmentation_click_handler import SegmentationClickHandler
from edge_detection_click_handler import EdgeDetectionClickHandler
from enhancement_click_handler import EnhancementClickHandler
from texture_recognition_click_handler import TextureRecognitionClickHandler

from main_screen_manager import MainScreenManager
from top_menu_bar import TopMenuBar


Window.size = (1020, 690)


class HomeLayout(BoxLayout):

    selected_image_path = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = dp(10)
        self.top_menu = TopMenuBar()
        self.screen_manager = MainScreenManager()
        self.add_widget(self.top_menu)
        self.add_widget(self.screen_manager)

    # Function to update the texture of images based on the computed value
    def update_texture(self, processed_image, colorfmt):
        texture = Texture.create(size=(processed_image.shape[1], processed_image.shape[0]), colorfmt=colorfmt)
        texture.blit_buffer(processed_image.tobytes(), colorfmt=colorfmt, bufferfmt='ubyte')
        self.screen_manager.ids.processedImage.texture = texture

    # Function to handel click event of buttons in the segmentation menu
    def segmentation_menu_click_handler(self, operation):
        self.screen_manager.current = "imageProcessing"
        self.screen_manager.ids.openedImage.source = self.selected_image_path
        segmentation_click_handler_instance = SegmentationClickHandler(self.selected_image_path)
        segmented_image = segmentation_click_handler_instance.menu_option_selected_create_thread(operation)
        Clock.schedule_once(lambda dt: self.update_texture(segmented_image, "bgr"))

    # Function to handel click event of buttons in the edge detection menu
    def edge_detection_menu_click_handler(self, operation):
        self.screen_manager.current = "imageProcessing"
        self.screen_manager.ids.openedImage.source = self.selected_image_path
        edge_detection_click_handler_instance = EdgeDetectionClickHandler(self.selected_image_path)
        segmented_image = edge_detection_click_handler_instance.menu_option_selected_create_thread(operation)
        Clock.schedule_once(lambda dt: self.update_texture(segmented_image, "luminance"))

    # Function to handel click event of buttons in the Enhancement menu
    def enhancement_menu_click_handler(self, operation):
        self.screen_manager.current = "imageProcessing"
        self.screen_manager.ids.openedImage.source = self.selected_image_path
        enhancement_click_handler_instance = EnhancementClickHandler(self.selected_image_path)
        enhanced_image = enhancement_click_handler_instance.menu_option_selected_create_thread(operation)
        Clock.schedule_once(lambda dt: self.update_texture(enhanced_image, "luminance"))

    def texture_recognition_menu_click_handler(self, operation):
        self.screen_manager.current = "imageProcessing"
        self.screen_manager.ids.openedImage.source = self.selected_image_path
        texture_recognition_click_handler_instance = TextureRecognitionClickHandler(self.selected_image_path)
        enhanced_image = texture_recognition_click_handler_instance.menu_option_selected_create_thread(operation)
        Clock.schedule_once(lambda dt: self.update_texture(enhanced_image, "rgba"))


class PortalApp(App):
    pass


if __name__ == "__main__":
    PortalApp().run()

