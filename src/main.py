from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle



class Button_Widget(Widget):

    def __init__(self,text,pos_hint=None, **kwargs):
        super(Button_Widget, self).__init__(pos_hint=pos_hint,size_hint=(None, None),**kwargs)
        btn1 = Button(text=text)
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

    def callback(self, instance):
        print('The button %s state is <%s>' % (instance, instance.state))


class CoffeeApp(App):
    def build(self):
        # Set up the layout:
        layout = FloatLayout()

        # Make the background gray:
        with layout.canvas.before:
            Color(.2, .2, .2, 1)

        coffee_button = Button(text='coffee',
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
        tea_button = Button(text='tea',
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 100))
        layout.add_widget(coffee_button)
        layout.add_widget(tea_button)
        return layout

if __name__ == '__main__':
    CoffeeApp().run()