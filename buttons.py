
from  kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget
from  kivy.uix.popup import Popup
from kivy.properties import  ObjectProperty

class Widgets(Widget):
    def __init__(self,**kwargs):
        super(Widgets, self).__init__(**kwargs)

    popup =  ObjectProperty(None)
    def tell(self):
        popup = Popup(title = "Comment",content = Label(text = "She is a beautiful lady"),
                          size_hint = (None,None),size = (200,200))
        popup.open()
        popup.on_touch_down(popup.dismiss())

class WidgetsApp(App):
    def build(self):
        return Widgets()
if __name__ == '__main__':
    WidgetsApp().run()