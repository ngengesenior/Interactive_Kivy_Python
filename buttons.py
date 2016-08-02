from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
class Widgets(BoxLayout):
    pass
class WidgetsApp(App):
    def build(self):
        return Widgets()
if __name__ == '__main__':
    WidgetsApp().run()