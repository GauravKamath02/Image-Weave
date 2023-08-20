from kivy.uix.widget import Widget


class RectangleSelection(Widget):
    def on_touch_down(self, touch):
        self.touch_start = touch.pos
        self.touch_end = None
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        self.touch_end = touch.pos
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self.touch_end = touch.pos
        return super().on_touch_up(touch)