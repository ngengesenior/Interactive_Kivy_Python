from kivy.app import App
from kivy.uix.stacklayout import StackLayout
class Stack(StackLayout):
    pass


class ButtonTestApp(App):
    def build(self):
        self.title = "StackLayout"
        return Stack()
if __name__ == '__main__':
    ButtonTestApp().run()

