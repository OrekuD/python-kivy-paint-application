from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior
Config.set("graphics", "width", 1300)
Config.set("graphics", "height", 700)
Config.set("graphics", "resizable", False)
Config.set("input", "mouse", "mouse,disable_multitouch")


class Colors(ToggleButton):
    def _do_press(self):
        if self.state == "normal":
            ToggleButtonBehavior._do_press()


class WindowManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


sm = WindowManager()


class CanvasScreen(Screen):
    line_width = 2

    def on_touch_down(self, touch):
        if Screen.on_touch_down(self, touch):
            return
        with self.canvas:
            Color(1, 0.5, .3, 1)
            touch.ud["current_line"] = Line(points=
                                            (touch.x, touch.y),
                                            width=self.line_width)

    def set_line_width(self, line_width="Normal"):
        self.line.width = {"Thin": 1, "Normal": 2, "Thick": 4}[line_width]

    def on_touch_move(self, touch):
        if "current_line" in touch.ud:
            touch.ud["current_line"].points += (touch.x, touch.y)

    def clear(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)


kv = Builder.load_file("xcolors.kv")

screens = [MainScreen(name="main"), CanvasScreen(name="canvas")]

for screen in screens:
    sm.add_widget(screen)


class XColors(App):
    def build(self):
        return kv


if __name__ == "__main__":
    from kivy.core.window import Window
    Window.clearcolor = get_color_from_hex("#FFFFFF")
    XColors().run()

