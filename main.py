herefrom kivy.app import App
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        return Label(text="Hello! Your App is Working")

if __name__ == "__main__":
    SimpleApp().run()
