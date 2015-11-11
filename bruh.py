from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 5
        self.padding = 5
        self.num1 = 0
        self.num2 = 0
        self.funct = 0
        self.tracker = Label(text=str(self.num1), font_size=50, halign='center')
        self.tracker.size_hint = (1, .1)
        self.add_widget(self.tracker)
        buttons = GridLayout(cols=4, spacing=5)
        self.add_widget(buttons)
        butts = []
        for i in range(10):
            butts.append(str(i))
        butts.append("+")
        butts.append("-")
        butts.append("*")
        butts.append("/")
        butts.append("=")
        butts.append("clear")
        for butt in butts:
            b = Button(text=str(butt))
            b.bind(on_press=self.press)
            buttons.add_widget(b)

        self.symbolFunctions = {
            "+":self.adder,
            "-":self.minuser,
            "=":self.equals,
            "*":self.multiplyer,
            "/":self.divider,
            "clear":self.numclear
        }

    def divider(self,obj):
        self.num1 = int(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 4
    def multiplyer(self,obj):
        self.num1 = int(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 3
    def equals(self,obj):

        try:
            num1 = int(self.num1)
            num2 = int(self.num2)
            if self.funct == 1:
                self.num1 = num1 +  num2
            elif self.funct == 2:
                self.num1 = num2 - num1
            elif self.funct == 3:
                self.num1 = num2 * num1
            elif self.funct == 4:
                self.num1 = num2 / num1
                self.num1 = float(self.num1)
        except (ValueError, ZeroDivisionError) as e:
            print(e)
            self.num1 = 0

  
    def adder(self, obj):
        self.num1 = int(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 1
    def minuser(self,obj):
        self.num1 = int(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 2
    def numclear(self, obj):
        self.num1 = 0
    def press(self, obj):
        try:
            int(obj.text)
            self.num1 = str(self.num1) + str(obj.text)
            self.tracker.text = str(float(self.num1))
        except ValueError:
            self.symbolFunctions[obj.text](obj)
            self.tracker.text = str(float(self.num1))


class CalcApp(App):
    def build(self):
        root = MainLayout()
        return root

if __name__ == "__main__":
    CalcApp().run()