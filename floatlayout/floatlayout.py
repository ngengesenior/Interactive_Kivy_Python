from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()
if __name__ == '__main__':
    FloatLayoutApp().run()