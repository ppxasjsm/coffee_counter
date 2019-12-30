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


class Users():
    def __init__(self, userData=None):
        if userData is None:
            self._columns = ['name', 'surname', 'email', 'balance', 'tea count', 'coffee count', 'last paid', 'id']
            self._userData = pd.DataFrame(columns=self._columns)
        else:
            pass

    def get_user_balance(self, name, surname=None, id=None):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]
        return self._userData.iloc[index]['balance']

    def get_user_email(self, name, surname=None, id=None):
        name = name.lower()
        print (name)
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        print(index_list)
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]
        return self._userData.iloc[index]['email']

    def is_user(self, name, surname=None, id=None):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]

    def get_number_of_teas(self, name, surname=None, id=None):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]
        return self._userData.iloc[index]['tea count']

    def get_number_of_coffees(self, name, surname=None, id=None):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]
        return self._userData.iloc[index]['coffee count']

    def add_user(self, user_dict):
        # check if the dictionary has all the right entries
        def compare(x, y):
            return collections.Counter(x) == collections.Counter(y)

        if compare(user_dict.keys(), self._columns):
            # add data to dataframe
            self._userData = self._userData.append(user_dict, ignore_index=True)
        else:
            raise ValueError("The new user data does not contain necessary columns")

    def add_coffee(self, name):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]
        bal = self._userData.iloc[index]['balance']
        bal = bal + 0.4
        self._userData.at[index, 'balance'] = bal
        counter = self._userData.iloc[index]['coffee count']
        counter += 1
        self._userData.at[index, 'coffee count'] = counter

    def add_tea(self, name):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]
        bal = self._userData.iloc[index]['balance']
        bal = bal + 0.15
        self._userData.at[index, 'balance'] = bal
        counter = self._userData.iloc[index]['tea count']
        counter += 1
        self._userData.at[index, 'tea count'] = counter

    def paid(self, name):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]

        # Setting counters to zero
        self._userData.at[index, 'tea count'] = 0
        self._userData.at[index, 'coffee count'] = 0
        self._userData.at[index, 'balance'] = 0
        self._userData.at[index, 'last paid'] = date.today()

    def get_last_paid_info(self, name):
        index_list = self._userData.index[self._userData['name'] == name].tolist()
        if len(index_list) == 0:
            raise ValueError("The name %s could not be found in the user list!" % name)
        index = index_list[0]
        return self._userData.iloc[index]['last paid']

    @property
    def userData(self):
        return self._userData


def press_callback(obj, user):
    print("Button pressed,", obj.text)
    if obj.text is "Add a coffee to my account":
        user.bal


class Button_Widget(Widget):

    def __init__(self, text, pos_hint=None, **kwargs):
        super(Button_Widget, self).__init__(pos_hint=pos_hint, size_hint=(None, None), **kwargs)
        btn1 = Button(text=text)
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

    def callback(self, instance):
        print('The button %s state is <%s>' % (instance, instance.state))


class CoffeeApp(App):
    title = 'Coffee Counter'

    def build(self):
        # Set up the layout:
        layout = FloatLayout()

        # Make the background gray:
        with layout.canvas.before:
            Color(.2, .2, .2, 1)

        coffee_button = Button(text='Add a coffee to my account',
                               font_size="20sp",
                               background_color=(1, 1, 1, 1),
                               color=(1, 1, 1, 1),
                               size=(32, 32),
                               size_hint=(.2, .2),
                               pos=(300, 250))
        coffee_button.bind(on_press=press_callback)
        tea_button = Button(text='Add a tea to my account',
                            font_size="20sp",
                            background_color=(1, 1, 1, 1),
                            color=(1, 1, 1, 1),
                            size=(32, 32),
                            size_hint=(.2, .2),
                            pos=(300, 100))
        tea_button.bind(on_press=press_callback)
        layout.add_widget(coffee_button)
        layout.add_widget(tea_button)
        return layout


if __name__ == '__main__':
    CoffeeApp().run()
