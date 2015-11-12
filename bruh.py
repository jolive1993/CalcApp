from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, FadeTransition
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty



class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 5
        self.padding = 5
        self.num1 = 0
        self.num2 = 0
        self.funct = 0
        self.deciPressed = 0
        self.tracker = Label(text=str(self.num1), font_size=50, halign='center')
        self.tracker.size_hint = (1, .1)
        self.add_widget(self.tracker)
        clear = Button(text="Clear", font_size=24, background_color=(3,2,3,2))
        clear.size_hint = (1, .1)
        clear.bind(on_press = self.press)
        buttons = GridLayout(cols=4, spacing=5)
        self.add_widget(buttons)
        self.add_widget(clear)
        butts = []
        for i in range(10):
            butts.append(str(i))
        butts.append("+")
        butts.append("-")
        butts.append("*")
        butts.append("/")
        butts.append("=")
        butts.append(".")
        for butt in butts:
            b = Button(text=str(butt))
            b.bind(on_press=self.press)
            b.background_color = (3,1,1,1)
            b.font_size = (24)
            buttons.add_widget(b)
            

        self.symbolFunctions = {
            "+":self.adder,
            "-":self.minuser,
            "=":self.equals,
            "*":self.multiplyer,
            "/":self.divider,
            ".":self.decimal,
            "Clear":self.numclear
        }

    def divider(self,obj):
        self.num1 = int(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 4
        self.deciPressed = 0
    def multiplyer(self,obj):
        self.num1 = int(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 3
        self.deciPressed = 0
    def equals(self,obj):

        try:
            num1 = float(self.num1)
            num2 = float(self.num2)
            self.deciPressed = 1
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
        self.num1 = float(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 1
        self.deciPressed = 0
    def minuser(self,obj):
        self.num1 = float(self.num1)
        self.num2 = self.num1
        self.num1 = 0
        self.funct = 2
        self.deciPressed = 0
    def numclear(self, obj):
        self.num1 = 0
        self.deciPressed = 0
    def press(self, obj):
        try:
            int(obj.text)
            self.num1 = str(self.num1) + str(obj.text)
            self.tracker.text = str(float(self.num1))
        except ValueError:
            self.symbolFunctions[obj.text](obj)
            self.tracker.text = str(float(self.num1))
    def decimal(self, obj):
        if self.deciPressed == 0:
            self.num1 = str(self.num1) + (".")
            self.deciPressed = 1
        else:
            self.num1 = str(self.num1)
    def change(self, obj):
        root.current = 'Tit %d'
        


class CalcApp(App):
    def build(self):
        root = ScreenManager(transition=FadeTransition())
        screen = Screen(name='Title %d')
        screen2 = Screen(name='Tit %d')
        screen.add_widget(MainLayout())
        screen2.add_widget(MainLayout())
        root.add_widget(screen)
        root.add_widget(screen2)
        return root

if __name__ == "__main__":
    CalcApp().run()