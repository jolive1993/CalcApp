from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class DemoBox(BoxLayout):
    def __init__(self, **kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.buckets = 0
        self.garbage = 0
        self.funct = 0
        self.tracker = TextInput(text=str(self.buckets))
        self.tracker.size_hint = (1, .1)
        self.add_widget(self.tracker)
        buttons = GridLayout(cols=4)
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
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = 0
        self.funct = 4
    def multiplyer(self,obj):
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = 0
        self.funct = 3
    def equals(self,obj):

        try:
            buckets = int(self.buckets)
            garbage = int(self.garbage)
            if self.funct == 1:
                self.buckets = buckets +  garbage
            elif self.funct == 2:
                self.buckets = garbage - buckets
            elif self.funct == 3:
                self.buckets = garbage * buckets
            elif self.funct == 4:
                self.buckets = garbage / buckets
                self.buckets = float(self.buckets)
        except (ValueError, ZeroDivisionError) as e:
            print(e)
            self.buckets = 0

        
    def adder(self, obj):
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = 0
        self.funct = 1
    def minuser(self,obj):
        self.buckets = int(self.buckets)
        self.garbage = self.buckets
        self.buckets = 0
        self.funct = 2
    def numclear(self, obj):
        self.buckets = 0
    def press(self,obj):
        try:
            int(obj.text)
            self.buckets = str(self.buckets) + str(obj.text)
            self.tracker.text = str(float(self.buckets))
        except ValueError:
            self.symbolFunctions[obj.text](obj)
            self.tracker.text = str(float(self.buckets))


    def on_property(self, obj, value):
        print("Typical property change from", obj, "to", value)

class DemoApp(App):
    def build(self):
        return DemoBox()

if __name__ == "__main__":
    DemoApp().run()