import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class WidgetExample(GridLayout):
    press_property=StringProperty()
    def on_press_button(self):
        print("printed")
        self.press_property="This App created by suresh"
class Android(App):
    pass

Android().run()