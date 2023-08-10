from kivy.app import App
from kivy.uix.button import Button


class LanguageLearnerApp(App):
    def build(self):
        return Button(
            text='Hello World',
            pos=(50,100),
            size_hint=(None,None),
            size=(300,200))



if __name__ == '__main__':
    LanguageLearnerApp().run()