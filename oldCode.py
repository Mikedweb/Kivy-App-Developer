# Sizing and positioning part 1
# from kivy.app import App
# from kivy.uix.button import Button


# class LanguageLearnerApp(App):
#     def build(self):
#         return Button(
#             text='Hello World',
#             pos=(50,50),
#             size=(500,500),
#             # size_hint=(.8,.8),
#             size_hint=(None,None))


# if __name__ == '__main__':
#     LanguageLearnerApp().run()

# Sizing and positioning part 2
# from kivy.app import App
# from kivy.uix.button import Button


# class FunkyButton(Button):
#     def __init__(self, **kwargs):
#         super(FunkyButton, self).__init__(**kwargs)
#         self.text="Funky button"
#         self.pos=(100,100)
#         self.size_hint=(.25,.25)


# class LanguageLearnerApp(App):
#     def build(self):
#         # return FunkyButton(
#         #     text="Funky button",
#         #     pos=(100,100),
#         #     size_hint=(.5,.5)
#         # ) 
#         return FunkyButton()   


# if __name__ == '__main__':
#     LanguageLearnerApp().run()

# Sizing and positioning part 3
# from kivy.app import App
# from kivy.uix.button import Button


# class FunkyButton(Button):
#     pass


# class LanguageLearnerApp(App):
#     def build(self):
#         return FunkyButton(
#             pos=(100,100),
#             size_hint=(None,None),
#             size=(500,500)
#         )   


# if __name__ == '__main__':
#     LanguageLearnerApp().run()

# Sizing and positioning part 4, 5
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget


# class GameScreen(Widget):
#     pass


# class LanguageLearnerApp(App):
#     def build(self):
#         return GameScreen()


# if __name__ == '__main__':
#     LanguageLearnerApp().run()

# Displaying text
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label


# class GameScreen(Widget):
#     pass


# class LanguageLearnerApp(App):
#     def build(self):
#         game_screen = GameScreen()
#         game_screen.add_widget(
#             Label(text='Hello World')
#         )

#         return game_screen


# if __name__ == '__main__':
#     LanguageLearnerApp().run()

# Displaying images,
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label


# class GameScreen(Widget):
#     pass


# class LanguageLearnerApp(App):
#     def build(self):
#         game_screen = GameScreen()
#         return game_screen


# if __name__ == '__main__':
#     LanguageLearnerApp().run()

# Properties
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label
# from kivy.properties import StringProperty, NumericProperty

# class GameScreen(Widget):
#     label_text = StringProperty("")
#     numeric = NumericProperty(0)
    
#     def __init__(self, **kwargs):
#         super(GameScreen, self).__init__(**kwargs)

#         self.numeric = 10
#         self.label_text = "Here is some text"


# class LanguageLearnerApp(App):
#     def build(self):
#         game_screen = GameScreen()
#         return game_screen


# if __name__ == '__main__':
#     LanguageLearnerApp().run()

# Buttons
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty

class GameScreen(Widget):
    

    def press_button(self):
        print("Button pressed!")


class LanguageLearnerApp(App):
    def build(self):
        game_screen = GameScreen()
        return game_screen


if __name__ == '__main__':
    LanguageLearnerApp().run()